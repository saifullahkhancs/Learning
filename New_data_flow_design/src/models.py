import json
from typing import Optional, Union, List
from typing_extensions import Literal
import config
from pydantic import BaseModel, Extra, Field, UUID4, ValidationError, root_validator
# from utils.rule_parser import RuleParser
from logger import get_logger
# from utils.coco import iso3_to_country
logger = get_logger(__name__, config.DEBUG)


class IntegrationSchema(BaseModel):
    id: str
    name: str


class SourceSchema(BaseModel):
    id: str = Field(default="")
    value: str
    type: str


class AnalysisSchema(BaseModel):
    community_verdict: Optional[str]
    community_score: Optional[int]
    free_verdict: Optional[str]
    free_score: Optional[int]
    premium_verdict: Optional[str]
    premium_score: Optional[int]
    strike_ready_verdict: Optional[str]
    strike_ready_score: Optional[int]
    strike_ready_tlp:Optional[str]


class _Object(BaseModel):
    md5: Optional[str]
    sha1: Optional[str]
    sha256: Optional[str]
    sha512: Optional[str]

    @root_validator(skip_on_failure=True)
    def validate_hash(cls, values):
        for v, k in values.items():
            if not k:
                values[v] = None
        return values


class ResourceSchema(BaseModel):
    id: str
    entity: str
    type: str
    value: str
    rule: Optional[str]
    object: Optional[_Object] = Field(default={})
    tags: Optional[List[str]] = Field(default=[])
    custom_score: Optional[int]
    analysis_state: Optional[str]
    analysis: Optional[AnalysisSchema] = Field(default={})
    name: Optional[str]
    hash: Optional[str]
    description: Optional[str]
    msg: Optional[str]
    action: Optional[str]
    actions: Optional[str]
    sid: Optional[int]
    rev: Optional[int]
    gid: Optional[int]
    priority: Optional[int]
    class_type: Optional[str]
    reference: Optional[list]
    metadata: Optional[dict]
    yaraParsedData: Optional[dict] = Field(default={})
    sigmaParsedData: Optional[dict] = Field(default={})
    snortParsedData: Optional[dict] = Field(default={})
    raw: Optional[dict]

    class Config:
        extra = Extra.allow

    @root_validator(pre=True)
    def object_handling(cls, values):
        if values['type'].lower() in ['sha1', 'sha256', 'sha512', 'md5']:
            if values.get('object'):
                pass
            else:
                values['object'] = {
                    values['type']: values['value']
                }
            values['type'] = 'object'
        if not values.get('object'):
            values['object'] = {}
        return values


class ActionSchema(BaseModel):
    name: str
    integration: Optional[IntegrationSchema]
    source: Optional[SourceSchema]


class LogMetadataSchema(BaseModel):
    plan_id: Optional[str]
    job_id: Optional[str]
    task_id: Optional[str]
    action: ActionSchema
    resource: ResourceSchema


class AuditLogSchema(BaseModel):
    workspace_id: UUID4
    company_id: UUID4
    user_id: UUID4
    label: str
    description: str
    success: bool = Field(default=True)
    timestamp: float
    type: str = Field(default='info')
    metadata: LogMetadataSchema


class KBCDCPayloadSchema(BaseModel):
    id: str


class KBCDCNodePayloadSchema(KBCDCPayloadSchema):
    before: Optional[dict] = Field(default={})
    after: Optional[dict] = Field(default={})
    type: Literal['node']


class KBCDCRelationPayloadSchema(KBCDCPayloadSchema):
    start: dict
    end: dict
    before: Optional[dict] = Field(default={})
    after: Optional[dict] = Field(default={})
    type: Literal['relationship']
    label: Optional[str]


class KBCDCSchema(BaseModel):
    meta: dict
    payload: Union[KBCDCNodePayloadSchema,
    KBCDCRelationPayloadSchema] = Field(descriminator='type')
    schema: dict = Field(alias='schema')
    def to_dict(self):
        return {
            "meta": self.meta,
            "payload": self.payload.to_dict() if hasattr(self.payload, 'to_dict') else self.payload,
            "schema": self.schema
        }


class NoProcessSchema(BaseModel):
    value: str
    type: str
    domain_only: bool
    whitelisted: bool
    workspace_id: Union[UUID4, str]


