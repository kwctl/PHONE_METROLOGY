# ADR 0001: Product Scope

Status: Accepted

## Decision

PhoneMetrology Enterprise measures visible hardware geometry and documents derived or externally sourced values separately.

## Consequences

- Hidden geometry is never silently inferred as measured.
- Accuracy claims require validation evidence.
- UI and exports must show provenance, uncertainty, and quality.
