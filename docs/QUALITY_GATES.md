# Quality Gates

## Severity

| Severity | Meaning |
|---|---|
| P0 | Release or merge blocker with direct correctness, safety, data-loss, security, or false-measurement impact. |
| P1 | Must fix before phase gate closes. |
| P2 | Must be owned and scheduled or explicitly accepted. |
| P3 | Improvement or documentation issue. |

## B0 Bootstrap

Status: complete locally.

Evidence:

- `.codex/config.toml` exists and TOML syntax is valid.
- `.codex/hooks.json` exists and JSON syntax is valid.
- `.codex/hooks/*.py` compile.
- `.codex/agents/*.toml` exist and TOML syntax is valid.
- `AGENTS.md` and module `AGENTS.md` files exist.
- Git repository initialized locally.

## P0 Project Control

Status: in progress.

Acceptance criteria:

- Requirements are testable.
- Product boundaries are explicit.
- Measurement values and provenance are defined.
- Threat model covers mobile app, import, export, optional sync, and CI.
- Later phases have acceptance criteria.
- Independent review reports no P0 or P1 documentation contradictions.

Open evidence gap: independent review not yet performed.

## P1 Build Foundation

Status: not started.

Acceptance criteria:

- `xcodebuild -list` succeeds.
- Debug build succeeds.
- Unit test target runs.
- Baseline UI test launches the app.
- CI executes at least syntax, build, and tests.
- Debug screen shows build metadata.
- No P0 or P1 scaffold review findings remain.

Open evidence gap: no macOS/Xcode environment is available in this session.
