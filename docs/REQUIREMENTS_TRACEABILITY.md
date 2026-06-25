# Requirements Traceability

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-PROV-001 | Every output value has exactly one primary provenance classification. | Blueprint sections 5 and 9 | Unit tests for model encoding and export schema. |
| REQ-PROV-002 | Estimated values are excluded from manufacturing-critical exports unless explicitly approved. | Blueprint section 5.4 | Export policy tests. |
| REQ-OFFLINE-001 | Measurement, storage, and export work without account or network. | Blueprint sections 7 and 8 | UI/integration test with network disabled. |
| REQ-GEOM-001 | Hidden geometry is represented as `unknown` unless sourced externally. | Blueprint sections 5.3 and 10.5 | Domain model and export tests. |
| REQ-UNC-001 | Accepted measurements include uncertainty and quality decision. | Blueprint sections 9 and 10 | MeasurementCore unit tests. |
| REQ-CAP-001 | Device capability snapshot is captured before measurement. | Blueprint section 10.1 | Real-device test and simulator mock test. |
| REQ-SEC-001 | Raw images, depth maps, secrets, and full paths are not written to production logs. | AGENTS.md security rules | Static checks and log redaction tests. |
| REQ-SYNC-001 | Optional sync does not become a dependency of the offline core. | Blueprint section 8.6 | Architecture review and dependency tests. |
