import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';
import { Neo4jGraphQL } from "@neo4j/graphql";
import neo4j from "neo4j-driver";

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




  const typeDefs = `
  type Strike {
  uid: String
  srid: String
  name: String
  verified: Boolean
  hasTransaction: [Transaction!]! @relationship(type: "HAS_TRANSACTION", direction: OUT)
}
   type Tactic {
  uid: String
  srid: String
  name: String
  displayName: String
  description: String
  mitreId: String
   has(sourceSRID: String!): [Technique!]! 
          @cypher(
            statement: """
            MATCH (this)-[rel:HAS]->(tech:Technique)
            WHERE rel.sourceSRID = $sourceSRID
            RETURN tech
            LIMIT 5
            """
          )
  }
interface TacticHasTechniques @relationshipProperties {
  sourceSRID: String
  label: String
  uid: String
}

type Technique {
    detection: String
    refs: String
    name: String
    displayName: String
    defenseBypassed: String
    description: String
    permission: String
    mitreId: String
    dataSources: String
    version: String
    platform: String
    tactic: String
    uid: String
    srid: String
    partOf: [Tactic!]! @relationship(type: "PART_OF", direction: OUT, properties: "TacticHasTechniques")
    
  }

  type Transaction {
  uid: String
  srid: String
  domain: String
  url: String
  urlType: String
  stage: String
  description: String
  configuration: String
  family: String
  objType: String
  date: String
  vtScore: String
  protocol: String
  replayMode: String
  impact: String
  flow: String
  ettr: Float
  timeout: Float
  category: String
  actor: String
  request: String
  response: String
  fileSize: String
  fileName: [String]
  filePath: String
  advisory: [String]
  cve: [String]
  processInfo: [String]
  createdAt: Float
  stageOrder: Int
  tactic_and_tech(sourceSRID: String!):  [TacticWithTechniques!]
          @cypher(
            statement: """
             MATCH (n:Transaction {srid:$sourceSRID})
              WITH n
              MATCH (tact:Tactic)-[rel2:HAS]->(tech:Technique)
              WHERE rel2.sourceSRID = n.srid
              WITH tact , COLLECT(DISTINCT tech) AS techniques
              RETURN { tactic: tact, techniques: techniques }
            """
          ) 
  hasTactic: [Tactic!]! @relationship(type: "HAS_TACTIC", direction: OUT)
}
  type TacticWithTechniques {
  tactic: Tactic
  techniques: [Technique!]!
}
`
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