class Intel(BaseModel):
    _id: Optional[str]
    id: Optional[str]
    srid: Optional[str]
    uid: Optional[str]
    name: Optional[Union[str, list]]
    displayName: Optional[str]
    description: Optional[str]
    type: Optional[str]
    created_at: Optional[int]
    updated_at: Optional[int]
    entity: Optional[list]
    tag: Optional[list]
    source: Optional[list]
    strikes_count: Optional[int]
    tactic: Optional[list]
    technique: Optional[list]
    strike_id: Optional[list]

    def __init__(self, **data):
        data['created_at'] = data.get('createdAt') or data.get('created_at')
        data['updated_at'] = data.get('updatedAt') or data.get('updated_at')
        super().__init__(**data)


class Rule(Intel):
    value: Optional[str]
    hash: Optional[str]
    msg: Optional[str]
    tlp: Optional[str]
    action: Optional[str]
    sid: Optional[int]
    rev: Optional[int]
    gid: Optional[int]
    priority: Optional[int]
    class_type: Optional[str]
    reference: Optional[list]
    # metadata: Optional[dict]
    exploits_platform: Optional[list]
    service: Optional[Union[str, list]]
    logSourceCategory: Optional[list]

    source_id: Optional[list]
    alert: Optional[list]
    alert_source: Optional[list]
    case: Optional[list]
    deployment: Optional[list]
    plan_id: Optional[list]
    job_id: Optional[list]
    task_id: Optional[list]

    sources_count: Optional[int]
    alerts_count: Optional[int]
    cases_count: Optional[int]
    deployments_count: Optional[int]

    analysis_state: Optional[str]
    community_verdict: Optional[str]
    community_score: Optional[int]
    free_verdict: Optional[str]
    free_score: Optional[int]
    premium_verdict: Optional[str]
    premium_score: Optional[int]
    strike_ready_verdict: Optional[str]
    strike_ready_score: Optional[int]
    analyst_score: Optional[int]

    def __init__(self, **data):
        super().__init__(**data)

    # def apply_old_parser(self, **data):
    #     if (data.get('sig') or data.get('value')) and data.get('type'):
    #         properties = RuleParser(rule=data.get('sig') or data.get('value'),
    #                                 rule_type=data.get('type')).get_properties() or data
    #         data.update(**properties)
    #         prop = {
    #             "displayName": properties.get(
    #                 'name') or properties.get('msg') or properties.get(
    #                 'sr_identifier'),
    #             "name": [
    #                 properties.get('sr_identifier')] if properties.get(
    #                 'sr_identifier') else [data.get("sig")]
    #         }
    #         if prop.get('displayName'):
    #             prop['name'].append(prop.get('displayName'))
    #             prop['name'] = list(set(prop['name']))
    #         data.update(**prop)
    #         data.update({
    #             'value': data.get('sig') or data.get('value'),
    #             'type': data.get('type'),
    #             'hash': properties.get('sr_identifier'),
    #             'entity': ['rule', 'mitigation', data.get('type')]
    #         })

    #     super().__init__(**data)


class Artifact(Intel):
    source_id: Optional[list]
    alert: Optional[list]
    alert_source: Optional[list]
    case: Optional[list]
    deployment: Optional[list]
    plan_id: Optional[list]
    job_id: Optional[list]
    task_id: Optional[list]
    timestamp: Optional[int]
    enrichment_user: Optional[str]

    sources_count: Optional[int]
    alerts_count: Optional[int]
    cases_count: Optional[int]
    deployments_count: Optional[int]
    is_deployable: Optional[bool]

    analysis_state: Optional[str]
    community_verdict: Optional[str]
    community_score: Optional[int]
    free_verdict: Optional[str]
    free_score: Optional[int]
    premium_verdict: Optional[str]
    premium_score: Optional[int]
    strike_ready_verdict: Optional[str]
    strike_ready_score: Optional[int]
    analyst_score: Optional[int]
    analyst_updated_at: Optional[float]
    kb_verdict: Optional[str]
    kb_score: Optional[int]

    malware: Optional[list]
    strike: Optional[list]
    tool: Optional[list]
    cve: Optional[list]
    category: Optional[list]
    threat_actor: Optional[list]
    threat_actors: Optional[list]
    ransom: Optional[list]
    targeted_organization: Optional[list]
    targets_sector: Optional[list]
    targeted_industry: Optional[list]
    targets_region: Optional[list]
    targeted_country: Optional[list]
    attack_origin: Optional[list]
    source_type: Optional[list]
    whois: Optional[dict]
    tlp: Optional[list]

    def __init__(self, **data):
        super().__init__(**data)


