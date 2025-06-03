import json

data = {
  "workspace_id": "de38ad9d-638b-4621-96de-7c0f77e9edf1",
  "company_id": "930226c1-3d64-481b-86e1-29eba3107a6e",
  "user_id": "23bbe6c7-597f-4e6d-8ddf-5c39000ee1c1",
  "label": "Enrich artifacts",
  "description": "Enriched artifacts from AE",
  "success": True,
  "timestamp": 1742371140.435291,
  "type": "info",
  "metadata": {
    "plan_id": None,
    "job_id": None,
    "task_id": "220004f1-15fa-4750-b8f5-e4590bea909d",
    "action": {
      "name": "enrichment",
      "integration": None,
      "source": None
    },
    "resource": {
      "id": "67da792e15c37e4502d9aec3",
      "entity": "Intel",
      "type": "domain",
      "value": "aliasndksandsa.com",
      "rule": None,
      "tags": [],
      "custom_score": None,
      "analysis_state": "completed",
      "analysis": {
        "community_verdict": "clean",
        "community_score": 5,
        "free_verdict": "clean",
        "free_score": 5,
        "premium_verdict": "no verdict",
        "premium_score": 0,
        "strike_ready_verdict": "clean",
        "strike_ready_score": 2,
        "strike_ready_tlp": "white"
      },
      "object": {},
      "hash": None,
      "force_refresh": True
    },
    "upcoming_retirement": None
  }
}

data= (data)
tlp=[ data.get("metadata").get("resource").get("analysis").get("strike_ready_tlp")] if data.get("metadata").get("resource").get("analysis_state") == "completed" and data.get("metadata").get("resource").get("analysis").get("strike_ready_tlp") else None

print(tlp)