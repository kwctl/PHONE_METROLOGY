# Risk Register

| ID | Risk | Severity | Mitigation | Status |
|---|---|---:|---|---|
| R-001 | Product could imply unsupported measurement accuracy. | P0 | Block claims until validation report exists; show uncertainty and provenance in UI and export. | Open |
| R-002 | Hidden connector dimensions could be inferred as measured. | P0 | Require `unknown` or `manufacturer` provenance for non-visible geometry. | Open |
| R-003 | Windows session cannot validate iOS build. | P1 | Move P1 scaffold verification to macOS/Xcode. | Open |
| R-004 | GitHub repository cannot be written from current credentials. | P1 | Local Git push succeeded on 2026-06-25. Keep connector permissions under review. | Closed |
| R-005 | LiDAR/depth registration assumptions could create plausible but wrong dimensions. | P0 | Require ADR and runtime capability probes before sensor pipeline lock-in. | Open |
| R-006 | Sensitive raw capture data could leak through diagnostics. | P1 | Define redaction and support package policy before diagnostics implementation. | Open |