class Domain(Artifact):
    domain: Optional[list]
    sr_rank: Optional[int]
    object: Optional[list]
    md5: Optional[list]
    sha1: Optional[list]
    sha256: Optional[list]
    url: Optional[list]
    ipv4: Optional[list]
    email: Optional[list]
    ip: Optional[list[str]]


class Email(Artifact):
    email: Optional[list]

    domain: Optional[list]
    ipv4: Optional[list]
    url: Optional[list]


class IP(Artifact):
    ip: Optional[list]
    ip_type: Optional[str]
    email: Optional[list]
    md5: Optional[list]
    sha1: Optional[list]
    sha256: Optional[list]
    url: Optional[list]
    domain: Optional[list]
    object: Optional[list]

class MD5(Artifact):
    md5: Optional[list]


class SHA1(Artifact):
    sha1: Optional[list]


class SHA256(Artifact):
    sha256: Optional[list]


class SHA512(Artifact):
    sha512: Optional[list]


class Object(Artifact):
    sha512: Optional[str]
    sha256: Optional[str]
    sha1: Optional[str]
    md5: Optional[str]
    object: Optional[list]
    node_type: Optional[str]
    size: Optional[float]
    file_type: Optional[list]
    ip: Optional[List[str]]
    url: Optional[List[str]]
    domain: Optional[List[str]]

    @root_validator(skip_on_failure=True)
    def add_entity(cls, values):
        if len(values.get('entity', []) or []) > 0:
            values['entity'].append('object')
            values['entity'] = list(set(values['entity']))
        else:
            values['entity'] = ['object']
        return values

    @root_validator(pre=True)
    def hashes_validate(cls, values):
        for hash in ['sha256','sha1','sha512','md5']:
            if values.get(hash):
                if isinstance(values[hash],list) and len(values[hash])> 0:
                    if len(values[hash])>1:
                        logger.warning(f'More relation hash object present for hash {values[hash]}')
                    values[hash] = values[hash][0]
            else:
                values[hash] = None
        return values

class URL(Artifact):
    url: Optional[list]
    object: Optional[list]
    email: Optional[list]
    domain: Optional[list]
    ip: Optional[list]


class CVEIntel(Intel):
    source_id: Optional[list]
    alert: Optional[list]
    alert_source: Optional[list]
    case: Optional[list]
    deployment: Optional[list]
    plan_id: Optional[list]
    job_id: Optional[list]
    task_id: Optional[list]

    sources_count: Optional[int]
    alerts_count: Optional[int]
    cases_count: Optional[int]
    deployments_count: Optional[int]

    analysis_state: Optional[str]
    community_verdict: Optional[str]
    community_score: Optional[int]
    free_verdict: Optional[str]
    free_score: Optional[int]
    premium_verdict: Optional[str]
    premium_score: Optional[int]
    strike_ready_verdict: Optional[str]
    strike_ready_score: Optional[int]
    analyst_score: Optional[int]


class CVE(CVEIntel):
    cve: Optional[list]

    attackVector: Optional[str]
    attackComplexity: Optional[str]
    privilegesRequired: Optional[str]
    userInteraction: Optional[str]
    confidentialityImpact: Optional[str]
    integrityImpact: Optional[str]
    availabilityImpact: Optional[str]
    baseSeverity: Optional[str]
    baseScore: Optional[str]
    scope: Optional[str]

    md5: Optional[list]
    sha1: Optional[list]
    sha256: Optional[list]
    url: Optional[list]
    domain: Optional[list]
    sha512: Optional[list]
    strike: Optional[list]
    ipv4: Optional[list]


