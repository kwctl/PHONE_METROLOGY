# Privacy Data Map

| Data | Stored Locally | Sync Optional | Notes |
|---|---:|---:|---|
| Project metadata | Yes | Yes | Contains project names and revision metadata. |
| RGB captures | Yes | Yes | Sensitive by default; excluded from support export unless selected. |
| Depth and confidence maps | Yes | Yes | Treated as raw capture data. |
| Measurements | Yes | Yes | Includes provenance, uncertainty, quality, and evidence references. |
| Audit events | Yes | Yes | Must not contain raw secrets or full local paths. |
| Diagnostics | Yes | Optional | Redacted by default. |
