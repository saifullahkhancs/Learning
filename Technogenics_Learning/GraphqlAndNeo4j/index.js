import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';
import { Neo4jGraphQL } from "@neo4j/graphql";
import neo4j from "neo4j-driver";
import fs from 'fs';
const typeDefs = fs.readFileSync('schema/schema.graphql', 'utf8');

// Initialize Neo4j Driver
const driver = neo4j.driver(
  'bolt://localhost:7687',
  neo4j.auth.basic('trunk_portal_user', 'zb03bTl463gppTmZ'), 
 // neo4j.auth.basic('neo4j', 'saif.7117755'), // replace with your Neo4j credentials
  {
  logging: {
    level: 'debug',  // Set to 'debug' for detailed logs including Cypher queries
    logger: (level, message) => console.log(`[${level}] ${message}`)
  }
  }
  // {
  //   logging: {
  //     level: 'debug' // Options: 'ERROR', 'WARN', 'INFO', 'DEBUG'
  //   }
  // }
);




// const typeDefs =  from schema.graphql
const resolvers = {
  Tactic: {
    has: async (tactic, { limit = 10 }, { driver }) => {
      const session = driver.session();
      const query = `
        MATCH (tact:Tactic {srid: $tacticSrid})-[rel:HAS]->(tech:Technique)
        RETURN tech, rel
        LIMIT $limit
      `;

      const result = await session.run(query, {
        tacticSrid: tactic.srid,
        limit: limit, // Specify the limit for the number of techniques
      });

      session.close();

      // Process the result to return the limited techniques associated with the tactic
      return result.records.map(record => record.get('tech').properties);
    },
  },
};



const session = driver.session();
  try {
    // Run a simple query to test connection
    await session.run('RETURN 1');
   // console.log('Successfully connected to the Neo4j database');
  } catch (error) {
    console.error('Failed to connect to Neo4j:', error);
  } finally {
    await session.close();
  }



// Create Neo4jGraphQL instance
const neoSchema = new Neo4jGraphQL(
  {
    typeDefs, 
    driver ,
    config: {
      enableDebug: true,  // Enable debug mode
  },

});
console.log(neoSchema.schema);

// Apollo Server setup
const server = new ApolloServer({
  schema: await neoSchema.getSchema(),
});

const { url } = await startStandaloneServer(server, {
  context: async ({ req }) => {
    // Log the name of the incoming GraphQL operation
    console.log(`Received request for ${req.body}`);

    // Return the request object to be used in resolvers if needed
    return { req };
  },
  listen: { port: 4000 },
});

console.log(`🚀 Server ready at ${url}`);

