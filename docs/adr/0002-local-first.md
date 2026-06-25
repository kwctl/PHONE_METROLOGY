# ADR 0002: Local-First Architecture

Status: Accepted

## Decision

The offline iOS application is the primary product. Accounts, backend services, and enterprise sync are optional adapters.

## Consequences

- Measurement cannot depend on network availability.
- Sync conflicts and revisions are modeled above local persistence.
- Local export, backup, restore, and deletion are mandatory product capabilities.
