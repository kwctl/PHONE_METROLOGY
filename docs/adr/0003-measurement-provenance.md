# ADR 0003: Measurement Provenance

Status: Accepted

## Decision

Each output value carries one primary provenance classification: `measured`, `derived`, `manufacturer`, `userProvided`, `estimated`, or `unknown`.

## Consequences

- `estimated` values are excluded from manufacturing-critical exports unless explicitly enabled.
- Manufacturer data is not merged into measured values without preserving source identity in evidence.
- Unknown values remain visible as unknown instead of being filled with plausible numbers.