class Malware(Intel):
    malware: Optional[list]
    campaign_count: Optional[int]
    object: Optional[list]
    threat_actor: Optional[list]
    threat_actors: Optional[list]
    md5: Optional[list]
    sha1: Optional[list]
    sha256: Optional[list]
    url: Optional[list]
    ipv4: Optional[list]
    domain: Optional[list]
    email: Optional[list]
    strike: Optional[list]
    exploits_platform: Optional[list]
    uses_technique: Optional[list]
    uses_tactic: Optional[list]
    category: Optional[list]
    ssdeep: Optional[list]
    uses_strike: Optional[list]
    has_campaign: Optional[list]
    has_stage: Optional[list]
    sponsored_by: Optional[list]
    packed_by: Optional[list]
    compromises_product: Optional[list]


class Mitigation(Rule):
    rule: Optional[list]
    eventId: Optional[list]
    sig: Optional[str]
    url: Optional[list]
    ipv4: Optional[list]
    md5: Optional[list]
    sha1: Optional[list]
    sha256: Optional[list]
    domain: Optional[list]
    email: Optional[list]
    ssdeep: Optional[list]
    malware: Optional[list]
    malwares: Optional[list]
    ransom: Optional[list]
    strike: Optional[list]
    tool: Optional[list]
    cve: Optional[list]
    threat_actor: Optional[list]
    threat_actors: Optional[list]
    source_type: Optional[list]
    source_port: Optional[list]
    destination_port: Optional[list]
    protocol: Optional[str]
    source_ip: Optional[list]
    destination_ip: Optional[list]
    logSourceCategory: Optional[list]

    @root_validator(skip_on_failure=True)
    def rule_entity(cls, values):
        if values.get('type'):
            values['entity'] = [values.get('type'), 'rule']
        return values


class ThreatActor(Intel):
    threat_actor: Optional[list]
    campaign_count: Optional[int]
    object: Optional[list]
    domain: Optional[list]
    has_campaign: Optional[list]
    industry: Optional[list]
    malware: Optional[list]
    md5: Optional[list]
    ransom: Optional[list]
    sha1: Optional[list]
    sha256: Optional[list]
    strike: Optional[list]
    targets_sector: Optional[list]
    tool: Optional[list]
    url: Optional[list]
    originCountry: Optional[str]

    # @root_validator
    # def iso_to_country_name(cls, values):
    #     if values.get('originCountry'):
    #         values['originCountry'] = iso3_to_country(values['originCountry'])
    #     return values



class Tool(Intel):
    tool: Optional[list]
    campaign_count: Optional[int]
    sources_count: Optional[int]
    strike: Optional[list]
    threat_actor: Optional[list]
    threat_actors: Optional[list]
    md5: Optional[list]
    sha1: Optional[list]
    sha256: Optional[list]
    sha512: Optional[list]
    has_campaign: Optional[list]
    object: Optional[list]


class Ransom(Intel):
    ransom: Optional[list]
    campaign_count: Optional[int]
    sources_count: Optional[int]
    object: Optional[list]
    threat_actor: Optional[list]
    threat_actors: Optional[list]
    md5: Optional[list]
    sha1: Optional[list]
    sha256: Optional[list]
    strike: Optional[list]
    has_campaign: Optional[list]


INTEL_SCHEMA = {
    "ThreatActor": ThreatActor,
    "Malware": Malware,
    "Tool": Tool,
    "Ransom": Ransom,
    "CVE": CVE,
    "IP": IP,
    "Domain": Domain,
    "URL": URL,
    "MD5": Object,
    "SHA1": Object,
    "SHA256": Object,
    "SHA512": Object,
    "Email": Email,
    "Mitigation": Mitigation,
    "Object": Object,
    'object': Object,
    "cve": CVE,
    "ip": IP,
    "ipv4": IP,
    "domain": Domain,
    "url": URL,
    "md5": Object,
    "sha1": Object,
    "sha256": Object,
    "sha512": Object,
    "email": Email,
    "yara": Mitigation,
    "snort": Mitigation,
    "sigma": Mitigation,
    "suricata": Mitigation,
    "rule": Mitigation,
}

KB_ARTIFACT_NODES = {
    "IP": "ipv4",
    "Domain": "domain",
    'Object': 'object',
    "URL": "url",
    "MD5": "object",
    "SHA1": "object",
    "SHA256": "object",
    "SHA512": "object",
    "Email": "email",
}

