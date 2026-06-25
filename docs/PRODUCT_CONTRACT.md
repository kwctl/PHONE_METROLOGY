# Product Contract

PhoneMetrology Enterprise is a local-first iPhone application for measuring visible hardware geometry. The first target device is iPhone 15 Pro Max.

## Allowed Product Claims Before Validation

- The product is under development.
- The intended measurement target is visible geometry such as board outlines, visible holes, visible connector envelopes, and distances between visible features.
- Simulator tests can validate deterministic software behavior but cannot validate sensor accuracy.

## Disallowed Claims Before Validation

- No final accuracy claim is allowed without a versioned validation report.
- No hidden geometry may be represented as optically measured.
- No manufacturing-ready export may include estimated values unless the user explicitly opts in and the export marks those values as estimated.

## Required Value Metadata

Every reported value must include value, unit, provenance, uncertainty when applicable, quality decision, evidence references, algorithm or source version, and creation timestamp.

## Offline Contract

The measurement core, local projects, and exports must work without an account, network, or backend. Enterprise sync is optional and cannot block local measurement.
