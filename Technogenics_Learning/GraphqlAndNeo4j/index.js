import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';
import { Neo4jGraphQL } from "@neo4j/graphql";
import neo4j from "neo4j-driver";

// Initialize Neo4j Driver
const driver = neo4j.driver(
  'bolt://localhost:7687',
  neo4j.auth.basic('neo4j', 'saif.7117755'), // replace with your Neo4j credentials
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

// Define GraphQL schema
const typeDefs = `
 scalar GenericScalar
union ThreatLandscape = News | PatchTuesday

type Query {
  threatLandscape(limit: Int = 10, offset: Int = 0, has_cve: Boolean = false): [ThreatLandscape!]!
    @cypher(
      statement: """
      MATCH (this) WHERE (this:News OR this:PatchTuesday) AND (($has_cve AND EXISTS ((this)-->(:CVE))) OR (NOT $has_cve))
      RETURN this
      ORDER BY this.date DESC SKIP $offset LIMIT $limit
      """
    )
  threatLandscapeCount(has_cve: Boolean = false): Int
    @cypher(
      statement: """
      MATCH (this) WHERE (this:News OR this:PatchTuesday) AND (($has_cve AND EXISTS ((this)-->(:CVE))) OR (NOT $has_cve))
      RETURN COUNT(this)
      """
    )
}

type Author {
  uid: String
  srid: String
  name: String
}
type AbuseIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  abuseConfidenceScore: Int
  countryCode: String
  domain: String
  hostnames: String
  ipAddress: String
  ipVersion: Int
  isp: String
  isPublic: Boolean
  isWhitelisted: Boolean
  lastReportedAt: String
  numDistinctUsers: Int
  totalReports: Int
  usageType: String

  hasHostname: [Subdomain!]! @relationship(type: "ABUSE_IP_SUBDOMAIN", direction: OUT)
  lookupOf: [IP!]! @relationship(type: "ABUSE_IP_LOOKUP_OF", direction: OUT)
}
type Action {
  name: String
  description: String
  uid: String
  srid: String

  mitigates: [Technique!]! @relationship(type: "MITIGATES", direction: OUT)
}
type ActorAlias {
  name: String
  displayName: String
  uid: String
  srid: String
  aliasOf: [ThreatActor!]! @relationship(type: "ALIAS_OF", direction: OUT)
  relatedTo: [ThreatActor!]! @relationship(type: "RELATED_TO", direction: OUT)
}
type ActorCreated {
  name: String
  uid: String
  srid: String
  createdActor: [ThreatActor!]! @relationship(type: "CREATED_ACTOR", direction: OUT)
}
type ActorModified {
  name: String
  uid: String
  srid: String
  modifiedActor: [ThreatActor!]! @relationship(type: "MODIFIED_ACTOR", direction: OUT)
}
type Analysis {
  score: Int
  confidence: String
  verdict: String
  domainAnalysis: [Domain!]! @relationship(type: "ANALYSIS_OF", direction: OUT, properties: "_TimeProperty")
  ipAnalysis: [IP!]! @relationship(type: "ANALYSIS_OF", direction: OUT, properties: "_TimeProperty")
  urlAnalysis: [URL!]! @relationship(type: "ANALYSIS_OF", direction: OUT, properties: "_TimeProperty")
  objectAnalysis: [Object!]! @relationship(type: "ANALYSIS_OF", direction: OUT, properties: "_TimeProperty")
  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT properties: "_SourceRelProperties")
}
type Agenda {
  name: String
  displayName: String
  uid: String
  srid: String
  motivationOf: [ThreatActor!]! @relationship(type: "MOTIVATION_OF", direction: OUT)
}
type AlienVaultDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  actual_size: Int
  count: Int
  data: String
  full_size: Int
  has_next: Boolean
  limit: Int
  next: String
  paged: Boolean
  page_num: Int
  passive_dns: String
  previous: String
  size: Int
  url_list: String

  lookupOf: [Domain!]! @relationship(type: "ALIEN_VAULT_DOMAIN_LOOKUP_OF", direction: OUT)
  hasPassiveDNS: [PassiveDNS!]! @relationship(type: "ALIEN_VAULT_DOMAIN_PASSIVE_DNS", direction: OUT)
  hasUrl: [URLList!]! @relationship(type: "ALIEN_VAULT_DOMAIN_URL", direction: OUT)
}
type AlienVaultUrlLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  area_code: Int
  accuracy_radius: Int
  charset: Int
  flag_title: String
  net_loc: String
  continent_code: String
  flag_url: String
  country_code: String
  city: String
  city_data: Boolean
  country_code2: String
  dma_code: Int
  country_name: String
  country_code3: String
  longitude: Float
  latitude: Float
  url: String
  subdivision: String
  region: String
  postal_code: String

  lookupOf: [URL!]! @relationship(type: "ALIEN_VAULT_URL_LOOKUP_OF", direction: OUT)
  urlList: [URLList!]! @relationship(type: "HAS_URL", direction: OUT)
}
type AttackCampaign {
  threatActor: String
  impact: String
  malwareUsed: String
  attackCampaign: String
  displayName: String
  dateDetectedOn: String
  detectedAt: Float
  seenAt: Float
  updatedAt: Float
  createdAt: Float
  targetCountry: String
  tags: String
  srid: String
  uid: String
  attackSummary: String
  dateSeenOn: String
  detectedBy: String
  name: String
  sector: String
  trends: String
  advisory: [String]

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  tagOfCampaign: [Tag!]! @relationship(type: "TAG_OF_CAMPAIGN", direction: OUT)
  seenOfCampaign: [CampaignSeen!]! @relationship(type: "SEEN_OF_CAMPAIGN", direction: OUT)
  detectionOfCampaign: [CampaignDetected!]! @relationship(type: "DETECTION_OF_CAMPAIGN", direction: OUT)
  campaignOfTA: [ThreatActor!]! @relationship(type: "CAMPAIGN_OF", direction: OUT)
  campaignOfMA: [Malware!]! @relationship(type: "CAMPAIGN_OF", direction: OUT)
  campaignOfTOA: [Tool!]! @relationship(type: "CAMPAIGN_OF", direction: OUT)
  campaignOfRA: [Ransom!]! @relationship(type: "CAMPAIGN_OF", direction: OUT)
  campaignOfStrike: [Strike!]! @relationship(type: "CAMPAIGN_OF_STRIKE", direction: OUT)

  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT)
  authentiHashIndicator: [AuthentiHash!]! @relationship(type: "AUTHENTIHASH_INDICATOR", direction: OUT)
  impHashIndicator: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT)
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT)
  sha512Indicator: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT)
  ssDeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  vHashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  objectIndicator: [Object!]! @relationship(type: "OBJECT_INDICATOR", direction: OUT)

  targetedByCampaign: [Country!]! @relationship(type: "TARGETED_BY_CAMPAIGN", direction: OUT)
  originOfCampaign: [Country!]! @relationship(type: "ORIGIN_OF_CAMPAIGN", direction: OUT)
  toolUsedByCampaign: [Tool!]! @relationship(type: "TOOL_USED_BY_CAMPAIGN", direction: OUT)
  malUsedByCampaign: [Malware!]! @relationship(type: "MAL_USED_BY_CAMPAIGN", direction: OUT)
  sectorTargetedByCampaign: [Sector!]! @relationship(type: "SECTOR_TARGETED_BY_CAMPAIGN", direction: OUT)
  industryTargetedByCampaign: [Industry!]! @relationship(type: "INDUSTRY_TARGETED_BY_CAMPAIGN", direction: OUT)
  tacticsOfCampaign: [Tactic!]! @relationship(type: "TACTICS_USED_BY_CAMPAIGN", direction: OUT)
  techniquesOfCampaign: [Technique!]! @relationship(type: "TECHNIQUES_USED_BY_CAMPAIGN", direction: OUT)
  mitigations: [Mitigation!]! @relationship(type: "MITIGATED_BY", direction: OUT)
  refs: [Reference!]! @relationship(type: "HAS_REFERENCE", direction: OUT)
  exploitsCVE: [CVE!]! @relationship(type: "EXPLOITS_CVE", direction: OUT, properties: "_TimeProperty")
}
type AuthentiHash {
  name: String
  srid: String
  uid: String

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  indicatesRansom: [Ransom!]! @relationship(type: "AUTHENTIHASH_OF_RANSOM", direction: OUT)
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_AUTHENTIHASH", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT)
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  indicatesAttackCampaign: [AttackCampaign!]! @relationship(type: "INDICATES_ATTACK_CAMPAIGN", direction: OUT)
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT)
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT)
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT)
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT)
  ofObject: [Object!]! @relationship(type: "AUTHENTIHASH_OF_OBJECT", direction: OUT, properties: "_TimeProperty")
}
type ASN {
  uid: String
  srid: String
  name: String
  number: Int
  asn: Int
  allocatedAt: Float

  allocation_age: Int
  allocation_date: Float
  rank: Int
  rank_score: Int
  reputation: Int
  reputation_score: Int
  takedown_reputation: Int
  takedown_reputation_score: Int
  date: Float
  density: Int
  ips_in_asn: Int
  ips_num_active: Int
  ips_num_listed: Int

  createdAt: Float
  updatedAt: Float
  hasDensity: [Density!]! @relationship(type: "ASN_OF", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  ip: [IP!]! @relationship(type: "ASN_OF", direction: OUT)
}
type BreachedWebsite {
  uid: String
  srid: String
  AddedDate: String
  BreachDate: String
  DataClasses: String
  Description: String
  Domain: String
  IsFabricated: Boolean
  IsRetired: Boolean
  IsSensitive: Boolean
  IsSpamList: Boolean
  IsVerified: Boolean
  LogoPath: String
  ModifiedDate: String
  Name: String
  PwnCount: Int
  Title: String

  breachedByEmail: [Email!]! @relationship(type: "WEBSITE_BREACHED_BY", direction: OUT)
  breachedBy: [HIBPEmailLookup!]! @relationship(type: "WEBSITE_BREACHED_BY", direction: OUT)
}
type BTC {
  uid: String
  srid: String
  name: String
  btcOf: [Ransom!]! @relationship(type: "BTC_OF", direction: OUT)
}
type CAPEC {
  uid: String
  srid: String
  name: String
  displayName: String
  description: String
  likelihoodAttacks: String
  severity: String
  prerequisites: String
  example: String
  mitigations: String
  skillsRequired: String

  childOf: [CAPEC!]! @relationship(type: "CHILD_OF", direction: OUT)
  hasChildern: [CAPEC!]! @relationship(type: "HAS_CHILDREN", direction: OUT)
  canPrecede: [CAPEC!]! @relationship(type: "CAN_PRECEDE", direction: OUT)
  precedes: [CAPEC!]! @relationship(type: "PRECEDES", direction: OUT)
  peerOf: [CAPEC!]! @relationship(type: "PEER_OF", direction: OUT)
  hasPeers: [CAPEC!]! @relationship(type: "HAS_PEERS", direction: OUT)
  canAlsoBe: [CAPEC!]! @relationship(type: "CAN_ALSO_BE", direction: OUT)
  canBe: [CAPEC!]! @relationship(type: "CAN_BE", direction: OUT)
  cwes: [CWE!]! @relationship(type: "RELATED_WEAKNESS", direction: OUT)
  impacts: [CAPECImpact!]! @relationship(type: "HAS_IMPACT", direction: OUT)
  scopes: [CAPECScope!]! @relationship(type: "HAS_SCOPE", direction: OUT)
}
type CAPECImpact {
  uid: String
  srid: String
  name: String
  displayName: String

  capecs: [CAPEC!]! @relationship(type: "INCLUDES", direction: OUT)
}
type CAPECScope {
  uid: String
  srid: String
  name: String
  displayName: String

  capecs: [CAPEC!]! @relationship(type: "INCLUDES", direction: OUT)
}

type Case @exclude {
  caseID: String
  caseTitle: String
  description: String
  priority: String
  verdict: String
  severity: String
  status: String
  progress: Float
  assignee: String
  reporter: String
  alerts: [String]
  assets: [String]
  tags: [String]
  vulnerabilities: [String]
  ticket_type: String
  manualIOCs: [String]
  metadata: GenericScalar
  source: GenericScalar
  createdAt: Float
  updatedAt: Float
  assignedAt: Float
  respondAt: Float
}
type City {
  name: String
  srid: String
  uid: String
  updatedAt: Float
  createdAt: Float
  domainIndicator: [Domain!]! @relationship(type: "CITY_OF", direction: OUT)
  whoIsIndicator: [WhoIs!]! @relationship(type: "CITY_OF", direction: OUT)
  fromCountry: [Country!]! @relationship(type: "CITY_OF", direction: OUT)
}
type CVE {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float

  patchInformation: String
  patch_information: String @alias(property: "patchInformation")
  patchable: Boolean
  exploitable: Boolean
  zeroDay: Boolean
  zero_day: Boolean @alias(property: "zeroDay")
  exploitMaturity: String
  publicExposure: Boolean
  severity: String
  displayName: String
  cveState: String
  description: String
  publishedDate: String
  cweNumber: String
  cweName: String
  otherName: String
  tags: String
  refs: String
  vectorString: String
  attackVector: String
  attackComplexity: String
  privilegesRequired: String
  userInteraction: String
  scope: String
  confidentialityImpact: String
  integrityImpact: String
  availabilityImpact: String
  baseScore: String
  baseSeverity: String
  cpe: String
  recentArticles: String
  vectorString2: String
  accessVector2: String
  accessComplexity2: String
  authentication2: String
  confidentialityImpact2: String
  integrityImpact2: String
  availabilityImpact2: String
  baseScore2: String
  Severity2: String
  exploitabilityScore2: String
  impactScore2: String
  approved: Boolean
  approved_by: String
  added_on: Float
  submitted_by: String
  type: String
  source: String
  exploitabilityScore: String
  impactScore: String
  title: String
  baseScoreMicrosoft: String
  baseSeverityMicrosoft: String


  vendor: [Vendor!]! @relationship(type: "HAS_VENDOR", direction: OUT, properties: "_TimeProperty")
  product: [Product!]! @relationship(type: "EXPLOITS", direction: OUT, properties: "_TimeProperty")
  version: [Version!]! @relationship(type: "HAS_VERSION", direction: OUT, properties: "_TimeProperty")
  cwe: [CWE!]! @relationship(type: "HAS_CWE", direction: OUT, properties: "_TimeProperty")
  createdOn: [Created!]! @relationship(type: "CREATED_ON", direction: OUT, properties: "_TimeProperty")
  exploitedInStrike: [Strike!]! @relationship(type: "EXPLOITED_IN_STRIKE", direction: OUT, properties: "_TimeProperty")
  exploitedInTransaction: [Transaction!]! @relationship(type: "EXPLOITED_IN_TRANSACTION", direction: OUT, properties: "_TimeProperty")
  exploitedInCampaign: [AttackCampaign!]! @relationship(type: "EXPLOITED_IN_CAMPAIGN", direction: OUT, properties: "_TimeProperty")
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT, properties: "_TimeProperty")
  hasAlias: [CVEAlias!]! @relationship(type: "HAS_ALIAS", direction: OUT, properties: "_TimeProperty")
  ips: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ipv6s: [IPV6!]! @relationship(type: "IPV6_INDICATOR", direction: OUT, properties: "_TimeProperty")
  domains: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT, properties: "_TimeProperty")
  urls: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT, properties: "_TimeProperty")
  authentiHash: [AuthentiHash!]! @relationship(type: "AUTHENTIHASH_INDICATOR", direction: OUT, properties: "_TimeProperty")
  md5: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT, properties: "_TimeProperty")
  domain: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT, properties: "_TimeProperty")
  email: [Email!]! @relationship(type: "EMAIL_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha1: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha256: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha512: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ssDeep: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT, properties: "_TimeProperty")
  vHash: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT, properties: "_TimeProperty")
  impHash: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT, properties: "_TimeProperty")
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  hasReference: [Reference!]! @relationship(type: "HAS_REF", direction: OUT, properties: "_TimeProperty")
  hasCpe: [CPE!]! @relationship(type: "HAS_CPE", direction: OUT, properties: "_TimeProperty")
  hasOperator: [Operator!]! @relationship(type: "HAS_OPERATOR", direction: OUT, properties: "_TimeProperty")
  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_SourceRelProperties")
  fixIn: [Version!]! @relationship(type: "FIX_IN", direction: OUT, properties: "_TimeProperty")
  vulnerabilityType: [VulnerabilityType!]! @relationship(type: "HAS_THREAT", direction: OUT, properties: "_TimeProperty")
  patchTuesday: [PatchTuesday!]! @relationship(type: "REPORTED_IN", direction: OUT, properties: "_TimeProperty")
  hasAdvisory: [Advisory!]! @relationship(type: "HAS_ADVISORY", direction: OUT, properties: "_TimeProperty")
  usedByObject: [Object!]! @relationship(type: "USED_BY_OBJECT", direction: OUT, properties: "_TimeProperty")
  hasPatch: [Patch!]! @relationship(type: "HAS_PATCH", direction: OUT, properties: "_TimeProperty")
  vulnerability: [Vulnerability!]! @relationship(type: "CVE_OF", direction: OUT)
  threatActor: [ThreatActor!]! @relationship(type: "TA_INDICATOR", direction: OUT)
  malware: [Malware!]! @relationship(type: "MALWARE_INDICATOR", direction: OUT)
  ransom: [Ransom!]! @relationship(type: "RANSOM_INDICATOR", direction: OUT)
  tool: [Tool!]! @relationship(type: "TOOL_INDICATOR", direction: OUT)
  mitigations: [Mitigation!]! @relationship(type: "MITIGATION_INDICATOR", direction: OUT)
}
type CPE {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  hasCve: [CVE!]! @relationship(type: "HAS_CVE", direction: OUT, properties: "_TimeProperty")
  hasProduct: [Product!]! @relationship(type: "HAS_PRODUCT", direction: OUT, properties: "_TimeProperty")
  hasPatch: [Patch!]! @relationship(type: "HAS_PATCH", direction: OUT, properties: "_TimeProperty")
}

type CVEAlias {
  name: String
  displayName: String
  uid: String
  srid: String
  aliasOf: [CVE!]! @relationship(type: "ALIAS_OF", direction: OUT)
}
type CWE {
  uid: String
  srid: String
  name: String
  description: String
  displayName: String

  cve: [CVE!]! @relationship(type: "RELATES_CVE", direction: OUT)
  capecs: [CAPEC!]! @relationship(type: "WEAKNESS_OF", direction: OUT)
}
type CampaignDetected {
  name: String
  srid: String
  uid: String
  campaignDetection: [AttackCampaign!]! @relationship(type: "CAMPAIGN_DETECTION", direction: OUT)
}
type CampaignSeen {
  name: String
  srid: String
  uid: String
  campaignSeen: [AttackCampaign!]! @relationship(type: "CAMPAIGN_SEEN", direction: OUT)
}
type Category {
  uid: String
  srid: String
  name: String
  description: String

  ratLinksMal: [Malware!]! @relationship(type: "RAT_LINKS_MAL", direction: OUT)
  bankLinksMal: [Malware!]! @relationship(type: "BANK_LINKS_MAL", direction: OUT)
  categoryOfStrike: [Strike!]! @relationship(type: "CATEGORY_OF_STRIKE", direction: OUT)
  categoryOfTransaction: [Transaction!]! @relationship(type: "CATEGORY_OF_TRANSACTION", direction: OUT)
  categoryOfUrl: [URL!]! @relationship(type: "CATEGORY_OF_URL", direction: OUT)
  categoryOfTalosDomain: [TalosDomainLookup!]! @relationship(type: "CATEGORY_OF_TALOS_DOMAIN", direction: OUT)
  categoryOfTalosIP: [TalosIPLookup!]! @relationship(type: "CATEGORY_OF_TALOS_IP", direction: OUT)
  categoryOfTalosUrl: [TalosUrlLookup!]! @relationship(type: "CATEGORY_OF_TALOS_URL", direction: OUT)
  categoryOfStage: [Stage!]! @relationship(type: "CATEGORY_OF",direction: OUT)
  categoryOfIp: [IP!]! @relationship(type: "CATEGORY_OF",direction: OUT)
  categoryOfDomain:[Domain!]! @relationship(type: "CATEGORY_OF",direction: OUT)
  categoryOfObject:[Object!]! @relationship(type: "CATEGORY_OF",direction: OUT)
  categoryUrl:[URL!]! @relationship(type: "CATEGORY_OF",direction: OUT)
  hasSource:[Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_SourceRelProperties")
}
type CheckPhishUrlScan {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  brand: String
  disposition: String
  error: Boolean
  insights: String
  job_id: String
  resolved: Boolean
  screenshot_path: String
  status: String
  url: String
  url_sha256: String

  scanOf: [URL!]! @relationship(type: "CHECK_PHISH_URL_SCAN_OF", direction: OUT)
}
type Country {
  uid: String
  srid: String
  name: String

  countryOfWhoIs: [WhoIs!]! @relationship(type: "COUNTRY_OF", direction: OUT)
  countryHasCity: [City!]! @relationship(type: "HAS_CITY", direction: OUT)

  affectedByStrike: [Strike!]! @relationship(type: "AFFECTED_BY", direction: OUT)
  originOfStrike: [Strike!]! @relationship(type: "ORIGIN_OF", direction: OUT)
  sponsors: [ThreatActor!]! @relationship(type: "SPONSORS", direction: OUT)
  targetedBy: [ThreatActor!]! @relationship(type: "TARGETED_BY", direction: OUT)
  campaignTargets: [AttackCampaign!]! @relationship(type: "CAMPAIGN_TARGETS", direction: OUT)
  sponsorsRansom: [Ransom!]! @relationship(type: "SPONSORS_RANSOM", direction: OUT)
  sponsorsMalware: [Malware!]! @relationship(type: "SPONSORS_MALWARE", direction: OUT)
  sponsorsTool: [Tool!]! @relationship(type: "SPONSORS_TOOL", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT)
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT)
  ssDeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  vHashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  reportedByCert: [Cert!]! @relationship(type: "REPORTED_BY_CERT", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  countryOfDomain: [Domain!]! @relationship(type: "COUNTRY_OF_DOMAIN", direction: OUT)
  countryOfWhoIsDomain: [WhoIsDomainLookup!]! @relationship(type: "COUNTRY_OF_WHO_IS_DOMAIN", direction: OUT)
  campaignOrigin: [AttackCampaign!]! @relationship(type: "CAMPAIGN_ORIGIN", direction: OUT)
  objectOrigin: [Object!]! @relationship(type: "ORIGIN_COUNTRY_OF", direction: OUT)
  targetedByUrl: [URL!]! @relationship(type: "TARGETED_BY", direction: OUT)
}
type Created {
  uid: String
  srid: String
  name: String
  createdMalware: [Malware!]! @relationship(type: "CREATED_MALWARE", direction: OUT)
  createdTool: [Tool!]! @relationship(type: "CREATED_TOOL", direction: OUT)
  createdCve: [CVE!]! @relationship(type: "CREATED_CVE", direction: OUT)
}
type Decrypter {
  uid: String
  srid: String
  available: String
  name: String
  privateName: String
  publicName: String
  refs: String
  version: String
  decrypterOf: [Ransom!]! @relationship(type: "DECRYPTER_OF", direction: OUT)
}
type Density {
  uid: String
  srid: String
  name: String
  density_avg: Int
  density_max: Int
  density_stddev: Float
  ips_active: Int
  subnet_size: Float
  asn: [ASN!]! @relationship(type: "HAS_ASN", direction: OUT)
  subnet: [Subnet!]! @relationship(type: "DENSITY_OF", direction: OUT)
}
type Definition {
  name: String
  uid: String
  description: String
  displayName: String
  srid: String
}
type DisposableDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  is_disposable: Boolean

  lookupOf: [Domain!]! @relationship(type: "DISPOSABLE_DOMAIN_LOOKUP_OF", direction: OUT)
}
type DNSAddress {
  uid: String
  srid: String
  name: String

  addressOf: [PassiveDNS!]! @relationship(type: "ADDRESS_OF_PASSIVE_DNS", direction: OUT)
}

interface _TimeProperty @relationshipProperties {
  createdAt: Float
  updatedAt: Float
}

interface _ReverseDnsTimeProperty @relationshipProperties {
  time: Float
}
interface _DnsSeenTime @relationshipProperties{
  seen_time: Float
}
type Domain {
  name: String
  uid: String
  srid: String
  updatedAt: Float
  createdAt: Float
  score: Int
  confidence: String
  firstSeen: Float
  lastSeen: Float
  verdict: String
  approved: Boolean
  fp: Boolean

  hasNameserver: [Nameserver!]! @relationship(type: "HAS_NAMESERVER", direction: OUT)
  hasCertificate: [DomainCertificate!]! @relationship(type: "DOMAIN_HAS_CERTIFICATE", direction: OUT)
  hasWhoIs: [WhoIs!]! @relationship(type: "HAS_WHOIS", direction: OUT)
  fromCity: [City!]! @relationship(type: "FROM_CITY", direction: OUT)
  hasCousins: [Domain!]! @relationship(type: "HAS_COUSIN_DOMAIN", direction: OUT)
  cousinsOf: [Domain!]! @relationship(type: "COUSIN_DOMAIN_OF", direction: OUT)
  hasSiblings: [Domain!]! @relationship(type: "HAS_SIBLING_DOMAIN", direction: OUT)
  siblingsOf: [Domain!]! @relationship(type: "SIBLING_DOMAIN_OF", direction: OUT)
  tld: [TLD!]! @relationship(type: "HAS_TLD",direction: OUT)
  domainRep: [DomainReputation!]! @relationship(type: "HAS_REPUTATION",direction: OUT)
  dga: [DomainGenerationAlgorithm!]! @relationship(type: "DGA_INFO",direction: OUT)
  resolvingIp: [IP!]! @relationship(type: "RESOLVING_IP", direction: OUT)
  mxInfo: [MailExchange!]! @relationship(type: "INDICATE_MX", direction: OUT)
  domainOfIp: [IP!]! @relationship(type: "DOMAIN_OF_IP",direction: OUT)

  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_SourceRelProperties")
  mitigatedBy: [Mitigation!]! @relationship(type: "MITIGATED_BY", direction: OUT, properties: "_TimeProperty")
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT)
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT, properties: "_TimeProperty")
  domainOfRansom: [Ransom!]! @relationship(type: "DOMAIN_OF_RANSOM", direction: OUT, properties: "_TimeProperty")
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT, properties: "_TimeProperty")
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT, properties: "_TimeProperty")
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT, properties: "_TimeProperty")
  hasVulnerability: [Vulnerability!]! @relationship(type: "HAS_VULNERABILITY", direction: OUT)
  hasIpHost: [IP!]! @relationship(type: "HAS_HOST", direction: OUT)
  hasDomainHost: [Domain!]! @relationship(type: "HAS_HOST", direction: OUT)
  ipHostOf: [IP!]! @relationship(type: "HOST_OF", direction: OUT)
  domainHostOf: [Domain!]! @relationship(type: "HOST_OF", direction: OUT)
  urlHostOf: [URL!]! @relationship(type: "HOST_OF", direction: OUT)
  objectHostOf: [Object!]! @relationship(type: "HOST_OF", direction: OUT)
  contactedObject : [Object!]! @relationship(type: "COMMUNICATED_BY", direction: OUT)
  downloadedFromHost: [Object!]! @relationship(type: "DOWNLOADS_OBJECT", direction: OUT)
  hasTactic : [Tactic!]! @relationship(type: "HAS_TACTIC", direction: OUT)
  hasTechnique : [Technique!]! @relationship(type: "HAS_TECHNIQUE", direction: OUT)
  hasSubTechnique : [Technique!]! @relationship(type: "HAS_SUB_TECHNIQUE", direction: OUT)

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  communicatedByObject: [Object!]! @relationship(type: "COMMUNICATED_BY_OBJECT", direction: OUT)
  downloadsObject: [Object!]! @relationship(type: "DOWNLOADS_OBJECT", direction: OUT)
  hasSubdomain: [Subdomain!]! @relationship(type: "HAS_SUBDOMAIN", direction: OUT)
  hasPassiveDNS: [PassiveDNS!]! @relationship(type: "HAS_PASSIVE_DNS", direction: OUT)
  nameServerPassiveDNS: [Nameserver!]! @relationship(type: "HAS_PASSIVE_DNS", direction: OUT, properties: "_DnsSeenTime")
  ipPassiveDns: [IP!]! @relationship(type: "HAS_PASSIVE_DNS_IP",direction: OUT, properties: "_DnsSeenTime")
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  hasAddress: [Address!]! @relationship(type: "HAS_ADDRESS", direction: OUT)
  hasDNSSEC: [DNSSEC!]! @relationship(type: "HAS_DNSSEC", direction: OUT)
  hasRegistrar: [Registrar!]! @relationship(type: "HAS_REGISTRAR", direction: OUT)
  indicatesEmail: [Email!]! @relationship(type: "INDICATES_EMAIL", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT)
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT)
  ssDeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  vHashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_DOMAIN", direction: OUT)
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
  indicatesCountry: [Country!]! @relationship(type: "INDICATES_COUNTRY", direction: OUT)
  resolutionOf: [IP!]! @relationship(type: "RESOLUTION_OF", direction: OUT)
  hasResolution: [IP!]! @relationship(type: "HAS_RESOLUTION", direction: OUT)
  fromCountry: [Country!]! @relationship(type: "FROM_COUNTRY", direction: OUT)
  domainOfUrl: [URL!]! @relationship(type: "DOMAIN_OF_URL", direction: OUT)
  reverseDnsWhoIs: [WhoIs!]! @relationship(type: "REVERSE_DNS_OF", direction: OUT)
  reverseDnsIp: [IP!]! @relationship(type: "REVERSE_DNS_OF", direction: OUT, properties: "_ReverseDnsTimeProperty")
  whoIsDomain: [WhoIs!]! @relationship(type: "DOMAIN_OF", direction: OUT)
  hasAnalysis: [Analysis!]! @relationship(type: "HAS_ANALYSIS", direction: OUT, properties: "_TimeProperty")
  hasPort: [Port!]! @relationship(type: "HAS_PORT", direction: OUT, properties: "_PortType")
  domainCategory: [Category!]! @relationship(type: "HAS_CATEGORY",direction: OUT)

  alienVaultDomainLookUp: [AlienVaultDomainLookup!]! @relationship(type: "ALIEN_VAULT_DOMAIN_LOOKUP", direction: OUT)
  disposableDomainLookup: [DisposableDomainLookup!]! @relationship(type: "DISPOSABLE_DOMAIN_LOOKUP", direction: OUT)
  domainResolutionLookup: [DomainResolution!]! @relationship(type: "DOMAIN_RESOLUTION_LOOKUP", direction: OUT)
  domainStatus: [DomainStatus!]! @relationship(type: "DOMAIN_STATUS", direction: OUT)
  opswatDomainLookup: [OPSWATDomainLookup!]! @relationship(type: "OPSWAT_DOMAIN_LOOKUP", direction: OUT)
  talosDomainLookup: [TalosDomainLookup!]! @relationship(type: "TALOS_DOMAIN_LOOKUP", direction: OUT)
  threatCrowdDomainLookup: [ThreatCrowdDomainLookup!]! @relationship(type: "THREAT_CROWD_DOMAIN_LOOKUP", direction: OUT)
  threatMinerDomainLookup: [ThreatMinerDomainLookup!]! @relationship(type: "THREAT_MINER_DOMAIN_LOOKUP", direction: OUT)
  urlHausDomainLookup: [URLHausDomainLookup!]! @relationship(type: "URL_HAUS_DOMAIN_LOOKUP", direction: OUT)
  whoIsDomainLookup: [WhoIsDomainLookup!]! @relationship(type: "WHO_IS_DOMAIN_LOOKUP", direction: OUT)
  virusTotalDomainLookup: [VirusTotalDomainLookup!]! @relationship(type: "VIRUS_TOTAL_DOMAIN_LOOKUP", direction: OUT)
  partOfthreatMinerIPPassiveDNS: [PassiveDNS!]! @relationship(type: "PART_OF_THREAT_MINER_IP_PASSIVE_DNS", direction: OUT)
  domainOfthreatCrowdMD5: [ThreatCrowdMD5Lookup!]! @relationship(type: "DOMAIN_OF_THREAT_CROWD_MD5", direction: OUT)
  domainOfTalosUrl: [TalosUrlLookup!]! @relationship(type: "DOMAIN_OF_TALOS_URL", direction: OUT)
  domainOfTalosIP: [TalosIPLookup!]! @relationship(type: "DOMAIN_OF_TALOS_IP", direction: OUT)
  domainOfShodanIP: [ShodanIPLookup!]! @relationship(type: "DOMAIN_OF_SHODAN_IP", direction: OUT)
  domainOfHybridAnalysisMD5: [HybridAnalysisMD5Lookup!]! @relationship(type: "DOMAIN_OF_HYBRID_ANALYSIS_MD5", direction: OUT)
  domainOfHybridAnalysisSHA1: [HybridAnalysisSHA1Lookup!]! @relationship(type: "DOMAIN_OF_HYBRID_ANALYSIS_SHA1", direction: OUT)
  domainOfHybridAnalysisSHA256: [HybridAnalysisSHA256Lookup!]! @relationship(type: "DOMAIN_OF_HYBRID_ANALYSIS_SHA256", direction: OUT)
  zScalerDomainLookup: [ZScalerDomainLookup!]! @relationship(type: "Z_SCALER_DOMAIN_LOOKUP", direction: OUT)
}
type DomainCertificate {
  cert_index: Int
  chain: String
  createdAt: Float
  date: Int
  fingerprint: String
  issuer: String
  not_after: Float
  not_before: Float
  source_name: String
  source_url: String
  srid: String
  subject: String
  uid: String
  updatedAt: Float
  host_name: String
  common_name: String
  san: [String]
  certificate_authority: String
  cert_as_text: String
  revoked_status: String
  hasHostname: [Hostname!]! @relationship(type: "DOMAIN_CERTIFICATE_HAS_HOSTNAME", direction: OUT)
  hasSha256: [SHA256!]! @relationship(type: "HAS_SHA256_FINGERPRINT", direction: OUT)
  hasSha1: [SHA1!]! @relationship(type: "HAS_SHA1_FINGERPRINT", direction: OUT)
  hasMd5: [MD5!]! @relationship(type: "HAS_MD5_FINGERPRINT", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "CERTIFICATE_OF_DOMAIN", direction: OUT)
}
type DomainGenerationAlgorithm{
  avg_probability: String
  dga_probability_score: String
  domain_string_freq_probability: String
  domain: [Domain!]! @relationship(type: "DGA_OF",direction: OUT)
}
type Address {
  uid: String
  srid: String
  name: String

  addressOfDomain: [Domain!]! @relationship(type: "ADDRESS_OF_DOMAIN", direction: OUT)

  addressOfWhoIsDomain: [WhoIsDomainLookup!]! @relationship(type: "ADDRESS_OF_WHO_IS_DOMAIN", direction: OUT)
}
type DNSSEC {
  uid: String
  srid: String
  name: String

  dnssecOfDomain: [Domain!]! @relationship(type: "DNSSEC_DOMAIN", direction: OUT)
  dnssecOfWhoIsDomain: [WhoIsDomainLookup!]! @relationship(type: "DNSSEC_OF_WHO_IS_DOMAIN", direction: OUT)
}
type Registrar {
  uid: String
  srid: String
  name: String
  who_is_server: String
  status: String
  IANA_id: String

  registrarDomain: [Domain!]! @relationship(type: "REGISTRAR_OF_DOMAIN", direction: OUT)
  registrarOfWhoIsDomain: [WhoIsDomainLookup!]! @relationship(type: "REGISTRAR_OF_WHO_IS_DOMAIN", direction: OUT)
  registrarOfWhoIs: [WhoIs!]! @relationship(type: "REGISTRAR_OF", direction: OUT)
  location: [Location!]! @relationship(type: "HAS_LOCATION", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "HAS_URL", direction: OUT)
}
type DomainReputation {
  cisco_umbrella_rank: Int
  mm_rank: Int
  sr_rank: Int
  domainRep: [Domain!]! @relationship(type: "REPUTATION_OF",direction: OUT)
}
type DomainResolution {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  alias_list: String
  primary_hostname: String
  resolutions: String

  domainResolutionLookupOf: [Domain!]! @relationship(type: "DOMAIN_RESOLUTION_LOOKUP_OF", direction: OUT)
  domainResolution: [Resolution!]! @relationship(type: "DOMAIN_RESOLUTION", direction: OUT)
}
type DomainStatus {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  response_headers: String
  status_code: Int
  final_url: String
  response_history: String

  statusOf: [Domain!]! @relationship(type: "STATUS_OF_DOMAIN", direction: OUT)
}
type Email {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  score: Int
  confidence: String
  firstSeen: Float
  lastSeen: Float
  verdict: String
  approved: Boolean
  fp: Boolean
  whoIsIndicator: [WhoIs!]! @relationship(type: "EMAIL_OF", direction: OUT)

  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_TimeProperty")
  mitigatedBy: [Mitigation!]! @relationship(type: "MITIGATED_BY", direction: OUT, properties: "_TimeProperty")
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  emailOfRansom: [Ransom!]! @relationship(type: "EMAIL_OF_RANSOM", direction: OUT, properties: "_TimeProperty")
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT, properties: "_TimeProperty")
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT, properties: "_TimeProperty")

  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  deliversObject: [Object!]! @relationship(type: "DELIVERS_OBJECT", direction: OUT)
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT, properties: "_TimeProperty")
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT)
  breachedWebsite: [BreachedWebsite!]! @relationship(type: "BREACHED_WEBSITE", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT, properties: "_TimeProperty")

  emailOfThreatCrowdDomain: [ThreatCrowdDomainLookup!]! @relationship(type: "EMAIL_OF_THREAT_CROWD_DOMAIN", direction: OUT)
  emailRepCheck: [EmailRepCheck!]! @relationship(type: "EMAIL_REP_CHECK", direction: OUT)
  hibpEmailLookup: [HIBPEmailLookup!]! @relationship(type: "HIBP_EMAIL_LOOKUP", direction: OUT)
}
type EmailRepCheck {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  references: Int
  company_logo: String
  reputation: String
  details: String
  suspicious: Boolean
  logos: String
  email: String
  explainer: String

  repOf: [Email!]! @relationship(type: "EMAIL_REP_CHECK_OF", direction: OUT)
}
type FileType {
  name: String
  uid: String
  srid: String
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
}
type FileName {
  name: String
  uid: String
  srid: String
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_FILENAME", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  exploitedByMalware: [Malware!]! @relationship(type: "EXPLOITED_BY_MALWARE", direction: OUT)
  exploitedByTool: [Tool!]! @relationship(type: "EXPLOITED_BY_TOOL", direction: OUT)
  usedBy: [ThreatActor!]! @relationship(type: "USED_BY", direction: OUT)
  mitigatedBy: [Mitigation!]! @relationship(type: "MITIGATED_BY", direction: OUT)
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
}
type GSBUrlLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  matches: String

  lookupOf: [URL!]! @relationship(type: "GSB_URL_LOOKUP_OF", direction: OUT)
}
type Hardware {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  hasProduct: [Product!]! @relationship(type: "HAS_PRODUCT", direction: OUT, properties: "_TimeProperty")
}
type HIBPEmailLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  results: String

  lookupOf: [Email!]! @relationship(type: "HIBP_EMAIL_LOOKUP_OF", direction: OUT)
  breachedWebsite: [BreachedWebsite!]! @relationship(type: "WEBSITE_BREACHED", direction: OUT)
}
type HoneyDBIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  as_name: String
  as_num: Int
  city: String
  country_iso: String
  country_name: String
  ip: String
  ip_hex: String
  ip_version: Int
  latitude: Float
  longitude: Float
  network: String
  network_broadcast: String
  network_hostmask: String
  network_netmask: String
  network_size: Int
  postal_code: String
  region_iso: String
  region_name: String

  lookupOf: [IP!]! @relationship(type: "HONEYDB_IP_LOOKUP_OF", direction: OUT)
}
type Hostname {
  uid: String
  srid: String
  name: String

  domainCertificateIndicator: [DomainCertificate!]! @relationship(type: "HOSTNAME_OF_DOMAIN_CERTIFICATE", direction: OUT)

  hostnameOfAbuseIP: [AbuseIPLookup!]! @relationship(type: "HOSTNAME_OF_ABUSE_IP", direction: OUT)
  hostnameOfShodanIP: [ShodanIPLookup!]! @relationship(type: "HOSTNAME_OF_SHODAN_IP", direction: OUT)
}
type HttpResponse {
  uid: String
  srid: String
  status_code: Int
  response_len: Int
  content_type: String
  filename: String
  url: [URL!]! @relationship(type: "RESPONSE_OF", direction: OUT)
}
type HybridAnalysisMD5Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  analysis_start_time: String
  av_detect: Int
  certificates: String
  classification_tags: String
  compromised_hosts: String
  domains: String
  environment_description: String
  extracted_files: String
  hosts: String
  interesting: Boolean
  md5: String
  mitre_attcks: String
  processes: String
  sha1: String
  sha256: String
  sha512: String
  size: Int
  state: String
  submissions: String
  submit_name: String
  tags: String
  threat_level: Int
  total_network_connections: Int
  total_processes: Int
  total_signatures: Int
  type: String
  type_short: String
  url_analysis: Boolean
  verdict: String
  vx_family: String

  hasDomain: [Domain!]! @relationship(type: "HAS_DOMAIN", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  lookupOf: [MD5!]! @relationship(type: "HYBRID_ANALYSIS_MD5_LOOKUP_OF", direction: OUT)
  hasSha1: [SHA1!]! @relationship(type: "HAS_SHA1", direction: OUT)
  hasSha256: [SHA256!]! @relationship(type: "HAS_SHA256", direction: OUT)
  hasSha512: [SHA512!]! @relationship(type: "HAS_SHA512", direction: OUT)
}
type HybridAnalysisSHA1Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  analysis_start_time: String
  av_detect: Int
  certificates: String
  classification_tags: String
  compromised_hosts: String
  domains: String
  environment_description: String
  extracted_files: String
  hosts: String
  interesting: Boolean
  md5: String
  mitre_attcks: String
  processes: String
  sha1: String
  sha256: String
  sha512: String
  size: Int
  state: String
  submissions: String
  submit_name: String
  tags: String
  threat_level: Int
  total_network_connections: Int
  total_processes: Int
  total_signatures: Int
  type: String
  type_short: String
  url_analysis: Boolean
  verdict: String
  vx_family: String

  hasDomain: [Domain!]! @relationship(type: "HAS_DOMAIN", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  lookupOf: [SHA1!]! @relationship(type: "HYBRID_ANALYSIS_SHA1_LOOKUP_OF", direction: OUT)
  hasMd5: [MD5!]! @relationship(type: "HAS_MD5", direction: OUT)
  hasSha256: [SHA256!]! @relationship(type: "HAS_SHA256", direction: OUT)
  hasSha512: [SHA512!]! @relationship(type: "HAS_SHA512", direction: OUT)
}
type HybridAnalysisSHA256Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  analysis_start_time: String
  av_detect: Int
  certificates: String
  classification_tags: String
  domains: String
  compromised_hosts: String
  environment_description: String
  extracted_files: String
  hosts: String
  interesting: Boolean
  md5: String
  mitre_attcks: String
  processes: String
  sha1: String
  sha256: String
  sha512: String
  size: Int
  state: String
  submissions: String
  submit_name: String
  tags: String
  threat_level: Int
  total_network_connections: Int
  total_processes: Int
  total_signatures: Int
  type: String
  type_short: String
  url_analysis: Boolean
  verdict: String
  vx_family: String

  hasDomain: [Domain!]! @relationship(type: "HAS_DOMAIN", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  lookupOf: [SHA256!]! @relationship(type: "HYBRID_ANALYSIS_SHA256_LOOKUP_OF", direction: OUT)
  hasMd5: [MD5!]! @relationship(type: "HAS_MD5", direction: OUT)
  hasSha1: [SHA1!]! @relationship(type: "HAS_SHA1", direction: OUT)
  hasSha512: [SHA512!]! @relationship(type: "HAS_SHA512", direction: OUT)
}
type IBMXForceIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  dns: String
  malware: String
  report: String

  lookupOf: [IP!]! @relationship(type: "IBM_XFORCE_IP_LOOKUP_OF", direction: OUT)
  passiveDNS: [PassiveDNS!]! @relationship(type: "HAS_PASSIVE_DNS", direction: OUT)
}
type IBMXForceMD5Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  malware: String
  tags: String

  lookupOf: [MD5!]! @relationship(type: "IBM_XFORCE_MD5_LOOKUP_OF", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
}
type IBMXForceSHA1Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  malware: String

  lookupOf: [SHA1!]! @relationship(type: "IBM_XFORCE_SHA1_LOOKUP_OF", direction: OUT)
  tags: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
}
type IBMXForceSHA256Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  malware: String

  lookupOf: [SHA256!]! @relationship(type: "IBM_XFORCE_SHA256_LOOKUP_OF", direction: OUT)
  tags: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
}
type IBMXForceURLLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  dns: String
  malware: String
  report: String
  whois: String

  lookupOf: [URL!]! @relationship(type: "IBM_XFORCE_URL_LOOKUP_OF", direction: OUT)
  hasPassiveDNS: [PassiveDNS!]! @relationship(type: "HAS_PASSIVE_DNS", direction: OUT)
}
type ImpHash {
  name: String
  srid: String
  uid: String

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  indicatesRansom: [Ransom!]! @relationship(type: "IMPHASH_OF_RANSOM", direction: OUT)
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_IMPHASH", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT)
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT)
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT)
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT)
  indicatesAttackCampaign: [AttackCampaign!]! @relationship(type: "INDICATES_ATTACK_CAMPAIGN", direction: OUT)
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT)
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  ofObject: [Object!]! @relationship(type: "IMPHASH_OF_OBJECT", direction: OUT, properties: "_TimeProperty")
}
type IndicatorOfAction {
  uid: String
  srid: String
  name: String
  displayName: String
  value: [String]
  type: String

  ipIndicator: [IP!]! @relationship(type: "INDICATES_IP", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "INDICATES_DOMAIN", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "INDICATES_URL", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "INDICATES_MD5", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "INDICATES_SHA1", direction: OUT)
  sha256Indicator: [SHA256!]! @relationship(type: "INDICATES_SHA256", direction: OUT)
  ssdeepIndicator: [SSDeep!]! @relationship(type: "INDICATES_SSDEEP", direction: OUT)
  authentihashIndicator: [AuthentiHash!]! @relationship(type: "INDICATES_AUTHENTIHASH", direction: OUT)
  imphashIndicator: [ImpHash!]! @relationship(type: "INDICATES_IMPHASH", direction: OUT)
  vhashIndicator: [VHash!]! @relationship(type: "INDICATES_VHASH", direction: OUT)
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT)
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT)
  indicaesRansom: [Ransom!]! @relationship(type: "INDICATES_RANSOM", direction: OUT)
  attackCampaigns: [AttackCampaign!]! @relationship(type: "INDICATES_CAMPAIGN", direction: OUT)
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT)
}
type Industry {
  uid: String
  srid: String
  name: String
  displayName: String
  hasAlias: [IndustryAlias!]! @relationship(type: "HAS_ALIAS", direction: OUT)
  targetedByStrike: [Strike!]! @relationship(type: "TARGETED_BY", direction: OUT)
  targetedByActor: [ThreatActor!]! @relationship(type: "TARGETED_BY_ACTOR", direction: OUT)
  targetedByCampaign: [AttackCampaign!]! @relationship(type: "TARGETED_BY_CAMPAIGN", direction: OUT)
  targetedByUrl: [URL!]! @relationship(type: "TARGETED_BY", direction: OUT)
}
type IndustryAlias {
  uid: String
  srid: String
  name: String
  displayName: String
  aliasOf: [Industry!]! @relationship(type: "ALIAS_OF", direction: OUT)
}
type IP {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  score: Int
  confidence: String
  firstSeen: Float
  lastSeen: Float
  status: String
  asn: String
  asn_cidr: String
  asn_country_code: String
  asn_date: String
  asn_description: String
  asn_registry: String
  nets: [String]
  nir: String
  query: String
  raw: String
  raw_referral: String
  referral: String
  type: String
  class: String
  verdict: String
  approved: Boolean
  fp: Boolean

  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_SourceRelProperties")
  hasStatus: [Status!]! @relationship(type: "HAS_STATUS", direction: OUT, properties: "_StatusRelProperties")
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT, properties: "_TimeProperty")
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  exploitedByTool: [Tool!]! @relationship(type: "EXPLOITED_BY_TOOL", direction: OUT, properties: "_TimeProperty")
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT, properties: "_TimeProperty")
  reverseDns: [Domain!]! @relationship(type: "HAS_REVERSE_DNS", direction: OUT, properties: "_ReverseDnsTimeProperty")
  hasVulnerability: [Vulnerability!]! @relationship(type: "HAS_VULNERABILITY", direction: OUT)
  hasAnalysis: [Analysis!]! @relationship(type: "HAS_ANALYSIS", direction: OUT, properties: "_TimeProperty")
  hasLocation: [Location!]! @relationship(type: "HAS_LOCATION", direction: OUT)
  hasWhoIs: [WhoIs!]! @relationship(type: "HAS_WHOIS", direction: OUT)
  resolvedByDomain: [Domain!]! @relationship(type: "RESOLVED_BY", direction: OUT)
  ipMx:[MailExchange!]! @relationship(type: "IP_OF",direction: OUT)
  hasAsn: [ASN!]! @relationship(type: "HAS_ASN",direction: OUT)

  mitigatedBy: [Mitigation!]! @relationship(type: "MITIGATED_BY", direction: OUT, properties: "_TimeProperty")
  indicatesRansom: [Ransom!]! @relationship(type: "INDICATES_RANSOM", direction: OUT, properties: "_TimeProperty")
  usedBy: [ThreatActor!]! @relationship(type: "USED_BY", direction: OUT, properties: "_TimeProperty")
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT)
  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT)
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT)
  ssDeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  vHashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  communicatedByObject: [Object!]! @relationship(type: "COMMUNICATED_BY_OBJECT", direction: OUT)
  downloadsObject: [Object!]! @relationship(type: "DOWNLOADS_OBJECT", direction: OUT)
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_IP", direction: OUT)
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
  indicatesCountry: [Country!]! @relationship(type: "INDICATES_COUNTRY", direction: OUT)
  indicatesEmail: [Email!]! @relationship(type: "INDICATES_EMAIL", direction: OUT)
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  resolutionOf: [Domain!]! @relationship(type: "RESOLUTION_OF", direction: OUT)
  hasResolution: [Domain!]! @relationship(type: "HAS_RESOLUTION", direction: OUT)
  hasHostname: [Subdomain!]! @relationship(type: "HAS_HOSTNAME", direction: OUT)
  hasPassiveDNS: [PassiveDNS!]! @relationship(type: "HAS_PASSIVE_DNS", direction: OUT)
  subnet: [Subnet!]! @relationship(type: "HAS_SUBNET", direction: OUT, properties: "_SubnetRelProperties")
  hasPort: [Port!]! @relationship(type: "HAS_PORT", direction: OUT, properties: "_PortType")
  hasIpHost: [IP!]! @relationship(type: "HAS_HOST", direction: OUT)
  hasDomainHost: [Domain!]! @relationship(type: "HAS_HOST", direction: OUT)
  ipHostOf: [IP!]! @relationship(type: "HOST_OF", direction: OUT)
  domainHostOf: [Domain!]! @relationship(type: "HOST_OF", direction: OUT)
  urlHostOf: [URL!]! @relationship(type: "HOST_OF", direction: OUT)
  objectHostOf: [Object!]! @relationship(type: "HOST_OF", direction: OUT)
  contactedObject : [Object!]! @relationship(type: "COMMUNICATED_BY", direction: OUT)
  downloadedFromHost: [Object!]! @relationship(type: "DOWNLOADS_OBJECT", direction: OUT)
  hasTactic : [Tactic!]! @relationship(type: "HAS_TACTIC", direction: OUT)
  hasTechnique : [Technique!]! @relationship(type: "HAS_TECHNIQUE", direction: OUT)
  hasSubTechnique : [Technique!]! @relationship(type: "HAS_SUB_TECHNIQUE", direction: OUT)
  ipCategory: [Category!]! @relationship(type: "HAS_CATEGORY",direction: OUT)
  domainPassiveDns: [Domain!]! @relationship(type: "PASSIVE_DNS_OF",direction: OUT, properties: "_DnsSeenTime")

  abuseIPLookup: [AbuseIPLookup!]! @relationship(type: "ABUSE_IP_LOOKUP", direction: OUT)
  honeyDBIPLookup: [HoneyDBIPLookup!]! @relationship(type: "HONEYDB_IP_LOOKUP", direction: OUT)
  ibmXForceIPLookup: [IBMXForceIPLookup!]! @relationship(type: "IBM_XFORCE_IP_LOOKUP", direction: OUT)
  ipStackGeolocationLookup: [IPStackGeolocationLookup!]! @relationship(type: "IP_STACK_GEOLOCATION_LOOKUP", direction: OUT)
  opswatIPLookup: [OPSWATIPLookup!]! @relationship(type: "OPSWAT_IP_LOOKUP", direction: OUT)
  ping: [PingIP!]! @relationship(type: "PING", direction: OUT)
  shodanIPLookup: [ShodanIPLookup!]! @relationship(type: "SHODAN_IP_LOOKUP", direction: OUT)
  talosIPLookup: [TalosIPLookup!]! @relationship(type: "TALOS_IP_LOOKUP", direction: OUT)
  threatCrowdIPLookup: [ThreatCrowdIPLookup!]! @relationship(type: "THREAT_CROWD_IP_LOOKUP", direction: OUT)
  threatMinerIPLookup: [ThreatMinerIPLookup!]! @relationship(type: "THREAT_MINER_IP_LOOKUP", direction: OUT)
  torNodeIPLookup: [TorNodeIPLookup!]! @relationship(type: "TOR_NODE_IP_LOOKUP", direction: OUT)
  virusTotalIPLookup: [VirusTotalIPLookup!]! @relationship(type: "VIRUS_TOTAL_IP_LOOKUP", direction: OUT)
  whoIsIPLookup: [WhoIsIPLookup!]! @relationship(type: "WHO_IS_IP_LOOKUP", direction: OUT)
  zScalerIPLookup: [ZScalerIPLookup!]! @relationship(type: "Z_SCALER_IP_LOOKUP", direction: OUT)
  domainResolution: [DomainResolution!]! @relationship(type: "RESOLVED_DOMAIN", direction: OUT)
  ipOfthreatCrowdMD5: [ThreatCrowdMD5Lookup!]! @relationship(type: "IP_OF_THREAT_CROWD_MD5", direction: OUT)
  aRecordOf: [IBMXForceURLLookup!]! @relationship(type: "A_RECORD_OF_IBM_XFORCE_URL", direction: OUT)
}
type IPV6 {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  score: Int
  confidence: String
  firstSeen: Float
  lastSeen: Float
  status: String

  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_TimeProperty")
  hasStatus: [Status!]! @relationship(type: "HAS_STATUS", direction: OUT, properties: "_StatusRelProperties")
  mitigatedBy: [Mitigation!]! @relationship(type: "MITIGATED_BY", direction: OUT, properties: "_TimeProperty")
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT, properties: "_TimeProperty")
  indicatesRansom: [Ransom!]! @relationship(type: "INDICATES_RANSOM", direction: OUT, properties: "_TimeProperty")
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  usedBy: [ThreatActor!]! @relationship(type: "USED_BY", direction: OUT, properties: "_TimeProperty")
  exploitedByTool: [Tool!]! @relationship(type: "EXPLOITED_BY_TOOL", direction: OUT, properties: "_TimeProperty")
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT, properties: "_TimeProperty")
}
type IPStackGeolocationLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  city: String
  continent_code: String
  continent_name: String
  country_code: String
  country_name: String
  ip: String
  latitude: Float
  location: String
  longitude: Float
  region_code: String
  region_name: String
  type: String
  zip: String

  lookupOf: [IP!]! @relationship(type: "IP_STACK_GEOLOCATION_LOOKUP_OF", direction: OUT)
}
type Location {
  continent_code: String
  continent_name: String
  country_code: String
  country_name: String
  country_is_in_european_union: Boolean
  city: String
  region:String
  region_code: String
  country_code_iso3: String
  country_capital: String
  country_tld: String
  postal: String
  latitude: Float
  longitude: Float
  timezone: String
  utc_offset: String
  country_calling_code: String
  currency: String
  currency_name: String
  languages: [String]
  country_area: Int
  country_population: Int
  hasCountry : [Country!]! @relationship(type: "HAS_COUNTRY", direction: OUT)
  hasCity : [City!]! @relationship(type: "HAS_CITY", direction: OUT)
  ip: [IP!]! @relationship(type: "LOCATION_OF", direction: OUT)
  domain: [Domain!]! @relationship(type: "LOCATION_OF", direction: OUT)
  object: [Object!]! @relationship(type: "LOCATION_OF", direction: OUT)
  url: [URL!]! @relationship(type: "LOCATION_OF", direction: OUT)
  registrar:[Registrar!]! @relationship(type: "LOCATION_OF", direction: OUT)

}
type MAC {
  uid: String
  srid: String
  name: String
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
}
type MailExchange {
  name: String
  uid: String
  srid: String
  priority_number: Int
  domain: [Domain!]! @relationship(type: "INDICATED_DOMAIN", direction: OUT)
  ip:[IP!]! @relationship(type: "HAS_IP",direction: OUT)
}
type MD5 {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  score: Int
  confidence: String
  firstSeen: Float
  lastSeen: Float
  fp: Boolean

  fingerprintDomainCertificate: [DomainCertificate!]! @relationship(type: "MD5_FINGERPRINT_OF_DOMAIN_CERTIFICATE", direction: OUT)

  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_TimeProperty")
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  ofObject: [Object!]! @relationship(type: "MD5_OF_OBJECT", direction: OUT, properties: "_TimeProperty")

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT, properties: "_TimeProperty")
  indicatesAttackCampaign: [AttackCampaign!]! @relationship(type: "INDICATES_ATTACK_CAMPAIGN", direction: OUT)
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT, properties: "_TimeProperty")
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT, properties: "_TimeProperty")
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT, properties: "_TimeProperty")
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATES_TRANSACTION", direction: OUT)
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
  md5OfRansom: [Ransom!]! @relationship(type: "MD5_OF_RANSOM", direction: OUT, properties: "_TimeProperty")
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT, properties: "_TimeProperty")

  hybridAnalysisMD5Lookup: [HybridAnalysisMD5Lookup!]! @relationship(type: "HYBRID_ANALYSIS_MD5_LOOKUP", direction: OUT)
  ibmXForceMD5Lookup: [IBMXForceMD5Lookup!]! @relationship(type: "IBM_XFORCE_MD5_LOOKUP", direction: OUT)
  opswatMD5Lookup: [OPSWATMD5Lookup!]! @relationship(type: "OPSWAT_MD5_LOOKUP", direction: OUT)
  threatCrowdMD5Lookup: [ThreatCrowdMD5Lookup!]! @relationship(type: "THREAT_CROWD_MD5_LOOKUP", direction: OUT)
  urlHausMD5Lookup: [URLHausMD5Lookup!]! @relationship(type: "URL_HAUS_MD5_LOOKUP", direction: OUT)
  virusTotalMD5Lookup: [VirusTotalMD5Lookup!]! @relationship(type: "VIRUS_TOTAL_MD5_LOOKUP", direction: OUT)
  md5OfThreatCrowdIP: [ThreatCrowdIPLookup!]! @relationship(type: "MD5_OF_THREAT_CROWD_IP", direction: OUT)
  md5OfThreatCrowdDomain: [ThreatCrowdDomainLookup!]! @relationship(type: "MD5_OF_THREAT_CROWD_DOMAIN", direction: OUT)

  partOfHybridAnalysisSHA1: [HybridAnalysisSHA1Lookup!]! @relationship(type: "PART_OF_HYBRID_ANALYSIS_SHA1_LOOKUP", direction: OUT)
  partOfHybridAnalysisSHA256: [HybridAnalysisSHA256Lookup!]! @relationship(type: "PART_OF_HYBRID_ANALYSIS_SHA256_LOOKUP", direction: OUT)
  partOfURLHausSHA256: [URLHausSHA256Lookup!]! @relationship(type: "PART_OF_URL_HAUS_SHA256_LOOKUP", direction: OUT)
  partOfVirusTotalSHA1: [VirusTotalSHA1Lookup!]! @relationship(type: "PART_OF_VIRUS_TOTAL_SHA1_LOOKUP", direction: OUT)
  partOfVirusTotalSHA256: [VirusTotalSHA256Lookup!]! @relationship(type: "PART_OF_VIRUS_TOTAL_SHA256_LOOKUP", direction: OUT)
}
type Malware {
  uid: String
  refs: String
  name: String
  alias: String
  description: String
  mitreId: String
  version: String
  platform: String
  srid: String

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  exploits: [Platform!]! @relationship(type: "EXPLOITS", direction: OUT)
  malUsesTech: [Technique!]! @relationship(type: "MAL_USES_TECH", direction: OUT)
  malUsesTact: [Tactic!]! @relationship(type: "MAL_USES_TACT", direction: OUT)
  malUsedByThreat: [ThreatActor!]! @relationship(type: "MAL_USED_BY_THREAT", direction: OUT)
  malLinksRat: [Category!]! @relationship(type: "MAL_LINKS_RAT", direction: OUT)
  malLinksBank: [Category!]! @relationship(type: "MAL_LINKS_BANK", direction: OUT)
  hasAlias: [MalwareAlias!]! @relationship(type: "HAS_ALIAS", direction: OUT)
  malCreated: [Created!]! @relationship(type: "MAL_CREATED", direction: OUT)
  malModified: [Modified!]! @relationship(type: "MAL_MODIFIED", direction: OUT)
  campaignUsesMal: [AttackCampaign!]! @relationship(type: "CAMPAIGN_USES_MAL", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ipv6Indicator: [IPV6!]! @relationship(type: "IPV6_INDICATOR", direction: OUT, properties: "_TimeProperty")
  fileIndicator: [FileName!]! @relationship(type: "FILE_INDICATOR", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT, properties: "_TimeProperty")
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT, properties: "_TimeProperty")
  emailIndicator: [Email!]! @relationship(type: "EMAIL_INDICATOR", direction: OUT, properties: "_TimeProperty")
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha512Indicator: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ssdeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  authentihashIndicator: [AuthentiHash!]! @relationship(type: "AUTHENTIHASH_INDICATOR", direction: OUT)
  imphashIndicator: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT)
  vhashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  usedInTrans: [Transaction!]! @relationship(type: "USED_IN_TRANS", direction: OUT)
  usedIn: [Strike!]! @relationship(type: "USED_IN", direction: OUT)
  hasCampaign: [AttackCampaign!]! @relationship(type: "HAS_CAMPAIGN", direction: OUT)
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  hasStage: [Stage!]! @relationship(type: "HAS_STAGE", direction: OUT)
  malwareSponsoredBy: [Country!]! @relationship(type: "MALWARE_SPONSORED_BY", direction: OUT)
  targetCountry: [Country!]! @relationship(type: "TARGETS_COUNTRY", direction: OUT)
  partOfCert: [Cert!]! @relationship(type: "PART_OF_CERT", direction: OUT)
  packedBy: [Packer!]! @relationship(type: "PACKED_BY", direction: OUT)
  mitigatedBy: [Mitigation!]! @relationship(type: "MITIGATED_BY", direction: OUT)
  usedByObject: [Object!]! @relationship(type: "USED_BY_OBJECT", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  compromisesProduct: [Product!]! @relationship(type: "COMPROMISES", direction: OUT)
  cveIndicator: [CVE!]! @relationship(type: "INDICATES_CVE",direction: OUT)
  targetsSector: [Sector!]! @relationship(type: "TARGETS_SECTOR", direction: OUT)
  targetsRegion: [Region!]! @relationship(type: "TARGETS_REGION", direction: OUT)
  targetsIndustry: [Industry!]! @relationship(type: "TARGETS_INDUSTRY", direction: OUT)
}
type MalwareAlias {
  name: String
  srid: String
  uid: String
  displayName: String
  aliasOf: [Malware!]! @relationship(type: "ALIAS_OF", direction: OUT)
}
type Modified {
  name: String
  uid: String
  srid: String
  modifiedMalware: [Malware!]! @relationship(type: "MODIFIED_MALWARE", direction: OUT)
  modifiedTool: [Tool!]! @relationship(type: "MODIFIED_TOOL", direction: OUT)
}
type Mitigation {
  srid: String
  uid: String
  name: String
  displayName: String
  description: String
  status: String
  tlp: String
  type: String
  sig: String
  gid: GenericScalar
  sid: GenericScalar
  ttl: GenericScalar
  confidence: String
  fpStatus: [String]
  createdAt: Float
  service: [String]
  updatedAt: Float
  eventId: GenericScalar
  createdDate: GenericScalar
  modifiedDate: GenericScalar
  classType: String
  protocol: String
  meta: GenericScalar
  source_port: GenericScalar
  destination_port: GenericScalar
  fields: [String]
  deployable: Boolean
  validator: String
  level: String
  validatorType: String
  ruleCategory: String
  logSourceCategory: GenericScalar

  hasTactic : [Tactic!]! @relationship(type: "HAS_TACTIC", direction: OUT)
  hasTechnique : [Technique!]! @relationship(type: "HAS_TECHNIQUE", direction: OUT)
  author: [Author!]! @relationship(type: "INDICATES_AUTHOR", direction: OUT)
  platform: [Platform!]! @relationship(type: "TARGETS_PLATFORM", direction: OUT)
  category: [Category!]! @relationship(type: "HAS_CATEGORY", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha512Indicator: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ssdeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  imphashIndicator: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT)
  vhashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  authentihashIndicator: [AuthentiHash!]! @relationship(type: "AUTHENTIHASH_INDICATOR", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ipv6Indicator: [IPV6!]! @relationship(type: "IPV6_INDICATOR", direction: OUT, properties: "_TimeProperty")
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT, properties: "_TimeProperty")
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT, properties: "_TimeProperty")
  emailIndicator: [Email!]! @relationship(type: "EMAIL_INDICATOR", direction: OUT, properties: "_TimeProperty")
  fileIndicator: [FileName!]! @relationship(type: "FILE_INDICATOR", direction: OUT)
  partOf: [Transaction!]! @relationship(type: "PART_OF", direction: OUT)
  partOfCert: [Cert!]! @relationship(type: "PART_OF_CERT", direction: OUT)
  mitigatesMalware: [Malware!]! @relationship(type: "MITIGATES_MALWARE", direction: OUT)
  mitigatesRansom: [Ransom!]! @relationship(type: "MITIGATION_USES_RANSOM", direction: OUT)
  mitigatesThreatActor: [ThreatActor!]! @relationship(type: "MITIGATION_USED_BY_TA", direction: OUT)
  mitigatesTool: [Tool!]! @relationship(type: "MITIGATION_USES_TOOL", direction: OUT)
  tags: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  strikes: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT)
  mitigatesAttackCampaign: [AttackCampaign!]! @relationship(type: "MITIGATES_ATTACK_CAMPAIGN", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  objectIndicator: [Object!]! @relationship(type: "OBJECT_INDICATOR", direction: OUT)
  hasSource: [Source!]! @relationship(type: "HAS_SOURCE",direction: OUT, properties: "_SourceRelProperties")
  cveIndicator: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT)
  references: [Reference!]! @relationship(type: "INDICATES_REFERENCE", direction: OUT)
  sourceIP: [RuleIP!]! @relationship(type: "SOURCE_IP", direction: OUT)
  destinationIP: [RuleIP!]! @relationship(type: "DESTINATION_IP", direction: OUT)
}

type RuleIP {
  name: String
  srid: String
  uid: String
  createdAt: Float
  updatedAt: Float
}
type Nameserver {
  name: String
  srid: String
  uid: String
  updatedAt: Float
  createdAt: Float
  density: Float
  domainIndicator: [Domain!]! @relationship(type: "NAMESERVER_OF_DOMAIN", direction: OUT)
  whoIsIndicator: [WhoIs!]! @relationship(type: "NAMESERVER_OF", direction: OUT)
}
type News {
  uid: String
  srid: String
  updatedAt: Float
  createdAt: Float
  title: String
  summary: String
  content: String
  date: Float
  crawler: String
  category: String
  case: [Case] @computed(from: ["srid", "cves"])

  cves: [String] @cypher(statement: "MATCH (this)-[]->(cve:CVE) RETURN COLLECT(cve.name)")
  mentionsAsn: [ASN!]! @relationship(type: "MENTIONS_ASN", direction: OUT)
  mentionsCountry: [Country!]! @relationship(type: "MENTIONS_COUNTRY", direction: OUT)
  mentionsCve: [CVE!]! @relationship(type: "MENTIONS_CVE", direction: OUT)
  newsOf: [CVE!]! @relationship(type: "NEWS_OF", direction: OUT, properties: "_TimeProperty")
  mentionsDomain: [Domain!]! @relationship(type: "MENTIONS_DOMAIN", direction: OUT)
  mentionsEmail: [Email!]! @relationship(type: "MENTIONS_EMAIL", direction: OUT)
  mentionsIp: [IP!]! @relationship(type: "MENTIONS_IP", direction: OUT)
  mentionsIpV6: [IPV6!]! @relationship(type: "MENTIONS_IPV6", direction: OUT)
  mentionsMac: [MAC!]! @relationship(type: "MENTIONS_MAC", direction: OUT)
  mentionsMalware: [Malware!]! @relationship(type: "MENTIONS_MALWARE", direction: OUT)
  mentionsMd5: [MD5!]! @relationship(type: "MENTIONS_MD5", direction: OUT)
  mentionsPlatform: [Platform!]! @relationship(type: "MENTIONS_PLATFORM", direction: OUT)
  mentionsRansom: [Ransom!]! @relationship(type: "MENTIONS_RANSOM", direction: OUT)
  mentionsSector: [Sector!]! @relationship(type: "MENTIONS_SECTOR", direction: OUT)
  mentionsSha1: [SHA1!]! @relationship(type: "MENTIONS_SHA1", direction: OUT)
  mentionsSha256: [SHA256!]! @relationship(type: "MENTIONS_SHA256", direction: OUT)
  mentionsSha512: [SHA512!]! @relationship(type: "MENTIONS_SHA512", direction: OUT)
  mentionsSSDeep: [SSDeep!]! @relationship(type: "MENTIONS_SSDEEP", direction: OUT)
  mentionsThreatActor: [ThreatActor!]! @relationship(type: "MENTIONS_THREAT_ACTOR", direction: OUT)
  mentionsTool: [Tool!]! @relationship(type: "MENTIONS_TOOL", direction: OUT)
  mentionsUrl: [URL!]! @relationship(type: "MENTIONS_URL", direction: OUT)
  mentionsMitigation: [Mitigation!]! @relationship(type: "MENTIONS_MITIGATION", direction: OUT)
  refs: Reference @relationship(type: "HAS_REFERENCE", direction: OUT)
  tags: [Tag!]! @relationship(type: "TAG_OF_NEWS", direction: OUT)
  patchTuesday: [PatchTuesday!]! @relationship(type: "RELATES_TO", direction: OUT, properties: "_TimeProperty")
  hasAdvisory: [Advisory!]! @relationship(type: "HAS_ADVISORY", direction: OUT, properties: "_TimeProperty")
  mentionsObject: [Object!]! @relationship(type: "MENTIONS_OBJECT", direction: OUT, properties: "_TimeProperty")
}
type Packer {
  uid: String
  srid: String
  name: String
  is_packed: Boolean

  packsObject: [Object!]! @relationship(type: "PACKS_OBJECT", direction: OUT)
  packsMalware: [Malware!]! @relationship(type: "PACKS_MALWARE", direction: OUT)
  partOfCert: [Cert!]! @relationship(type: "PART_OF_CERT", direction: OUT)
}
type Port {
  uid: String
  srid: String
  name: Int
  domainPort: [Domain!]! @relationship(type: "PORT_OF", direction: OUT, properties: "_PortType")
  ipPort: [IP!]! @relationship(type: "PORT_OF", direction: OUT, properties: "_PortType")
  urlPort: [URL!]! @relationship(type: "PORT_OF", direction: OUT, properties: "_PortType")
}
interface _PortType @relationshipProperties {
  type: String
}
type Object {
  uid: String
  srid: String
  name: String @cypher(statement: "MATCH (this)-[:HAS_MD5|:HAS_SHA1|:HAS_SHA256|:HAS_SHA512]->(hash) RETURN HEAD(COLLECT(hash.name)) ")
  description: String
  size: Float
  sizeUnit: String
  entropy: Float
  fileFormat: String
  extension: String
  updatedAt: Float
  createdAt: Float
  firstSeen: Float
  lastSeen: Float
  score: Int
  confidence: String
  verdict: String
  approved: Boolean
  fp: Boolean

  md5: [MD5!]! @relationship(type: "HAS_MD5", direction: OUT)
  sha1: [SHA1!]! @relationship(type: "HAS_SHA1", direction: OUT)
  sha256: [SHA256!]! @relationship(type: "HAS_SHA256", direction: OUT)
  sha512: [SHA512!]! @relationship(type: "HAS_SHA512", direction: OUT)
  ssDeep: [SSDeep!]! @relationship(type: "HAS_SSDEEP", direction: OUT)
  vHash: [VHash!]! @relationship(type: "HAS_VHASH", direction: OUT)
  telfHash: [TelfHash!]! @relationship(type: "HAS_TELFHASH", direction: OUT)
  impHash: [ImpHash!]! @relationship(type: "HAS_IMPHASH", direction: OUT)
  authentiHash: [AuthentiHash!]! @relationship(type: "HAS_AUTHENTIHASH", direction: OUT)

  usedByAttackCampaign: [AttackCampaign!]! @relationship(type: "OBJECT_USED_BY_ATTACK_CAMPAIGN", direction: OUT)
  packedBy: [Packer!]! @relationship(type: "PACKED_BY", direction: OUT)
  relatedToObject: [Object!]! @relationship(type: "RELATED_TO", direction: OUT)
  droppedObject: [Object!]! @relationship(type: "DROPPED_OBJECT", direction: OUT)
  droppedByObject: [Object!]! @relationship(type: "DROPPED_BY", direction: OUT)
  deletedObject: [Object!]! @relationship(type: "DELETED_OBJECT", direction: OUT)
  deletedByObject: [Object!]! @relationship(type: "DELETED_BY", direction: OUT)
  openedObject: [Object!]! @relationship(type: "OPENED_OBJECT", direction: OUT)
  openedByObject: [Object!]! @relationship(type: "OPENED_BY", direction: OUT)
  createdObject: [Object!]! @relationship(type: "CREATED_OBJECT", direction: OUT)
  createdByObject: [Object!]! @relationship(type: "CREATED_BY", direction: OUT)
  downloadedObject: [Object!]! @relationship(type: "DOWNLOADED_OBJECT", direction: OUT)
  downloadedByObject: [Object!]! @relationship(type: "DOWNLOADED_BY", direction: OUT)
  hasObject: [Object!]! @relationship(type: "HAS_OBJECT", direction: OUT)
  partOfObject: [Object!]! @relationship(type: "PART_OF_OBJECT", direction: OUT)
  fileType: [FileType!]! @relationship(type: "OF_TYPE", direction: OUT)
  fileIndicator: [FileName!]! @relationship(type: "FILE_INDICATOR", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT)
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT)
  sha512Indicator: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT)
  ssDeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  vHashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  impHashIndicator: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT)
  telfHashIndicator: [TelfHash!]! @relationship(type: "TELFHASH_INDICATOR", direction: OUT)
  usesCVE: [CVE!]! @relationship(type: "OBJECT_USES_CVE", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
#  hasStage: [Stage!]! @relationship(type: "HAS_STAGE", direction: OUT)
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  communicatesWithUrl: [URL!]! @relationship(type: "COMMUNICATES_WITH_URL", direction: OUT)
  downloadedFromUrl: [URL!]! @relationship(type: "DOWNLOADED_FROM_URL", direction: OUT)
  communicatesWithDomain: [Domain!]! @relationship(type: "COMMUNICATES_WITH_DOMAIN", direction: OUT)
  downloadedFromDomain: [Domain!]! @relationship(type: "DOWNLOADED_FROM_DOMAIN", direction: OUT)
  communicatesWithIp: [IP!]! @relationship(type: "COMMUNICATES_WITH_IP", direction: OUT)
  downloadedFromIp: [IP!]! @relationship(type: "DOWNLOADED_FROM_IP", direction: OUT)
  usesMalware: [Malware!]! @relationship(type: "OBJECT_USES_MAL", direction: OUT)
  usedByThreatActor: [ThreatActor!]! @relationship(type: "OBJECT_USED_BY_TA", direction: OUT)
  #  usesTactic:[Tactic!]! @relationship(type:"OBJECT_USES_TACT", direction: OUT)
  #  usesTechnique:[Technique!]! @relationship(type:"OBJECT_USES_TECH", direction: OUT)
  usesRansom: [Ransom!]! @relationship(type: "OBJECT_USES_RANSOM", direction: OUT)
  usesTool: [Tool!]! @relationship(type: "OBJECT_USES_TOOL", direction: OUT)
  #  targetsPlatform:[Platform!]! @relationship(type:"TARGETS_PLATFORM", direction: OUT)
  deliveredByEmail: [Email!]! @relationship(type: "DELIVERED_BY_EMAIL", direction: OUT)
  mitigatedBy: [Mitigation!]! @relationship(type: "MITIGATED_BY", direction: OUT)
  #  hasReference:[Reference!]! @relationship(type:"HAS_REFERENCE", direction: OUT)
  reportedByCert: [Cert!]! @relationship(type: "REPORTED_BY_CERT", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_SourceRelProperties")
#  usedByTactic: [Tactic!]! @relationship(type: "OBJECT_USED_BY_TACTIC", direction: OUT)
#  usedByTechnique: [Technique!]! @relationship(type: "OBJECT_USED_BY_TECHNIQUE", direction: OUT)
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_OBJECT", direction: OUT)
  hasVulnerability: [Vulnerability!]! @relationship(type: "HAS_VULNERABILITY", direction: OUT)
  hasAnalysis: [Analysis!]! @relationship(type: "HAS_ANALYSIS", direction: OUT, properties: "_TimeProperty")
  hasIpHost: [IP!]! @relationship(type: "HAS_HOST", direction: OUT)
  hasDomainHost: [Domain!]! @relationship(type: "HAS_HOST", direction: OUT)
  hasTactic : [Tactic!]! @relationship(type: "HAS_TACTIC", direction: OUT)
  hasTechnique : [Technique!]! @relationship(type: "HAS_TECHNIQUE", direction: OUT)
  hasSubTechnique : [Technique!]! @relationship(type: "HAS_SUB_TECHNIQUE", direction: OUT)
  objectCategory: [Category!]! @relationship(type: "HAS_CATEGORY",direction: OUT)
  originOfObject: [Country!]! @relationship(type: "OBJ_UPLOADED_ORIGIN", direction: OUT)

}
type Operator {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  hasCve: [CVE!]! @relationship(type: "HAS_CVE", direction: OUT, properties: "_TimeProperty")
  hasVersion: [Version!]! @relationship(type: "HAS_VERSION", direction: OUT, properties: "_TimeProperty")
}
type Cert {
  uid: String
  srid: String
  name: String
  tile: String
  type: String
  date: String

  reportReference: [Reference!]! @relationship(type: "HAS_REPORT_REFERENCE", direction: OUT)
  stixReference: [Reference!]! @relationship(type: "HAS_STIX_REFERENCE", direction: OUT)
  csvReference: [Reference!]! @relationship(type: "HAS_CSV_REFERENCE", direction: OUT)
  hasMalware: [Malware!]! @relationship(type: "HAS_MALWARE", direction: OUT)
  hasPacker: [Packer!]! @relationship(type: "HAS_PACKER", direction: OUT)
  reportsObject: [Object!]! @relationship(type: "REPORTS_OBJECT", direction: OUT)
  reportsCountry: [Country!]! @relationship(type: "REPORTS_COUNTRY", direction: OUT)
  providesMitigation: [Mitigation!]! @relationship(type: "HAS_MITIGATION", direction: OUT)
  fileIndicator: [FileName!]! @relationship(type: "FILE_INDICATOR", direction: OUT)
  emailIndicator: [Email!]! @relationship(type: "EMAIL_INDICATOR", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT)
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT)
  sha512Indicator: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT)
  ssDeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  vHashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  hasStage: [Stage!]! @relationship(type: "HAS_STAGE", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  cve: [CVE!]! @relationship(type: "EXPLOITS_CVE", direction: OUT)
}
type RansomNote {
  uid: String
  srid: String
  url: String

  noteOfRansom: [Ransom!]! @relationship(type: "NOTE_OF_RANSOM", direction: OUT)
  contactEmail: [Email!]! @relationship(type: "CONTACT_EMAIL", direction: OUT)
  hasBTC: [BTC!]! @relationship(type: "HAS_BTC", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT)
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT)
  ssdeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  imphashIndicator: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT)
  vhashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  authentihashIndicator: [AuthentiHash!]! @relationship(type: "AUTHENTIHASH_INDICATOR", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT)
  fileIndicator: [FileName!]! @relationship(type: "FILE_INDICATOR", direction: OUT)
  dropsObject: [Object!]! @relationship(type: "DROPS_OBJECT", direction: OUT)
}
type Reference {
  uid: String
  srid: String
  url: String
  name: String

  refOfObject: [Object!]! @relationship(type: "REF_OF_OBJECT", direction: OUT)
  refOfMalware: [Malware!]! @relationship(type: "REF_OF_MALWARE", direction: OUT)
  refOfRansom: [Ransom!]! @relationship(type: "REF_OF_RANSOM", direction: OUT)
  refOfThreatActor: [ThreatActor!]! @relationship(type: "REF_OF_TA", direction: OUT)
  refOfCve: [CVE!]! @relationship(type: "REF_OF", direction: OUT, properties: "_TimeProperty")
  refOfCertRep: [Cert!]! @relationship(type: "REF_OF_CERT_REPORT", direction: OUT)
  refOfCertStix: [Cert!]! @relationship(type: "REF_OF_CERT_STIX", direction: OUT)
  refOfCertCsv: [Cert!]! @relationship(type: "REF_OF_CERT_CSV", direction: OUT)
  refOfDecrypter: [Decrypter!]! @relationship(type: "REF_OF_DECRYPTER", direction: OUT)
  refOfTool: [Tool!]! @relationship(type: "REF_OF_TOOL", direction: OUT)
  refOfCampaign: [AttackCampaign!]! @relationship(type: "REF_OF", direction: OUT)
  refOfStrike: [Strike!]! @relationship(type: "REF_OF_STRIKE", direction: OUT)
  analysisRefOfStrike: [Strike!]! @relationship(type: "ANALYSIS_REF_OF_STRIKE", direction: OUT)
  newsRefOfStrike: [Strike!]! @relationship(type: "NEWS_REF_OF_STRIKE", direction: OUT)
  hasAdvisory: [Advisory!]! @relationship(type: "REF_OF", direction: OUT, properties: "_TimeProperty")
  patchTuesday: [PatchTuesday!]! @relationship(type: "RELATES_TO", direction: OUT, properties: "_TimeProperty")
}
type OPSWATDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  address: String
  lookup_results: String

  lookupOf: [Domain!]! @relationship(type: "OPSWAT_DOMAIN_LOOKUP_OF", direction: OUT)
}
type OPSWATMD5Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  additional_info: String
  appinfo: Boolean
  data_id: String
  extracted_files: String
  file_id: String
  file_info: String
  malware_family: String
  malware_type: String
  parent_data_id: String
  process_info: String
  rest_version: String
  scan_results: String
  scan_result_history_length: Int
  share_file: Int
  threat_name: String
  votes: String

  lookupOf: [MD5!]! @relationship(type: "OPSWAT_MD5_LOOKUP_OF", direction: OUT)
}
type OPSWATSHA1Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  additional_info: String
  appinfo: Boolean
  data_id: String
  extracted_files: String
  file_id: String
  file_info: String
  malware_family: String
  malware_type: String
  parent_data_id: String
  process_info: String
  rest_version: String
  scan_results: String
  scan_result_history_length: Int
  share_file: Int
  threat_name: String
  votes: String

  lookupOf: [SHA1!]! @relationship(type: "OPSWAT_SHA1_LOOKUP_OF", direction: OUT)
}
type OPSWATSHA256Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  additional_info: String
  appinfo: Boolean
  data_id: String
  extracted_files: String
  file_id: String
  file_info: String
  malware_family: String
  malware_type: String
  parent_data_id: String
  process_info: String
  rest_version: String
  scan_results: String
  scan_result_history_length: Int
  share_file: Int
  threat_name: String
  votes: String

  lookupOf: [SHA256!]! @relationship(type: "OPSWAT_SHA256_LOOKUP_OF", direction: OUT)
}
type OPSWATIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  address: String
  geo_info: String
  lookup_results: String

  lookupOf: [IP!]! @relationship(type: "OPSWAT_IP_LOOKUP_OF", direction: OUT)
}
type OPSWATUrlLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  address: String
  lookup_results: String

  lookupOf: [URL!]! @relationship(type: "OPSWAT_URL_LOOKUP_OF", direction: OUT)
}
type PassiveDNS {
  uid: String
  srid: String
  address: String
  assetType: String
  domain: String
  firstSeen: String
  flagTitle: String
  flagUrl: String
  hostname: String
  indicatorLink: String
  ip: String
  lastSeen: String
  name: String
  recordType: String
  type: String
  value: String
  record_type: String
  seen_time: Float

  passiveDNSOfDomain: [Domain!]! @relationship(type: "PASSIVE_DNS_OF_DOMAIN", direction: OUT)
  passiveDNSOfIP: [IP!]! @relationship(type: "PASSIVE_DNS_OF_IP", direction: OUT)
  pdDomain: [Domain!]! @relationship(type: "PASSIVE_DNS_OF", direction: OUT)
  ipPassiveDns: [IP!]! @relationship(type: "HAS_PASSIVE_DNS_IP",direction: OUT)
  nameserverPassiveDns: [Nameserver!]! @relationship(type: "HAS_PASSIVE_DNS",direction: OUT, properties: "_DnsSeenTime")

  passiveDNSOfAlienVaultDomain: [AlienVaultDomainLookup!]! @relationship(type: "PASSIVE_DNS_OF_ALIEN_VAULT_DOMAIN_LOOKUP", direction: OUT)
  passiveDNSOfIBMXForceIP: [IBMXForceIPLookup!]! @relationship(type: "PASSIVE_DNS_OF_IBM_XFORCE_IP", direction: OUT)
  passiveDNSOfThreatMinerIP: [ThreatMinerIPLookup!]! @relationship(type: "PASSIVE_DNS_OF_THREAT_MINER_IP", direction: OUT)
  passiveDNSOfThreatMinerDomain: [ThreatMinerDomainLookup!]! @relationship(type: "PASSIVE_DNS_OF_THREAT_MINER_DOMAIN_LOOKUP", direction: OUT)
  passiveDNSOfIBMXForceURL: [IBMXForceURLLookup!]! @relationship(type: "PASSIVE_DNS_OF_IBM_XFORCE_URL", direction: OUT)
}
type Permission {
  name: String
  displayName: String
  uid: String
  srid: String
  requiredBy: [Technique!]! @relationship(type: "REQUIRED_BY", direction: OUT)
}
type PhishTankUrlLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  meta: String
  results: String

  lookupOf: [URL!]! @relationship(type: "PHISH_TANK_URL_LOOKUP_OF", direction: OUT)
}
type PingIP {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  error: String
  ping_output: String
  status_code: Int
  summary: String

  pingOf: [IP!]! @relationship(type: "PING_OF_IP", direction: OUT)
}
type Platform {
  name: String
  displayName: String
  description: String
  uid: String
  srid: String
  exploitedBy: [Malware!]! @relationship(type: "EXPLOITED_BY", direction: OUT)
  exploitedByTech: [Technique!]! @relationship(type: "EXPLOITED_BY_TECH", direction: OUT)
  exploitedByTool: [Tool!]! @relationship(type: "EXPLOITED_BY_TOOL", direction: OUT)
  exploitedByRansom: [Ransom!]! @relationship(type: "EXPLOITED_BY_RANSOM", direction: OUT)
  targetedIn: [Transaction!]! @relationship(type: "TARGETED_IN", direction: OUT)
  targetedInStrike: [Strike!]! @relationship(type: "TARGETED_IN_STRIKE", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
}
type Product {
  uid: String
  srid: String
  name: String
  createdAt: Float
  updatedAt: Float
  displayName: String
  headquarters: String
  description: String
  industry: String
  locations: String
  integrationName: String
  cve: [CVE!]! @relationship(type: "RELATES_CVE", direction: OUT)
  providedBy: [Vendor!]! @relationship(type: "PROVIDED_BY", direction: OUT)
  productUsedBy: [Vendor!]! @relationship(type: "USED_BY", direction: OUT)
  productMaintainer: [Vendor!]! @relationship(type: "MAINTAINED_BY", direction: OUT)
  compromisesVendor: [Vendor!]! @relationship(type: "COMPROMISED", direction: OUT)
  malwareAssociated: [Malware!]! @relationship(type: "COMPROMISED_BY", direction: OUT)
  victimizedBy: [Strike!]! @relationship(type: "VICTIMIZED_BY", direction: OUT)
  hasVendor: [Vendor!]! @relationship(type: "HAS_VENDOR", direction: OUT, properties: "_TimeProperty")
  hasCpe: [CPE!]! @relationship(type: "HAS_CPE", direction: OUT, properties: "_TimeProperty")
  hasVersion: [Version!]! @relationship(type: "HAS_VERSION", direction: OUT, properties: "_TimeProperty")
  hasHardware: [Hardware!]! @relationship(type: "HAS_HARDWARE", direction: OUT, properties: "_TimeProperty")
}
type PulseDiveUrlLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  attributes: String
  comments: String
  domain: String
  domainiid: String
  feeds: String
  iid: Int
  indicator: String
  manualrisk: Int
  properties: String
  recent: Int
  redirects: String
  retired: String
  riskfactors: String
  risk_recommended: String
  risk: String
  stamp_added: String
  stamp_probed: String
  stamp_seen: String
  stamp_updated: String
  threats: String
  type: String
  umbrella_domain: String
  umbrella_rank: Int

  lookupOf: [URL!]! @relationship(type: "PULSE_DIVE_URL_LOOKUP_OF", direction: OUT)
}
type Ransom {
  uid: String
  srid: String
  name: String
  description: String
  encryption: String
  price: String
  paymentMethod: String
  date: String
  origin: String
  creator: String
  sourceLanguage: String
  family: String
  fileSize: String
  fileType: String
  authentiHash: String
  impHash: String
  md5: String
  sha1: String
  sha256: String
  ssDeep: String
  vHash: String
  extensions: [String]
  ransomNote: String
  ransomwareExtension: [String]
  platform: String
  refs: String
  alias: String
  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  ransomAuthentihash: [AuthentiHash!]! @relationship(type: "RANSOM_AUTHENTIHASH", direction: OUT)
  ransomImphash: [ImpHash!]! @relationship(type: "RANSOM_IMPHASH", direction: OUT)
  ransomDomain: [Domain!]! @relationship(type: "RANSOM_DOMAIN", direction: OUT, properties: "_TimeProperty")
  ransomEmail: [Email!]! @relationship(type: "RANSOM_EMAIL", direction: OUT, properties: "_TimeProperty")
  ransomIp: [IP!]! @relationship(type: "RANSOM_IP", direction: OUT, properties: "_TimeProperty")
  ransomIpv6: [IPV6!]! @relationship(type: "RANSOM_IPV6", direction: OUT, properties: "_TimeProperty")
  ransomMd5: [MD5!]! @relationship(type: "RANSOM_MD5", direction: OUT, properties: "_TimeProperty")
  ransomSha1: [SHA1!]! @relationship(type: "RANSOM_SHA1", direction: OUT, properties: "_TimeProperty")
  ransomSha256: [SHA256!]! @relationship(type: "RANSOM_SHA256", direction: OUT, properties: "_TimeProperty")
  ransomSha512: [SHA512!]! @relationship(type: "RANSOM_SHA512", direction: OUT, properties: "_TimeProperty")
  ransomUrl: [URL!]! @relationship(type: "RANSOM_URL", direction: OUT, properties: "_TimeProperty")
  ransomVhash: [VHash!]! @relationship(type: "RANSOM_VHASH", direction: OUT)
  ransomSsdeep: [SSDeep!]! @relationship(type: "RANSOM_SSDEEP", direction: OUT)
  ransomExploits: [Platform!]! @relationship(type: "RANSOM_EXPLOITS", direction: OUT)
  hasAlias: [RansomAlias!]! @relationship(type: "HAS_ALIAS", direction: OUT)
  ransomCreated: [RansomDate!]! @relationship(type: "RANSOM_CREATED", direction: OUT)
  ransomAttacksExtension: [RansomExtension!]! @relationship(type: "RANSOM_ATTACKS_EXTENSION", direction: OUT)
  ransomFiletype: [RansomFileType!]! @relationship(type: "RANSOM_FILETYPE", direction: OUT)
  ransomFamily: [RansomFamily!]! @relationship(type: "RANSOM_FAMILY", direction: OUT)
  ransomSponsoredBy: [Country!]! @relationship(type: "RANSOM_SPONSORED_BY", direction: OUT)
  decryptedBy: [Decrypter!]! @relationship(type: "DECRYPTED_BY", direction: OUT)
  hasBtc: [BTC!]! @relationship(type: "HAS_BTC", direction: OUT)
  hasCampaign: [AttackCampaign!]! @relationship(type: "HAS_CAMPAIGN", direction: OUT)
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  targetsSector: [Sector!]! @relationship(type: "TARGETS_SECTOR", direction: OUT)
  ransomUsedByThreat: [ThreatActor!]! @relationship(type: "RANSOM_USED_BY_THREAT", direction: OUT)
  usedInStrike: [Strike!]! @relationship(type: "USED_IN_STRIKE", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  ransomTransaction: [Transaction!]! @relationship(type: "USED_BY_TRANSACTION", direction: OUT)
  usedByObject: [Object!]! @relationship(type: "USED_BY_OBJECT", direction: OUT)
  ranUsesTech: [Technique!]! @relationship(type: "RANSOM_USES_TECH", direction: OUT)
  ranUsesTact: [Tactic!]! @relationship(type: "RANSOM_USES_TACT", direction: OUT)
  cveIndicator: [CVE!]! @relationship(type: "INDICATES_CVE",direction: OUT)
}
type RansomAlias {
  name: String
  uid: String
  displayName: String
  srid: String
  aliasOf: [Ransom!]! @relationship(type: "ALIAS_OF", direction: OUT)
}
type RansomDate {
  name: String
  uid: String
  srid: String
  createdRansom: [Ransom!]! @relationship(type: "CREATED_RANSOM", direction: OUT)
}
type RansomExtension {
  name: String
  uid: String
  srid: String
  extensionAttackedByRansom: [Ransom!]! @relationship(type: "EXTENSION_ATTACKED_BY_RANSOM", direction: OUT)
}
type RansomFamily {
  name: String
  uid: String
  srid: String
  familyRelatedToRansom: [Ransom!]! @relationship(type: "FAMILY_RELATED_TO_RANSOM", direction: OUT)
}
type RansomFileType {
  name: String
  uid: String
  srid: String
  filetypeOfRansom: [Ransom!]! @relationship(type: "FILETYPE_OF_RANSOM", direction: OUT)
}
type Region {
  name: String
  srid: String
  uid: String
  regionTargetedBy: [ThreatActor!]! @relationship(type: "REGION_TARGETED_BY", direction: OUT)
}
type Resolution {
  uid: String
  srid: String
  domain: String
  ip_address: String
  last_resolved: String

  resolutionOfIP: [IP!]! @relationship(type: "RESOLUTION_OF_IP", direction: OUT)
  resolutionOfDomain: [Domain!]! @relationship(type: "RESOLUTION_OF_DOMAIN", direction: OUT)

  resolutionOfThreatCrowdIP: [ThreatCrowdIPLookup!]! @relationship(type: "RESOLUTION_OF_THREAT_CROWD_IP", direction: OUT)
  resolutionOfDomainResolution: [DomainResolution!]! @relationship(type: "RESOLUTION_OF_DOMAIN_RESOLUTION", direction: OUT)
  resolutionOfThreatCrowdDomain: [ThreatCrowdDomainLookup!]! @relationship(type: "RESOLUTION_OF_THREAT_CROWD_DOMAIN", direction: OUT)
}
type ShodanIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  asn: String
  city: String
  country_code: String
  country_code3: String
  country_name: String
  data: String
  hostnames: String
  ip: Int
  ip_str: String
  isp: String
  last_update: String
  latitude: Float
  longitude: Float
  org: String
  ports: String
  postal_code: String
  region_code: String
  vulns: String

  hasDomain: [Domain!]! @relationship(type: "HAS_DOMAIN", direction: OUT)
  hasHostname: [Subdomain!]! @relationship(type: "SHODAN_IP_SUBDOMAIN", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  lookupOf: [IP!]! @relationship(type: "SHODAN_IP_LOOKUP_OF", direction: OUT)
}
type SHA1 {
  name: String
  srid: String
  uid: String
  updatedAt: Float
  createdAt: Float
  score: Int
  confidence: String
  firstSeen: Float
  lastSeen: Float
  fp: Boolean

  fingerprintDomainCertificate: [DomainCertificate!]! @relationship(type: "SHA_1_FINGERPRINT_OF_DOMAIN_CERTIFICATE", direction: OUT)

  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_TimeProperty")
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  ofObject: [Object!]! @relationship(type: "SHA1_OF_OBJECT", direction: OUT, properties: "_TimeProperty")

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  sha1OfRansom: [Ransom!]! @relationship(type: "SHA1_OF_RANSOM", direction: OUT, properties: "_TimeProperty")
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  indicatesAttackCampaign: [AttackCampaign!]! @relationship(type: "INDICATES_ATTACK_CAMPAIGN", direction: OUT)
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_SHA1", direction: OUT)
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT, properties: "_TimeProperty")
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT, properties: "_TimeProperty")
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT, properties: "_TimeProperty")
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT, properties: "_TimeProperty")
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT, properties: "_TimeProperty")

  hybridAnalysisSHA1Lookup: [HybridAnalysisSHA1Lookup!]! @relationship(type: "HYBRID_ANALYSIS_SHA1_LOOKUP", direction: OUT)
  ibmXForceSHA1Lookup: [IBMXForceSHA1Lookup!]! @relationship(type: "IBM_XFORCE_SHA1_LOOKUP", direction: OUT)
  opswatSHA1Lookup: [OPSWATSHA1Lookup!]! @relationship(type: "OPSWAT_SHA1_LOOKUP", direction: OUT)
  threatCrowdSHA1Lookup: [ThreatCrowdMD5Lookup!]! @relationship(type: "THREAT_CROWD_SHA1_LOOKUP", direction: OUT)
  virusTotalSHA1Lookup: [VirusTotalSHA1Lookup!]! @relationship(type: "VIRUS_TOTAL_SHA1_LOOKUP", direction: OUT)

  partOfHybridAnalysisMD5: [HybridAnalysisMD5Lookup!]! @relationship(type: "PART_OF_HYBRID_ANALYSIS_MD5_LOOKUP", direction: OUT)
  partOfHybridAnalysisSHA256: [HybridAnalysisSHA256Lookup!]! @relationship(type: "PART_OF_HYBRID_ANALYSIS_SHA256_LOOKUP", direction: OUT)
  partOfVirusTotalMD5: [VirusTotalMD5Lookup!]! @relationship(type: "PART_OF_VIRUS_TOTAL_MD5_LOOKUP", direction: OUT)
  partOfVirusTotalSHA256: [VirusTotalSHA256Lookup!]! @relationship(type: "PART_OF_VIRUS_TOTAL_SHA256_LOOKUP", direction: OUT)
}
type SHA256 {
  name: String
  srid: String
  uid: String
  updatedAt: Float
  createdAt: Float
  score: Int
  confidence: String
  firstSeen: Float
  lastSeen: Float
  fp: Boolean

  fingerprintDomainCertificate: [DomainCertificate!]! @relationship(type: "SHA_256_FINGERPRINT_OF_DOMAIN_CERTIFICATE", direction: OUT)

  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_TimeProperty")
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  ofObject: [Object!]! @relationship(type: "SHA256_OF_OBJECT", direction: OUT, properties: "_TimeProperty")

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  sha256OfRansom: [Ransom!]! @relationship(type: "SHA256_OF_RANSOM", direction: OUT, properties: "_TimeProperty")
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  indicatesAttackCampaign: [AttackCampaign!]! @relationship(type: "INDICATES_ATTACK_CAMPAIGN", direction: OUT)
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_SHA256", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT, properties: "_TimeProperty")
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT, properties: "_TimeProperty")
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT, properties: "_TimeProperty")
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT, properties: "_TimeProperty")
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT, properties: "_TimeProperty")

  hybridAnalysisSHA256Lookup: [HybridAnalysisSHA256Lookup!]! @relationship(type: "HYBRID_ANALYSIS_SHA256_LOOKUP", direction: OUT)
  ibmXForceSHA256Lookup: [IBMXForceSHA256Lookup!]! @relationship(type: "IBM_XFORCE_SHA256_LOOKUP", direction: OUT)
  opswatSHA256Lookup: [OPSWATSHA256Lookup!]! @relationship(type: "OPSWAT_SHA256_LOOKUP", direction: OUT)
  urlHausSHA256Lookup: [URLHausSHA256Lookup!]! @relationship(type: "URL_HAUS_SHA256_LOOKUP", direction: OUT)
  virusTotalSHA256Lookup: [VirusTotalSHA256Lookup!]! @relationship(type: "VIRUS_TOTAL_SHA256_LOOKUP", direction: OUT)

  partOfHybridAnalysisMD5: [HybridAnalysisMD5Lookup!]! @relationship(type: "PART_OF_HYBRID_ANALYSIS_MD5_LOOKUP", direction: OUT)
  partOfHybridAnalysisSHA1: [HybridAnalysisSHA1Lookup!]! @relationship(type: "PART_OF_HYBRID_ANALYSIS_SHA1_LOOKUP", direction: OUT)
  partOfURLHausMD5: [URLHausMD5Lookup!]! @relationship(type: "PART_OF_URL_HAUS_MD5_LOOKUP", direction: OUT)
  partOfVirusTotalMD5: [VirusTotalMD5Lookup!]! @relationship(type: "PART_OF_VIRUS_TOTAL_MD5_LOOKUP", direction: OUT)
  partOfVirusTotalSHA1: [VirusTotalSHA1Lookup!]! @relationship(type: "PART_OF_VIRUS_TOTAL_SHA1_LOOKUP", direction: OUT)
}
type SHA3_384{
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  ofObject: [Object!]! @relationship(type: "SHA3_384_OF_OBJECT", direction: OUT, properties: "_TimeProperty")
}
type SHA512 {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  score: Int
  confidence: String
  firstSeen: Float
  lastSeen: Float
  fp: Boolean

  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_TimeProperty")
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT, properties: "_TimeProperty")
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  sha512OfRansom: [Ransom!]! @relationship(type: "SHA512_OF_RANSOM", direction: OUT, properties: "_TimeProperty")
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT, properties: "_TimeProperty")
  ofObject: [Object!]! @relationship(type: "SHA512_OF_OBJECT", direction: OUT, properties: "_TimeProperty")

  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT, properties: "_TimeProperty")
  indicatesThreatActor: [ThreatActor!]! @relationship(type: "INDICATES_THREAT_ACTOR", direction: OUT, properties: "_TimeProperty")
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)

  partOfHybridAnalysisMD5: [HybridAnalysisMD5Lookup!]! @relationship(type: "PART_OF_HYBRID_ANALYSIS_MD5_LOOKUP", direction: OUT)
  partOfHybridAnalysisSHA1: [HybridAnalysisSHA1Lookup!]! @relationship(type: "PART_OF_HYBRID_ANALYSIS_SHA1_LOOKUP", direction: OUT)
  partOfHybridAnalysisSHA256: [HybridAnalysisSHA256Lookup!]! @relationship(type: "PART_OF_HYBRID_ANALYSIS_SHA256_LOOKUP", direction: OUT)
}
type Source {
  name: String
  hash: String
  srid: String
  uid: String
  updatedAt: Float
  createdAt: Float
  confidence: String
  type: String
  url: String
  displayName: String
  month: String
  timestamp: Float
  year: Int
  sourceOfDomain: [Domain!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_SourceRelProperties")
  sourceOfEmail: [Email!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_TimeProperty")
  sourceOfIp: [IP!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_SourceRelProperties")
  sourceOfIpv6: [IPV6!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_TimeProperty")
  sourceOfMd5: [MD5!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_TimeProperty")
  sourceOfSha1: [SHA1!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_TimeProperty")
  sourceOfSha256: [SHA256!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_TimeProperty")
  sourceOfSha512: [SHA512!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_TimeProperty")
  sourceOfUrl: [URL!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_SourceRelProperties")
  sourceOfObject: [Object!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_SourceRelProperties")
  sourceOfCve: [CVE!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_SourceRelProperties")
  relatesCve: [CVE!]! @relationship(type: "RELATES_CVE", direction: OUT, properties: "_TimeProperty")
  hasCpe: [CPE!]! @relationship(type: "HAS_CPE", direction: OUT, properties: "_TimeProperty")
  hasAdvisory: [Advisory!]! @relationship(type: "HAS_ADVISORY", direction: OUT, properties: "_TimeProperty")
  patchTuesday: [PatchTuesday!]! @relationship(type: "HAS_RELATES_TO", direction: OUT, properties: "_TimeProperty")
  sourceOfAnalysis: [Analysis!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_SourceRelProperties")
  sourceOfMitigation: [Mitigation!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_SourceRelProperties")
  sourceOfCategory: [Category!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_SourceRelProperties")
  sourceOfStage: [Stage!]! @relationship(type: "SOURCE_OF", direction: OUT, properties: "_SourceRelProperties")
}
interface _SourceRelProperties @relationshipProperties {
  createdAt: Float
  updatedAt: Float
  reported_time: Float
}
type SSDeep {
  name: String
  srid: String
  uid: String

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  ssdeepOfRansom: [Ransom!]! @relationship(type: "SSDEEP_OF_RANSOM", direction: OUT)
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  indicatesAttackCampaign: [AttackCampaign!]! @relationship(type: "INDICATES_ATTACK_CAMPAIGN", direction: OUT)
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT)
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_SSDEEP", direction: OUT)
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT)
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT)
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT)
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT)
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  ofObject: [Object!]! @relationship(type: "SSDEEP_OF_OBJECT", direction: OUT, properties: "_TimeProperty")
}
type Sector {
  name: String
  displayName: String
  uid: String
  srid: String
  ransomTargetsSector: [Ransom!]! @relationship(type: "RANSOM_TARGETS_SECTOR", direction: OUT)
  campaignTargetsSector: [AttackCampaign!]! @relationship(type: "CAMPAIGN_TARGETS_SECTOR", direction: OUT)
  sectorTargetedBy: [ThreatActor!]! @relationship(type: "SECTOR_TARGETED_BY", direction: OUT)
  targetedBy: [Strike!]! @relationship(type: "TARGETED_BY", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  urlTargetsSector: [URL!]! @relationship(type: "TARGETED_BY", direction: OUT)
}
type Stage {
  srid: String
  uid: String
  name: String
  authentihashIndicator: [AuthentiHash!]! @relationship(type: "AUTHENTIHASH_INDICATOR", direction: OUT)
  fileIndicator: [FileName!]! @relationship(type: "FILE_INDICATOR", direction: OUT)
  imphashIndicator: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT)
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT)
  ssdeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  partOf: [Transaction!]! @relationship(type: "PART_OF", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT)
  vhashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT)
  partOfObject: [Object!]! @relationship(type: "PART_OF_OBJECT", direction: OUT)
  objectIndicator: [Object!]! @relationship(type: "OBJECT_INDICATOR", direction: OUT)
  partOfCert: [Cert!]! @relationship(type: "PART_OF_CERT", direction: OUT)
  partOfMalware: [Malware!]! @relationship(type: "PART_OF_MALWARE", direction: OUT)
  hasCategory: [Category!]! @relationship(type: "HAS_CATEGORY", direction: OUT)
  hasSource:[Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_SourceRelProperties")
}
interface _StatusTimeProperty @relationshipProperties {
  updatedAt: Float
  createdAt: Float
  start: Float
  end: Float
}
type Status {
  uid: String
  status: String
  updatedAt: Float
  createdAt: Float
  statusOfIp: [IP!]! @relationship(type: "STATUS_OF", direction: OUT, properties: "_StatusTimeProperty")
  statusOfIpv6: [IPV6!]! @relationship(type: "STATUS_OF", direction: OUT, properties: "_StatusTimeProperty")
  statusOfUrl: [URL!]! @relationship(type: "STATUS_OF", direction: OUT, properties: "_StatusTimeProperty")
}
interface _StatusRelProperties @relationshipProperties {
  createdAt: Float
  expiredAt: Float
}
type Strike {
  uid: String
  srid: String
  name: String
  verified: Boolean
  category: String
  subcategory: String
  description: String
  threatVector: String
  score: String
  severity: String
  victim: String
  implications: String
  impact: String
  attackType: String
  ettr: Float
  timeout: Float
  createdAt: Float
  updatedAt: Float
  advisories: [String]

  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT, properties: "_TimeProperty")
  emailIndicator: [Email!]! @relationship(type: "EMAIL_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ipv6Indicator: [IPV6!]! @relationship(type: "IPV6_INDICATOR", direction: OUT, properties: "_TimeProperty")
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha512Indicator: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT, properties: "_TimeProperty")
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT, properties: "_TimeProperty")
  objectIndicator: [Object!]! @relationship(type: "OBJECT_INDICATOR", direction: OUT, properties: "_TimeProperty")

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  affectedRegions: [Country!]! @relationship(type: "AFFECTED", direction: OUT)
  attackCampaigns: [AttackCampaign!]! @relationship(type: "HAS_CAMPAIGN", direction: OUT)
  categories: [Category!]! @relationship(type: "CATEGORY", direction: OUT)
  exploitsCVE: [CVE!]! @relationship(type: "EXPLOITS", direction: OUT, properties: "_TimeProperty")
  targetsIndustry: [Industry!]! @relationship(type: "TARGETS_INDUSTRY", direction: OUT)
  malwareUsed: [Malware!]! @relationship(type: "MALWARE_USED", direction: OUT)
  relates: [News!]! @relationship(type: "RELATES", direction: OUT)
  originCountry: [Country!]! @relationship(type: "ORIGINATED_IN", direction: OUT)
  targetsPlatform: [Platform!]! @relationship(type: "TARGETS_PLATFORM", direction: OUT)
  ransomnsUsed: [Ransom!]! @relationship(type: "RANSOM_USED", direction: OUT)
  analysisLinks: [Reference!]! @relationship(type: "HAS_ANALYSIS_REFERENCE", direction: OUT)
  newsLinks: [Reference!]! @relationship(type: "HAS_NEWS_REFERENCE", direction: OUT)
  refs: [Reference!]! @relationship(type: "HAS_REFERENCE", direction: OUT)
  targetsSector: [Sector!]! @relationship(type: "TARGETS_SECTOR", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  usedByTA: [ThreatActor!]! @relationship(type: "USED_BY", direction: OUT)
  toolUsed: [Tool!]! @relationship(type: "HAS_TOOL", direction: OUT)
  hasTransaction: [Transaction!]! @relationship(type: "HAS_TRANSACTION", direction: OUT)
  victimizes: [Product!]! @relationship(type: "VICTIMIZES", direction: OUT)
}
type Subdomain {
  uid: String
  srid: String
  name: String
  subDomainOfDomain: [Domain!]! @relationship(type: "SUBDOMAIN_OF_DOMAIN", direction: OUT)

  hostnameOfIP: [IP!]! @relationship(type: "HOSTNAME_OF_IP", direction: OUT)
  hostnameOfAbuseIP: [AbuseIPLookup!]! @relationship(type: "SUBDOMAIN_OF_ABUSE_IP", direction: OUT)
  subdomainOfThreatCrowdDomain: [ThreatCrowdDomainLookup!]! @relationship(type: "SUBDOMAIN_OF_THREAT_CROWD_DOMAIN", direction: OUT)
  subdomainOfThreatMiner: [ThreatMinerDomainLookup!]! @relationship(type: "SUBDOMAIN_OF_THREAT_MINER_DOMAIN", direction: OUT)
}
type Subnet {
  srid: String
  uid: String
  name: String
  allocation_age: Int
  allocation_date: String
  reputation: Int
  reputation_score: Int
  createdAt: Float
  updatedAt: Float
  density: [Density!]! @relationship(type: "HAS_DENSITY", direction: OUT)
  ip: [IP!]! @relationship(type: "SUBNET_OF", direction: OUT)
}
interface _SubnetRelProperties @relationshipProperties {
  createdAt: Float
  expiredAt: Float
}
type SucuriUrlLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  blacklists: String
  links: String
  ratings: String
  recommendations: String
  scan: String
  site: String
  software: String
  tls: String
  warnings: String

  lookupOf: [URL!]! @relationship(type: "SUCURI_URL_LOOKUP_OF", direction: OUT)
}
type Tactic {
  uid: String
  srid: String
  name: String
  displayName: String
  description: String
  mitreId: String
  tactUsedByMal: [Malware!]! @relationship(type: "TACT_USED_BY_MAL", direction: OUT)
  tactUsedByRan: [Ransom!]! @relationship(type: "TECH_USED_BY_RANSOM", direction: OUT)
  tactUsedByThreat: [ThreatActor!]! @relationship(type: "TACT_USED_BY_THREAT", direction: OUT)
  tactUsedByTool: [Tool!]! @relationship(type: "TACT_USED_BY_TOOL", direction: OUT)
  has: [Technique!]! @relationship(type: "HAS", direction: OUT, properties: "TacticHasTechniques")
  partOf: [Transaction!]! @relationship(type: "PART_OF", direction: OUT)
  tacticOfIp : [IP!]! @relationship(type: "TACTIC_OF", direction: OUT)
  tacticOfUrl : [URL!]! @relationship(type: "TACTIC_OF", direction: OUT)
  tacticOfDomain : [Domain!]! @relationship(type: "TACTIC_OF", direction: OUT)
  tacticOfObject : [Object!]! @relationship(type: "TACTIC_OF", direction: OUT)
}
interface TacticHasTechniques @relationshipProperties {
  sourceSRID: String
  label: String
  uid: String
}


type Tag {
  uid: String
  srid: String
  name: String
  type: String
  description: String

  tagOfIpv6: [IPV6!]! @relationship(type: "TAG_OF_IPV6", direction: OUT, properties: "_TimeProperty")
  sha512Indicator: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT, properties: "_TimeProperty")

  campaignTag: [AttackCampaign!]! @relationship(type: "CAMPAIGN_TAG", direction: OUT)
  tagOf: [IP!]! @relationship(type: "TAG_OF", direction: OUT, properties: "_TimeProperty")
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ssdeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  imphashIndicator: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT)
  vhashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  authentihashIndicator: [AuthentiHash!]! @relationship(type: "AUTHENTIHASH_INDICATOR", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "TAG_OF_URL", direction: OUT, properties: "_TimeProperty")
  cveIndicator: [CVE!]! @relationship(type: "TAG_OF_CVE", direction: OUT, properties: "_TimeProperty")
  fileIndicator: [FileName!]! @relationship(type: "FILE_INDICATOR", direction: OUT)
  tagOfStrike: [Strike!]! @relationship(type: "TAG_OF_STRIKE", direction: OUT)
  tagOfCert: [Cert!]! @relationship(type: "TAG_OF_CERT", direction: OUT)
  tagOfObject: [Object!]! @relationship(type: "TAG_OF_OBJECT", direction: OUT)
  tagOfMalware: [Malware!]! @relationship(type: "TAG_OF_MALWARE", direction: OUT)
  tagOfDomain: [Domain!]! @relationship(type: "TAG_OF_DOMAIN", direction: OUT, properties: "_TimeProperty")
  tagOfUrl: [URL!]! @relationship(type: "TAG_OF_URL", direction: OUT)
  tagOfEmail: [Email!]! @relationship(type: "TAG_OF_EMAIL", direction: OUT, properties: "_TimeProperty")
  relatedToNews: [News!]! @relationship(type: "RELATED_TO_NEWS", direction: OUT)
  tagOfTransaction: [Transaction!]! @relationship(type: "TAG_OF_TRANSACTION", direction: OUT)

  tagOfShodanIP: [ShodanIPLookup!]! @relationship(type: "TAG_OF_SHODAN_IP", direction: OUT)
  tagOfUrlHausUrl: [URLHausURLLookup!]! @relationship(type: "TAG_OF_URL_HAUS_URL", direction: OUT)
  tagOfIBMXForceMD5: [IBMXForceMD5Lookup!]! @relationship(type: "TAG_OF_IBM_XFORCE_MD5", direction: OUT)
  tagOfIBMXForceSHA1: [IBMXForceSHA1Lookup!]! @relationship(type: "TAG_OF_IBM_XFORCE_SHA1", direction: OUT)
  tagOfIBMXForceSHA256: [IBMXForceSHA256Lookup!]! @relationship(type: "TAG_OF_IBM_XFORCE_SHA256", direction: OUT)
  tagOfHybridAnalysisMD5: [HybridAnalysisMD5Lookup!]! @relationship(type: "TAG_OF_HYBRID_ANALYSIS_MD5", direction: OUT)
  tagOfHybridAnalysisSHA1: [HybridAnalysisSHA1Lookup!]! @relationship(type: "TAG_OF_HYBRID_ANALYSIS_SHA1", direction: OUT)
  tagOfHybridAnalysisSHA256: [HybridAnalysisSHA256Lookup!]! @relationship(type: "TAG_OF_HYBRID_ANALYSIS_SHA256", direction: OUT)
  hasAdvisory: [Advisory!]! @relationship(type: "HAS_ADVISORY", direction: OUT, properties: "_TimeProperty")
  patchTuesday: [PatchTuesday!]! @relationship(type: "RELATES_TO", direction: OUT, properties: "_TimeProperty")
}
type TalosDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  categories: String
  daily_mag: Float
  daychange: Float
  domain: String
  entry: String
  is_hostname: Boolean
  monthly_mag: Float
  show: String
  threat_categories: String
  threat_score: String
  web_score: String
  web_score_name: String

  category: [Category!]! @relationship(type: "TALOS_DOMAIN_CATEGORY", direction: OUT)
  lookupOf: [Domain!]! @relationship(type: "TALOS_DOMAIN_LOOKUP_OF", direction: OUT)
}
type TalosIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  blacklists: String
  category: String
  cidr: Boolean
  cities: String
  country: String
  country_code: String
  country_flag: String
  daily_mag: Float
  daily_spam_level: Int
  daily_spam_name: String
  daychange: Float
  display_ipv6_volume: Boolean
  dnsmatch: Int
  domain: String
  email_score: String
  email_score_name: String
  error: String
  hostname: String
  ip: String
  locations: String
  map: String
  monthly_mag: Float
  monthly_spam_level: Int
  monthly_spam_name: String
  organization: String
  web_score: String
  web_score_name: String

  hasCategory: [Category!]! @relationship(type: "TALOS_IP_CATEGORY", direction: OUT)
  hasDomain: [Domain!]! @relationship(type: "TALOS_IP_DOMAIN", direction: OUT)
  lookupOf: [IP!]! @relationship(type: "TALOS_IP_LOOKUP_OF", direction: OUT)
}
type TalosUrlLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  cities: String
  category: String
  country: String
  country_code: String
  country_flag: String
  domain: String
  hostname: String
  locations: String
  map: String
  organization: String
  type: String
  uri: String
  url: String
  web_score: String
  web_score_name: String

  hasCategory: [Category!]! @relationship(type: "TALOS_URL_CATEGORY", direction: OUT)
  hasDomain: [Domain!]! @relationship(type: "TALOS_URL_DOMAIN", direction: OUT)
  lookupOf: [URL!]! @relationship(type: "TALOS_URL_LOOKUP_OF", direction: OUT)
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
  mitigatedBy: [Action!]! @relationship(type: "MITIGATED_BY", direction: OUT)
  techUsedByMal: [Malware!]! @relationship(type: "TECH_USED_BY_MAL", direction: OUT)
  techUsedByRan: [Ransom!]! @relationship(type: "TECH_USED_BY_RANSOM", direction: OUT)
  requires: [Permission!]! @relationship(type: "REQUIRES", direction: OUT)
  techExploits: [Platform!]! @relationship(type: "TECH_EXPLOITS", direction: OUT)
  partOf: [Tactic!]! @relationship(type: "PART_OF", direction: OUT, properties: "TacticHasTechniques")
  techUsedByTool: [Tool!]! @relationship(type: "TECH_USED_BY_TOOL", direction: OUT)
  techUsedByThreat: [ThreatActor!]! @relationship(type: "TECH_USED_BY_THREAT", direction: OUT)
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  techniqueOfIp : [IP!]! @relationship(type: "TECHNIQUE_OF", direction: OUT)
  subTechniqueIp : [IP!]! @relationship(type: "SUB_TECHNIQUE_OF", direction: OUT)
  techniqueOfUrl : [URL!]! @relationship(type: "TECHNIQUE_OF", direction: OUT)
  subTechniqueUrl : [URL!]! @relationship(type: "SUB_TECHNIQUE_OF", direction: OUT)
  techniqueOfDomain : [Domain!]! @relationship(type: "TECHNIQUE_OF", direction: OUT)
  subTechniqueDomain : [Domain!]! @relationship(type: "SUB_TECHNIQUE_OF", direction: OUT)
  techniqueOfObject : [Object!]! @relationship(type: "TECHNIQUE_OF", direction: OUT)
  subTechniqueObject : [Object!]! @relationship(type: "SUB_TECHNIQUE_OF", direction: OUT)
  hasSubTechnique: [Technique!]! @relationship(type: "HAS_SUB_TECHNIQUE", direction: OUT)
  subTechniqueOf: [Technique!]! @relationship(type: "SUB_TECHNIQUE_OF", direction: OUT)
}
type TelfHash {
  name: String
  srid: String
  uid: String

  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  ofObject: [Object!]! @relationship(type: "TELFHASH_OF_OBJECT", direction: OUT, properties: "_TimeProperty")
}
type TLSH {
  name: String
  srid: String
  uid: String
  createdAt: Float
  updatedAt: Float

  ofObject: [Object!]! @relationship(type: "TLSH_OF_OBJECT", direction: OUT, properties: "_TimeProperty")
}
type TLD {
  name: String
  srid: String
  uid: String
  createdAt: Float
  updatedAt: Float
  domain: [Domain!]! @relationship(type: "TLD_OF",direction: OUT)
}
type ThreatActor {
  uid: String
  srid: String
  srDescription: String
  name: String
  description: String
  originCountry: String
  incidentType: String
  sectors: String
  suspectedVictims: String
  vendor: String
  refs: String
  alias: String
  tools: String
  targetCategory: String

  ipv6Indicator: [IPV6!]! @relationship(type: "IPV6_INDICATOR", direction: OUT, properties: "_TimeProperty")
  emailIndicator: [Email!]! @relationship(type: "EMAIL_INDICATOR", direction: OUT, properties: "_TimeProperty")

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  hasAlias: [ActorAlias!]! @relationship(type: "HAS_ALIAS", direction: OUT)
  relates: [ActorAlias!]! @relationship(type: "RELATES", direction: OUT)
  actorCreated: [ActorCreated!]! @relationship(type: "ACTOR_CREATED", direction: OUT)
  actorModified: [ActorModified!]! @relationship(type: "ACTOR_MODIFIED", direction: OUT)
  motivatedBy: [Agenda!]! @relationship(type: "MOTIVATED_BY", direction: OUT)
  hasCampaign: [AttackCampaign!]! @relationship(type: "HAS_CAMPAIGN", direction: OUT)
  authentihashIndicator: [AuthentiHash!]! @relationship(type: "AUTHENTIHASH_INDICATOR", direction: OUT)
  sponsoredBy: [Country!]! @relationship(type: "SPONSORED_BY", direction: OUT)
  targets: [Country!]! @relationship(type: "TARGETS", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT, properties: "_TimeProperty")
  fileIndicator: [FileName!]! @relationship(type: "FILE_INDICATOR", direction: OUT)
  imphashIndicator: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT, properties: "_TimeProperty")
  threatUsesMal: [Malware!]! @relationship(type: "THREAT_USES_MAL", direction: OUT)
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT, properties: "_TimeProperty")
  targetsRegion: [Region!]! @relationship(type: "TARGETS_REGION", direction: OUT)
  targetsSector: [Sector!]! @relationship(type: "TARGETS_SECTOR", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha512Indicator: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ssdeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  partOfStrike: [Strike!]! @relationship(type: "PART_OF_STRIKE", direction: OUT)
  threatUsesTact: [Tactic!]! @relationship(type: "THREAT_USES_TACT", direction: OUT)
  threatUsesTech: [Technique!]! @relationship(type: "THREAT_USES_TECH", direction: OUT)
  threatUsesTool: [Tool!]! @relationship(type: "THREAT_USES_TOOL", direction: OUT)
  partOfTransaction: [Transaction!]! @relationship(type: "PART_OF_TRANSACTION", direction: OUT)
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT, properties: "_TimeProperty")
  vhashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  threatUsesRansom: [Ransom!]! @relationship(type: "THREAT_USES_RANSOM", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  targetsIndustry: [Industry!]! @relationship(type: "TARGETS_INDUSTRY", direction: OUT)
  usedByObject: [Object!]! @relationship(type: "USED_BY_OBJECT", direction: OUT)
  cveIndicator: [CVE!]! @relationship(type: "INDICATES_CVE",direction: OUT)
}
type ThreatCrowdDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  emails: String
  hashes: String
  permalink: String
  references: String
  resolutions: String
  response_code: String
  subdomains: String
  votes: Int

  hasEmail: [Email!]! @relationship(type: "THREAT_CROWD_DOMAIN_EMAIL", direction: OUT)
  hasMd5: [MD5!]! @relationship(type: "THREAT_CROWD_DOMAIN_MD5", direction: OUT)
  lookupOf: [Domain!]! @relationship(type: "THREAT_CROWD_DOMAIN_LOOKUP_OF", direction: OUT)
  hasResolution: [Resolution!]! @relationship(type: "THREAT_CROWD_DOMAIN_RESOLUTION", direction: OUT)
  hasSubdomain: [Subdomain!]! @relationship(type: "THREAT_CROWD_DOMAIN_SUBDOMAIN", direction: OUT)
}
type ThreatCrowdMD5Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  domains: String
  ips: String
  md5: String
  permalink: String
  references: String
  response_code: String
  scans: String
  sha1: String

  hasDomain: [Domain!]! @relationship(type: "HAS_DOMAIN", direction: OUT)
  hasIP: [IP!]! @relationship(type: "HAS_IP", direction: OUT)
  lookupOfMD5: [MD5!]! @relationship(type: "THREAT_CROWD_MD5_LOOKUP_OF", direction: OUT)
  lookupOfSHA1: [SHA1!]! @relationship(type: "THREAT_CROWD_SHA1_LOOKUP_OF", direction: OUT)
}
type ThreatCrowdIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  permalink: String
  references: String
  response_code: String
  votes: Int

  hasMD5: [MD5!]! @relationship(type: "THREAT_CROWD_IP_MD5", direction: OUT)
  hasResolutions: [Resolution!]! @relationship(type: "THREAT_CROWD_IP_RESOLUTION", direction: OUT)
  lookupOf: [IP!]! @relationship(type: "THREAT_CROWD_IP_LOOKUP_OF", direction: OUT)
}
type ThreatMinerDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  associate_urls: String
  passive_dns: String
  related_samples: String
  subdomains: String
  whois: String
  results: String

  lookupOf: [Domain!]! @relationship(type: "THREAT_MINER_DOMAIN_LOOKUP_OF", direction: OUT)
  hasPassiveDNS: [PassiveDNS!]! @relationship(type: "THREAT_MINER_DOMAIN_PASSIVE_DNS", direction: OUT)
  hasSubdomain: [Subdomain!]! @relationship(type: "THREAT_MINER_DOMAIN_SUBDOMAIN", direction: OUT)
}
type ThreatMinerIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  related_samples: String
  ssl_cert: String
  whois: String
  uri: String

  lookupOf: [IP!]! @relationship(type: "THREAT_MINER_IP_LOOKUP_OF", direction: OUT)
  passiveDNS: [PassiveDNS!]! @relationship(type: "THREAT_MINER_IP_PASSIVE_DNS", direction: OUT)
}
type Tool {
  uid: String
  srid: String
  name: String
  description: String
  mitreId: String
  version: String
  refs: String
  alias: String
  platform: String

  ipv6Indicator: [IPV6!]! @relationship(type: "IPV6_INDICATOR", direction: OUT, properties: "_TimeProperty")
  domainIndicator: [Domain!]! @relationship(type: "DOMAIN_INDICATOR", direction: OUT, properties: "_TimeProperty")
  emailIndicator: [Email!]! @relationship(type: "EMAIl_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha512Indicator: [SHA512!]! @relationship(type: "SHA512_INDICATOR", direction: OUT, properties: "_TimeProperty")
  urlIndicator: [URL!]! @relationship(type: "URL_INDICATOR", direction: OUT, properties: "_TimeProperty")

  campaignUsesTool: [AttackCampaign!]! @relationship(type: "CAMPAIGN_USES_TOOL", direction: OUT)
  authentihashIndicator: [AuthentiHash!]! @relationship(type: "AUTHENTIHASH_INDICATOR", direction: OUT)
  toolCreated: [Created!]! @relationship(type: "TOOL_CREATED", direction: OUT)
  fileIndicator: [FileName!]! @relationship(type: "FILE_INDICATOR", direction: OUT)
  imphashIndicator: [ImpHash!]! @relationship(type: "IMPHASH_INDICATOR", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "IP_INDICATOR", direction: OUT, properties: "_TimeProperty")
  md5Indicator: [MD5!]! @relationship(type: "MD5_INDICATOR", direction: OUT, properties: "_TimeProperty")
  toolModified: [Modified!]! @relationship(type: "TOOL_MODIFIED", direction: OUT)
  toolExploits: [Platform!]! @relationship(type: "TOOL_EXPLOITS", direction: OUT)
  sha1Indicator: [SHA1!]! @relationship(type: "SHA1_INDICATOR", direction: OUT, properties: "_TimeProperty")
  sha256Indicator: [SHA256!]! @relationship(type: "SHA256_INDICATOR", direction: OUT, properties: "_TimeProperty")
  ssdeepIndicator: [SSDeep!]! @relationship(type: "SSDEEP_INDICATOR", direction: OUT)
  toolUsesTact: [Tactic!]! @relationship(type: "TOOL_USES_TACT", direction: OUT)
  toolUsesTech: [Technique!]! @relationship(type: "TOOL_USES_TECH", direction: OUT)
  hasCampaign: [AttackCampaign!]! @relationship(type: "HAS_CAMPAIGN", direction: OUT)
  toolUsedByThreat: [ThreatActor!]! @relationship(type: "TOOL_USED_BY_THREAT", direction: OUT)
  hasAlias: [ToolAlias!]! @relationship(type: "HAS_ALIAS", direction: OUT)
  vhashIndicator: [VHash!]! @relationship(type: "VHASH_INDICATOR", direction: OUT)
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  toolSponsoredBy: [Country!]! @relationship(type: "TOOL_SPONSORED_BY", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  usedByObject: [Object!]! @relationship(type: "USED_BY_OBJECT", direction: OUT)
  partOfStrike: [Strike!]! @relationship(type: "PART_OF_STRIKE", direction: OUT)
  cveIndicator: [CVE!]! @relationship(type: "INDICATES_CVE",direction: OUT)
}
type ToolAlias {
  name: String
  uid: String
  displayName: String
  srid: String
  aliasOf: [Tool!]! @relationship(type: "ALIAS_OF", direction: OUT)
}
type TorNodeIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  ExitAddress: String
  ExitNode: String
  LastStatus: String
  Published: String

  lookupOf: [IP!]! @relationship(type: "TOR_NODE_IP_LOOKUP_OF", direction: OUT)
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
  indicatesAuthentiHash: [AuthentiHash!]! @relationship(type: "INDICATES_AUTHENTIHASH", direction: OUT)
  categories: [Category!]! @relationship(type: "CATEGORY", direction: OUT)
  exploitsCVE: [CVE!]! @relationship(type: "EXPLOITS_CVE", direction: OUT)
  hasFile: [FileName!]! @relationship(type: "HAS_FILE", direction: OUT)
  indicatesImpHash: [ImpHash!]! @relationship(type: "INDICATES_IMPHASH", direction: OUT)
  hasIP: [IP!]! @relationship(type: "HAS_IP", direction: OUT)
  hasMalware: [Malware!]! @relationship(type: "HAS_MALWARE", direction: OUT)
  indicatesMD5: [MD5!]! @relationship(type: "INDICATES_MD5", direction: OUT)
  hasMitigation: [Mitigation!]! @relationship(type: "HAS_MITIGATION", direction: OUT)
  targetsPlatform: [Platform!]! @relationship(type: "TARGETS_PLATFORM", direction: OUT)
  indicatesSHA1: [SHA1!]! @relationship(type: "INDICATES_SHA1", direction: OUT)
  indicatesSHA256: [SHA256!]! @relationship(type: "INDICATES_SHA256", direction: OUT)
  indicatesSSDeep: [SSDeep!]! @relationship(type: "INDICATES_SSDEEP", direction: OUT)
  hasStage: [Stage!]! @relationship(type: "HAS_STAGE", direction: OUT)
  partOf: [Strike!]! @relationship(type: "PART_OF", direction: OUT)
  hasTactic: [Tactic!]! @relationship(type: "HAS_TACTIC", direction: OUT)
  hasActor: [ThreatActor!]! @relationship(type: "HAS_ACTOR", direction: OUT)
  hasTool: [Tool!]! @relationship(type: "HAS_TOOL", direction: OUT)
  hasUrl: [URL!]! @relationship(type: "HAS_URL", direction: OUT)
  indicatesVHash: [VHash!]! @relationship(type: "INDICATES_VHASH", direction: OUT)
  tags: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  usesRansom: [Ransom!]! @relationship(type: "USES_RANSOM", direction: OUT)
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
}

type Trendsv2 @node(label: "Trend") {
  uid: String
  srid: String
  name: String
  entity: String
  score: Int
  createdAt: Float
  updatedAt: Float
}

type Trends {
  uid: String
  srid: String
  name: String
  malware: String
  threatActor: String

  malwareTrends: [MalwareAlias!]! @relationship(type: "MALWARE_TRENDS", direction: OUT)
  toolTrends: [ToolAlias!]! @relationship(type: "TOOL_TRENDS", direction: OUT)
  ransomTrends: [RansomAlias!]! @relationship(type: "RANSOM_TRENDS", direction: OUT)
  threatTrends: [ActorAlias!]! @relationship(type: "THREAT_TRENDS", direction: OUT)
}

type Tweet {
  name: String
  screenName: String
  userid: String
  retweetCount: String
  date: String
  statusid: String
  tweetUrl: String
  description: String
  hashtags: String
  cveNumbers: String
  domains: String
  urls: String
  md5: String
  sha1: String
  sha256: String
  email: String
  ip4: String
  retweetTrack: String
  ioc: String
  ActorName: String
  MalwareName: String
  ToolName: String
  RansomName: String
  srid: String
  uid: String
  tweetBy: [UserTwitter!]! @relationship(type: "TWEET_BY", direction: OUT)
  relatedActor: [ThreatActor!]! @relationship(type: "RELATED_ACTOR", direction: OUT)
  relatedMalware: [Malware!]! @relationship(type: "RELATED_MALWARE", direction: OUT)
  relatedTool: [Tool!]! @relationship(type: "RELATED_TOOL", direction: OUT)
  relatedRansom: [Ransom!]! @relationship(type: "RELATED_RANSOM", direction: OUT)
  hasMD5: [MD5!]! @relationship(type: "HAS_MD5", direction: OUT)
  hasSHA1: [SHA1!]! @relationship(type: "HAS_SHA1", direction: OUT)
  hasSHA256: [SHA256!]! @relationship(type: "HAS_SHA256", direction: OUT)
  hasIP: [IP!]! @relationship(type: "HAS_IP", direction: OUT)
  hasURL: [URL!]! @relationship(type: "HAS_URL", direction: OUT)
  hasDomain: [Domain!]! @relationship(type: "HAS_DOMAIN", direction: OUT)
}
type URL {
  name: String
  uid: String
  srid: String
  updatedAt: Float
  createdAt: Float
  score: Int
  confidence: String
  firstSeen: Float
  lastSeen: Float
  isPhishing: Boolean
  verdict: String
  approved: Boolean
  fp: Boolean

  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_SourceRelProperties")
  hasStatus: [Status!]! @relationship(type: "HAS_STATUS", direction: OUT, properties: "_StatusRelProperties")
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  urlOfRansom: [Ransom!]! @relationship(type: "URL_OF_RANSOM", direction: OUT, properties: "_TimeProperty")
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT, properties: "_TimeProperty")
  registrarUrl: [Registrar!]! @relationship(type: "URL_OF", direction: OUT)
  hasTactic : [Tactic!]! @relationship(type: "HAS_TACTIC", direction: OUT)
  hasTechnique : [Technique!]! @relationship(type: "HAS_TECHNIQUE", direction: OUT)
  hasSubTechnique : [Technique!]! @relationship(type: "HAS_SUB_TECHNIQUE", direction: OUT)
  urlTargetSector: [Sector!]! @relationship(type: "SECTOR_TARGETED_BY_URL", direction: OUT)
  associatedCampaign: [AttackCampaign!]! @relationship(type: "INDICATES_CAMPAIGN", direction: OUT)
  targetCountry: [Country!]! @relationship(type: "TARGETED_COUNTRY", direction: OUT)
  targetIndustry: [Industry!]! @relationship(type: "INDUSTRY_TARGETED_BY_URL", direction: OUT)

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  hasTweets: [Tweet!]! @relationship(type: "HAS_TWEETS", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
  hasCategory: [Category!]! @relationship(type: "HAS_CATEGORY", direction: OUT)
  hasPayload: [Payload!]! @relationship(type: "HAS_PAYLOAD", direction: OUT)
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  indicatesTransaction: [Transaction!]! @relationship(type: "INDICATOR_OF_URL", direction: OUT)
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT, properties: "_TimeProperty")
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT, properties: "_TimeProperty")
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT, properties: "_TimeProperty")
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT, properties: "_TimeProperty")
  indicatesCert: [Cert!]! @relationship(type: "INDICATES_CERT", direction: OUT)
  indicatesEmail: [Email!]! @relationship(type: "INDICATES_EMAIL", direction: OUT)
  communicatedByObject: [Object!]! @relationship(type: "COMMUNICATED_BY_OBJECT", direction: OUT)
  downloadsObject: [Object!]! @relationship(type: "DOWNLOADS_OBJECT", direction: OUT)
  relatedTo: [URLList!]! @relationship(type: "RELATED_TO", direction: OUT)
  childUrlOfDomain: [Domain!]! @relationship(type: "CHILD_URL_OF_DOMAIN", direction: OUT)
  urlOfDomain: [Domain!]! @relationship(type: "URL_OF_DOMAIN", direction: OUT)
  mentionedInNews: [News!]! @relationship(type: "MENTIONED_IN_NEWS", direction: OUT)
  shortens: [URL!]! @relationship(type: "SHORTENS", direction: OUT)
  shortenedBy: [URL!]! @relationship(type: "SHORTENED_BY", direction: OUT)
  whoIsIndicator: [WhoIs!]! @relationship(type: "REFERRAL_URL_OF",direction: OUT)
  hasVulnerability: [Vulnerability!]! @relationship(type: "HAS_VULNERABILITY", direction: OUT)
  hasAnalysis: [Analysis!]! @relationship(type: "HAS_ANALYSIS", direction: OUT, properties: "_TimeProperty")
  hasIpHost: [IP!]! @relationship(type: "HAS_HOST", direction: OUT)
  hasDomainHost: [Domain!]! @relationship(type: "HAS_HOST", direction: OUT)
  hasPort: [Port!]! @relationship(type: "HAS_PORT", direction: OUT, properties: "_PortType")
  urlCategory: [Category!]! @relationship(type: "HAS_CATEGORY",direction: OUT)
  urlAssociatedWithIp : [IP!]! @relationship(type: "URL_OF_IP", direction: OUT, properties: "_TimeProperty")
  bodyPartsOfUrl: [URL!]! @relationship(type: "PART_OF", direction: OUT)
  urlHasBodyParts: [URL!]! @relationship(type: "HAS_PART", direction: OUT)
  alienVaultUrlLookUp: [AlienVaultUrlLookup!]! @relationship(type: "ALIEN_VAULT_URL_LOOKUP", direction: OUT)
  checkPhishUrlScan: [CheckPhishUrlScan!]! @relationship(type: "CHECK_PHISH_URL_SCAN", direction: OUT)
  gsbUrlLookup: [GSBUrlLookup!]! @relationship(type: "GSB_URL_LOOKUP", direction: OUT)
  ibmXForceURLLookup: [IBMXForceURLLookup!]! @relationship(type: "IBM_XFORCE_URL_LOOKUP", direction: OUT)
  opswatUrlLookup: [OPSWATUrlLookup!]! @relationship(type: "OPSWAT_URL_LOOKUP", direction: OUT)
  phishTankUrlLookup: [PhishTankUrlLookup!]! @relationship(type: "PHISH_TANK_URL_LOOKUP", direction: OUT)
  pulseDiveUrlLookup: [PulseDiveUrlLookup!]! @relationship(type: "PULSE_DIVE_URL_LOOKUP", direction: OUT)
  sucuriUrlLookup: [SucuriUrlLookup!]! @relationship(type: "SUCURI_URL_LOOKUP", direction: OUT)
  talosUrlLookup: [TalosUrlLookup!]! @relationship(type: "TALOS_URL_LOOKUP", direction: OUT)
  urlHausURLLookup: [URLHausURLLookup!]! @relationship(type: "URL_HAUS_URL_LOOKUP", direction: OUT)
  virusTotalUrlLookup: [VirusTotalUrlLookup!]! @relationship(type: "VIRUS_TOTAL_URL_LOOKUP", direction: OUT)
  webpluseURLLookup: [WebpluseURLLookup!]! @relationship(type: "WEBPULSE_URL_LOOKUP", direction: OUT)
  urlScanLookup: [URLScanLookup!]! @relationship(type: "URL_SCAN", direction: OUT)
  urlStatus: [URLStatus!]! @relationship(type: "URL_STATUS", direction: OUT)
  httpResponse: [HttpResponse!]! @relationship(type: "HAS_RESPONSE", direction: OUT)
}
type URLHausDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  blacklists: String
  firstseen: String
  host: String
  query_status: String
  urlhaus_reference: String
  urls: String
  url_count: String

  lookupOf: [Domain!]! @relationship(type: "URL_HAUS_DOMAIN_LOOKUP_OF", direction: OUT)
  hasUrl: [URLList!]! @relationship(type: "URL_HAUS_DOMAIN_URL", direction: OUT)
}
type URLHausMD5Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  file_size: String
  file_type: String
  firstseen: String
  imphash: String
  lastseen: String
  md5_hash: String
  query_status: String
  sha256_hash: String
  signature: String
  ssdeep: String
  tlsh: String
  urlhaus_download: String
  url_count: String
  url_list: String
  virustotal: String

  hasSha256: [SHA256!]! @relationship(type: "HAS_SHA256", direction: OUT)
  lookupOf: [MD5!]! @relationship(type: "URL_HAUS_MD5_LOOKUP_OF", direction: OUT)
  urls: [URLList!]! @relationship(type: "URL_HAUS_MD5_URL", direction: OUT)
}
type URLHausSHA256Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  file_size: String
  file_type: String
  firstseen: String
  imphash: String
  lastseen: String
  md5_hash: String
  query_status: String
  sha256_hash: String
  signature: String
  ssdeep: String
  tlsh: String
  urlhaus_download: String
  url_count: String
  url_list: String
  virustotal: String

  hasMd5: [MD5!]! @relationship(type: "HAS_MD5", direction: OUT)
  lookupOf: [SHA256!]! @relationship(type: "URL_HAUS_SHA256_LOOKUP_OF", direction: OUT)
  urls: [URLList!]! @relationship(type: "URL_HAUS_SHA256_URL", direction: OUT)
}
type URLHausURLLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  blacklists: String
  date_added: String
  host: String
  id: String
  larted: String
  payloads: String
  query_status: String
  reporter: String
  tags: String
  takedown_time_seconds: String
  threat: String
  url: String
  url_status: String
  urlhaus_reference: String

  lookupOf: [URL!]! @relationship(type: "URL_HAUS_URL_LOOKUP_OF", direction: OUT)
  hasPayload: [Payload!]! @relationship(type: "URL_HAUS_URL_PAYLOAD", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "URL_HAUS_URL_TAG", direction: OUT)
}
type Payload {
  uid: String
  srid: String
  filename: String
  file_type: String
  firstseen: String
  imphash: String
  response_size: String
  response_md5: String
  response_sha256: String
  signature: String
  ssdeep: String
  tlsh: String
  urlhaus_download: String
  virustotal: String

  payloadOfUrl: [URL!]! @relationship(type: "PAYLOAD_OF_URL", direction: OUT)
  payloadOfUrlHausUrl: [URLHausURLLookup!]! @relationship(type: "PAYLOAD_OF_URL_HAUS_URL", direction: OUT)
}
type URLList {
  uid: String
  srid: String
  date: String
  domain: String
  encoded: String
  gsb: String
  hostname: String
  httpcode: Int
  result: String
  url: String
  checked: Int
  deep_analysis: Boolean
  params: String
  secs: Float
  ip: String
  uri: String
  date_added: String
  id: Int
  larted: Boolean
  reporter: String
  tags: String
  takedown_time_seconds: Int
  threat: String
  url_status: String
  urlhaus_reference: String
  url_id: String
  filename: String
  firstseen: String
  lastseen: String

  relatedToURL: [URL!]! @relationship(type: "RELATED_TO", direction: OUT)

  urlOfAlienVaultDomain: [AlienVaultDomainLookup!]! @relationship(type: "URL_OF_ALIEN_VAULT_DOMAIN_LOOKUP", direction: OUT)
  urlOfURLHausDomain: [URLHausDomainLookup!]! @relationship(type: "URL_OF_URL_HAUS_DOMAIN", direction: OUT)

  urlOfUrlHausMD5: [URLHausMD5Lookup!]! @relationship(type: "URL_OF_URL_HAUS_MD5", direction: OUT)
  urlOfUrlHausSHA256: [URLHausSHA256Lookup!]! @relationship(type: "URL_OF_URL_HAUS_SHA256", direction: OUT)
  urlOfAlienVaultUrl: [AlienVaultUrlLookup!]! @relationship(type: "URL_OF_ALIEN_VAULT_URL", direction: OUT)
}
type URLScanLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  response: String

  lookupOf: [URL!]! @relationship(type: "URL_SCAN_OF", direction: OUT)
}
type URLStatus {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  final_url: String
  response_headers: String
  response_history: String
  status_code: Int

  statusOf: [URL!]! @relationship(type: "STATUS_OF_URL", direction: OUT)
}
type UserTwitter {
  name: String
  userid: String
  srid: String
  uid: String
  tweets: [Tweet!]! @relationship(type: "TWEETS", direction: OUT)
}
type Vendor {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  displayName: String
  description: String
  category: String
  version: String
  locations: String
  headquarters: String
  integrationName: String
  cve: [CVE!]! @relationship(type: "RELATES_CVE", direction: OUT)
  hasCve: [CVE!]! @relationship(type: "HAS_CVE", direction: OUT, properties: "_TimeProperty")
  hasProduct: [Product!]! @relationship(type: "HAS_PRODUCT", direction: OUT, properties: "_TimeProperty")
  providesProduct: [Product!]! @relationship(type: "PROVIDES", direction: OUT)
  usesProduct: [Product!]! @relationship(type: "USES", direction: OUT)
  maintainsProduct: [Product!]! @relationship(type: "MAINTAINS", direction: OUT)
  compromisedByProduct: [Product!]! @relationship(type: "COMPROMISED_DUE_TO", direction: OUT)
}
type Version {
  uid: String
  srid: String
  name: String
  updatedAt: Float
  createdAt: Float
  product: String
  start_version: Float
  is_range: Boolean
  end_version: Float
  cve: [CVE!]! @relationship(type: "RELATES_CVE", direction: OUT, properties: "_TimeProperty")
  hasOperator: [Operator!]! @relationship(type: "HAS_OPERATOR", direction: OUT, properties: "_TimeProperty")
  hasProduct: [Product!]! @relationship(type: "HAS_PRODUCT", direction: OUT, properties: "_TimeProperty")
  fixOf: [CVE!]! @relationship(type: "FIX_OF", direction: OUT, properties: "_TimeProperty")
}
type VHash {
  name: String
  srid: String
  uid: String

  actionIndicator: [IndicatorOfAction!]! @relationship(type: "ACTION_INDICATOR", direction: OUT)
  vhashOfRansom: [Ransom!]! @relationship(type: "VHASH_OF_RANSOM", direction: OUT)
  partOf: [Stage!]! @relationship(type: "PART_OF", direction: OUT)
  indicatorOfVHASH: [Transaction!]! @relationship(type: "INDICATOR_OF_VHASH", direction: OUT)
  hasTag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT)
  indicatesAttackCampaign: [AttackCampaign!]! @relationship(type: "INDICATES_ATTACK_CAMPAIGN", direction: OUT)
  indicatesMalware: [Malware!]! @relationship(type: "INDICATES_MALWARE", direction: OUT)
  indicatesStrike: [Strike!]! @relationship(type: "INDICATES_STRIKE", direction: OUT)
  indicatesTool: [Tool!]! @relationship(type: "INDICATES_TOOL", direction: OUT)
  indicatesActor: [ThreatActor!]! @relationship(type: "INDICATES_ACTOR", direction: OUT)
  indicatesMitigation: [Mitigation!]! @relationship(type: "INDICATES_MITIGATION", direction: OUT)
  indicatesCve: [CVE!]! @relationship(type: "INDICATES_CVE", direction: OUT, properties: "_TimeProperty")
  indicatesObject: [Object!]! @relationship(type: "INDICATES_OBJECT", direction: OUT)
  ofObject: [Object!]! @relationship(type: "VHASH_OF_OBJECT", direction: OUT, properties: "_TimeProperty")
}
type VirusTotalDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  data: String

  lookupOf: [Domain!]! @relationship(type: "VIRUS_TOTAL_DOMAIN_LOOKUP_OF", direction: OUT)
}
type VirusTotalMD5Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  md5: String
  permalink: String
  positives: Int
  resource: String
  response_code: Int
  scans: String
  scan_date: String
  scan_id: String
  sha1: String
  sha256: String
  total: Int
  verbose_msg: String

  lookupOfMD5: [MD5!]! @relationship(type: "VIRUS_TOTAL_MD5_LOOKUP_OF", direction: OUT)
  hasSha1: [SHA1!]! @relationship(type: "HAS_SHA1", direction: OUT)
  hasSha256: [SHA256!]! @relationship(type: "HAS_SHA256", direction: OUT)
}
type VirusTotalIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  data: String

  lookupOf: [IP!]! @relationship(type: "VIRUS_TOTAL_IP_LOOKUP_OF", direction: OUT)
}
type VirusTotalSHA1Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  md5: String
  permalink: String
  positives: Int
  resource: String
  response_code: Int
  scans: String
  scan_date: String
  scan_id: String
  sha1: String
  sha256: String
  total: Int
  verbose_msg: String

  hasMd5: [MD5!]! @relationship(type: "HAS_MD5", direction: OUT)
  lookupOfSHA1: [SHA1!]! @relationship(type: "VIRUS_TOTAL_SHA1_LOOKUP_OF", direction: OUT)
  hasSha256: [SHA256!]! @relationship(type: "HAS_SHA256", direction: OUT)
}
type VirusTotalUrlLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  data: String

  lookupOf: [URL!]! @relationship(type: "VIRUS_TOTAL_URL_LOOKUP_OF", direction: OUT)
}
type VirusTotalSHA256Lookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  md5: String
  permalink: String
  positives: Int
  resource: String
  response_code: Int
  scans: String
  scan_date: String
  scan_id: String
  sha1: String
  sha256: String
  total: Int
  verbose_msg: String

  hasMd5: [MD5!]! @relationship(type: "HAS_MD5", direction: OUT)
  hasSha1: [SHA1!]! @relationship(type: "HAS_SHA1", direction: OUT)
  lookupOfSHA256: [SHA256!]! @relationship(type: "VIRUS_TOTAL_SHA256_LOOKUP_OF", direction: OUT)
}
type WebpluseURLLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  categorization: String
  curTrackingId: Int
  linkable: Boolean
  locked: Boolean
  lockedMessage: String
  lockedSpecialNote: String
  multiple: Boolean
  rateDate: String
  ratingDts: String
  ratingDtsCutoff: Int
  resolvedDetail: String
  securityCategory: Boolean
  securityCategoryIds: String
  threatriskLevel: String
  threatriskLevelEn: String
  translatedCategories: String
  unrated: Boolean
  url: String

  lookupOf: [URL!]! @relationship(type: "WEBPULSE_URL_LOOKUP_OF", direction: OUT)
}

type WhoIs {
  hash_value: String
  address: String
  city: String
  country: String
  createdAt: Float
  updatedAt: Float
  creation_date: String
  domain_name: String
  expiration_date: String
  name: String
  org: String
  registrar: String
  sha_256: String
  srid: String
  state: String
  uid: String
  updated_date: String
  whois_server: String
  zipcode: String
  hasEmail: [Email!]! @relationship(type: "HAS_EMAIL", direction: OUT)
  domainIndicator: [Domain!]! @relationship(type: "WHOIS_OF", direction: OUT)
  ipIndicator: [IP!]! @relationship(type: "WHOIS_OF", direction: OUT)
  fromCountry: [Country!]! @relationship(type: "FROM_COUNTRY", direction: OUT)
  fromCity: [City!]! @relationship(type: "FROM_CITY", direction: OUT)
  registrarIndicator: [Registrar!]! @relationship(type: "HAS_REGISTRAR", direction: OUT)
  hasNameserver: [Nameserver!]! @relationship(type: "HAS_NAMESERVER", direction: OUT)
  referralUrl: [URL!]!@relationship(type: "HAS_REFERRAL_URL", direction: OUT)
  reverseDns : [Domain!]! @relationship(type: "HAS_REVERSE_DNS",direction: OUT)
  hasDomain: [Domain!]! @relationship(type: "HAS_DOMAIN", direction: OUT)
}

type WhoIsDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  address: String
  city: String
  country: String
  creation_date: String
  dnssec: String
  domain_name: String
  expiration_date: String
  name: String
  name_servers: String
  org: String
  registrar: String
  state: String
  updated_date: String
  whois_server: String
  zipcode: String

  hasAddress: [Address!]! @relationship(type: "HAS_ADDRESS", direction: OUT)
  fromCountry: [Country!]! @relationship(type: "FROM_COUNTRY", direction: OUT)
  hasDNSSEC: [DNSSEC!]! @relationship(type: "HAS_DNSSEC", direction: OUT)
  lookupOf: [Domain!]! @relationship(type: "WHO_IS_DOMAIN_LOOKUP_OF", direction: OUT)
  hasRegistrar: [Registrar!]! @relationship(type: "WHO_IS_DOMAIN_REGISTRAR", direction: OUT)
}
type WhoIsIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  country: String
  cidr0_cidrs: String
  endAddress: String
  entities: String
  events: String
  handle: String
  ipVersion: String
  links: String
  name: String
  notices: String
  objectClassName: String
  port43: String
  rdapConformance: String
  remarks: String
  startAddress: String
  type: String

  lookupOf: IP @relationship(type: "WHO_IS_IP_LOOKUP_OF", direction: OUT)
}
type ZScalerDomainLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  category: String

  lookupOf: Domain @relationship(type: "Z_SCALER_DOMAIN_LOOKUP_OF", direction: OUT)
}
type ZScalerIPLookup {
  uid: String
  srid: String
  _name: String
  sr_label: String
  sr_description: String
  engine_verdict_score: Int
  category: String

  lookupOf: IP @relationship(type: "Z_SCALER_IP_LOOKUP_OF", direction: OUT)
}

type Advisory {
  name: String
  description: String
  uid: String
  srid: String
  createdAt: Float
  updatedAt: Float
  hasCve: [CVE!]! @relationship(type: "HAS_CVE", direction: OUT, properties: "_TimeProperty")
  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_TimeProperty")
  mentionedInNews: [News!]! @relationship(type: "HAS_NEWS", direction: OUT, properties: "_TimeProperty")
  hasRef: [Reference!]! @relationship(type: "HAS_REF", direction: OUT, properties: "_TimeProperty")
  tag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
}

type PatchTuesday {
  date: Float
  publiclyExposed: Int
  critical: Int
  description: String
  medium: Int
  noSeverity: Int
  srid: String
  createdAt: Float
  updatedAt: Float
  uid: String
  total: Int
  high: Int
  low: Int
  name: String
  exploitedInWild: Int
  case: [Case] @computed(from: ["srid", "cves"])

  cves: [String] @cypher(statement: "MATCH (this)-[:HAS_CVE]->(cve:CVE) RETURN COLLECT(cve.name)")
  hasCve: [CVE!]! @relationship(type: "HAS_CVE", direction: OUT, properties: "_TimeProperty")
  hasSource: [Source!]! @relationship(type: "HAS_SOURCE", direction: OUT, properties: "_TimeProperty")
  mentionedInNews: [News!]! @relationship(type: "HAS_NEWS", direction: OUT, properties: "_TimeProperty")
  vulnerabilityType: [VulnerabilityType!]! @relationship(type: "HAS_THREAT", direction: OUT, properties: "_TimeProperty")
  hasRef: [Reference!]! @relationship(type: "HAS_REFERENCE", direction: OUT, properties: "_TimeProperty")
  tag: [Tag!]! @relationship(type: "HAS_TAG", direction: OUT, properties: "_TimeProperty")
}

type VulnerabilityType {
  name: String
  uid: String
  srid: String
  createdAt: Float
  updatedAt: Float
  hasCve: [CVE!]! @relationship(type: "HAS_CVE", direction: OUT, properties: "_TimeProperty")
  patchTuesday: [PatchTuesday!]! @relationship(type: "RELATES_TO", direction: OUT, properties: "_TimeProperty")
}

type Vulnerability {
  name: String
  uid: String
  srid: String
  createdAt: Float
  updatedAt: Float
  hasCve: [CVE!]! @relationship(type: "HAS_CVE", direction: OUT, properties: "_TimeProperty")
  domainVulnerability: [Domain!]! @relationship(type: "VULNERABILITY_OF", direction: OUT)
  ipVulnerability: [IP!]! @relationship(type: "VULNERABILITY_OF", direction: OUT)
  urlVulnerability: [URL!]! @relationship(type: "VULNERABILITY_OF", direction: OUT)
  objectVulnerability: [Object!]! @relationship(type: "VULNERABILITY_OF", direction: OUT)
  emailVulnerability: [Email!]! @relationship(type: "VULNERABILITY_OF", direction: OUT)
}

type Patch
{
  uid: String
  srid: String
  value: String
  type: String
  patchId: String
  source: String
  createdAt: Float
  updatedAt: Float
  cve: String
  hasCve: [CVE!]! @relationship(type: "PATCH_OF", direction: OUT, properties: "_TimeProperty")
  hasCpe: [CPE!]! @relationship(type: "HAS_CPE", direction: OUT, properties: "_TimeProperty")
}

`;



// Check Neo4j connection before running queries
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