KB_SYNC_NODES = {
    "ThreatActor": "threat_actor",
    "Malware": "malware",
    "Tool": "tool",
    "Ransom": "ransom",
    "CVE": "cve",
    "IP": "ipv4",
    "Domain": "domain",
    "URL": "url",
    "MD5": "object",
    "SHA1": "object",
    "SHA256": "object",
    "SHA512": "object",
    'Object': 'object',
    "Email": "email",
    "Mitigation": "rule",
    "Platform": "exploits_platform",
    "Technique": "technique",
    "Tactic": "tactic",
    "Transaction": "strike",
    "Category": "category",
    "SSDeep": "ssdeep",
    "Strike": "strike",
    "AttackCampaign": "has_campaign",
    "Tag": "tag",
    "Tags": "tag",
    "Stage": "has_stage",
    "Country": "sponsored_by",
    "Packer": "packed_by",
    "Product": "compromises_product",
    "Sector": "targets_sector",
    "Region": "targets_region",
    "Industry": "industry",
    "Source": "source",
    "Author": "author",
    "WhoIs": "whois",
    "FileType": "file_type",
    'RuleIP': 'rule_ip',
    'Reference': 'reference',
    'TLP': 'tlp'
}

INTEL_NODES = {
    "IP": "ipv4",
    "Domain": "domain",
    "URL": "url",
    "MD5": "object",
    "SHA1": "object",
    "SHA256": "object",
    "SHA512": "object",
    "sha1": "object",
    "sha256": "object",
    "sha512": "object",
    'Object': 'object',
    'object': 'object',
    "Email": "email",
    "CVE": "cve",
    "Mitigation": "Mitigation",
}

specialized_node_relations = {
    "IP": {
        "IP_USED_TO_TARGET": {
            "key_name": "targeted_organization",
            "direction": "OUT",
            "related_to": "Organization",
        }
        ,
        "TARGET_SECTOR": {

            "key_name": "targets_sector",
            "direction": "OUT",
            "related_to": "Sector",

        },
        "TARGETS_INDUSTRY": {
            "key_name": "targeted_industry",
            "direction": "OUT",
            "related_to": "Industry",

        },
        "TARGETS_REGION": {
            "key_name": "targets_region",
            "direction": "OUT",
            "related_to": "Region",

        },
        "TARGETS_COUNTRY": {
            "key_name": "targeted_country",
            "direction": "OUT",
            "related_to": "Country",

        },
        "ATTACK_ORIGIN_COUNTRY": {
            "key_name": "attack_origin",
            "direction": "OUT",
            "related_to": "Country",

        }
    },
    "Domain": {
        "DOMAIN_USED_TO_TARGET": {
            "key_name": "targeted_organization",
            "direction": "OUT",
            "related_to": "Organization",
        }
        ,
        "TARGET_SECTOR": {

            "key_name": "targets_sector",
            "direction": "OUT",
            "related_to": "Sector",

        },
        "TARGETS_INDUSTRY": {
            "key_name": "targeted_industry",
            "direction": "OUT",
            "related_to": "Industry",

        },
        "TARGETS_REGION": {
            "key_name": "targets_region",
            "direction": "OUT",
            "related_to": "Region",

        },
        "TARGETS_COUNTRY": {
            "key_name": "targeted_country",
            "direction": "OUT",
            "related_to": "Country",

        },
        "ATTACK_ORIGIN_COUNTRY": {
            "key_name": "attack_origin",
            "direction": "OUT",
            "related_to": "Country",

        }
    },
    "URL": {
        "URL_USED_TO_TARGET": {
            "key_name": "targeted_organization",
            "direction": "OUT",
            "related_to": "Organization",
        }
        ,
        "TARGET_SECTOR": {

            "key_name": "targets_sector",
            "direction": "OUT",
            "related_to": "Sector",

        },
        "TARGETS_INDUSTRY": {
            "key_name": "targeted_industry",
            "direction": "OUT",
            "related_to": "Industry",

        },
        "TARGETS_REGION": {
            "key_name": "targets_region",
            "direction": "OUT",
            "related_to": "Region",

        },
        "TARGETS_COUNTRY": {
            "key_name": "targeted_country",
            "direction": "OUT",
            "related_to": "Country",

        },
        "ATTACK_ORIGIN_COUNTRY": {
            "key_name": "attack_origin",
            "direction": "OUT",
            "related_to": "Country",

        }
    },
    "Object": {
        "OBJECT_USED_TO_TARGET": {
            "key_name": "targeted_organization",
            "direction": "OUT",
            "related_to": "Organization",
        }
        ,
        "TARGET_SECTOR": {

            "key_name": "targets_sector",
            "direction": "OUT",
            "related_to": "Sector",

        },
        "TARGETS_INDUSTRY": {
            "key_name": "targeted_industry",
            "direction": "OUT",
            "related_to": "Industry",

        },
        "TARGETS_REGION": {
            "key_name": "targets_region",
            "direction": "OUT",
            "related_to": "Region",

        },
        "TARGETS_COUNTRY": {
            "key_name": "targeted_country",
            "direction": "OUT",
            "related_to": "Country",

        },
        "ATTACK_ORIGIN_COUNTRY": {
            "key_name": "attack_origin",
            "direction": "OUT",
            "related_to": "Country",
        },
        "OF_TYPE": {
            "key_name": "file_type",
            "direction": "OUT",
            "related_to": "FileType",
        }
    },
    "SHA1": {
        "OBJECT_USED_TO_TARGET": {
            "key_name": "targeted_organization",
            "direction": "OUT",
            "related_to": "Organization",
        }
        ,
        "TARGET_SECTOR": {

            "key_name": "targets_sector",
            "direction": "OUT",
            "related_to": "Sector",

        },
        "TARGETS_INDUSTRY": {
            "key_name": "targeted_industry",
            "direction": "OUT",
            "related_to": "Industry",

        },
        "TARGETS_REGION": {
            "key_name": "targets_region",
            "direction": "OUT",
            "related_to": "Region",

        },
        "TARGETS_COUNTRY": {
            "key_name": "targeted_country",
            "direction": "OUT",
            "related_to": "Country",

        },
        "ATTACK_ORIGIN_COUNTRY": {
            "key_name": "attack_origin",
            "direction": "OUT",
            "related_to": "Country",

        }
    },
    "SHA256": {
        "OBJECT_USED_TO_TARGET": {
            "key_name": "targeted_organization",
            "direction": "OUT",
            "related_to": "Organization",
        }
        ,
        "TARGET_SECTOR": {

            "key_name": "targets_sector",
            "direction": "OUT",
            "related_to": "Sector",

        },
        "TARGETS_INDUSTRY": {
            "key_name": "targeted_industry",
            "direction": "OUT",
            "related_to": "Industry",

        },
        "TARGETS_REGION": {
            "key_name": "targets_region",
            "direction": "OUT",
            "related_to": "Region",

        },
        "TARGETS_COUNTRY": {
            "key_name": "targeted_country",
            "direction": "OUT",
            "related_to": "Country",

        },
        "ATTACK_ORIGIN_COUNTRY": {
            "key_name": "attack_origin",
            "direction": "OUT",
            "related_to": "Country",

        }
    },
    "MD5": {
        "OBJECT_USED_TO_TARGET": {
            "key_name": "targeted_organization",
            "direction": "OUT",
            "related_to": "Organization",
        }
        ,
        "TARGET_SECTOR": {

            "key_name": "targets_sector",
            "direction": "OUT",
            "related_to": "Sector",

        },
        "TARGETS_INDUSTRY": {
            "key_name": "targeted_industry",
            "direction": "OUT",
            "related_to": "Industry",

        },
        "TARGETS_REGION": {
            "key_name": "targets_region",
            "direction": "OUT",
            "related_to": "Region",

        },
        "TARGETS_COUNTRY": {
            "key_name": "targeted_country",
            "direction": "OUT",
            "related_to": "Country",

        },
        "ATTACK_ORIGIN_COUNTRY": {
            "key_name": "attack_origin",
            "direction": "OUT",
            "related_to": "Country",

        }
    },
    "Mitigation": {
        "SOURCE_IP": {
            "key_name": "source_ip",
            "direction": "OUT",
            "related_to": "RuleIP",
        },
        "DESTINATION_IP": {
            "key_name": "destination_ip",
            "direction": "OUT",
            "related_to": "RuleIP",
        }
    }
}

if __name__ == '__main__':
    a = Ransom().dict()
    print(a)
