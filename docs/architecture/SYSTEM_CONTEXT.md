# System Context

PhoneMetrology Enterprise is a local-first iOS product. The primary user is an engineer or technician measuring visible hardware geometry for prototyping, documentation, and CAD handoff.

## Core Boundaries

- iOS app: capture guidance, annotation, local project management, and export.
- MeasurementCore: geometry, typed coordinate frames, fitting, uncertainty, and quality decisions.
- CaptureContracts: protocols and metadata contracts for ARKit, AVFoundation, CoreMotion, and simulator mocks.
- ExportKit: JSON, CSV, SVG, DXF, and later PDF/STEP export boundaries.
- Optional sync service: organization, role, audit, retention, and object sync. It is not required for local measurement.

## External Systems

- iPhone sensors and iOS frameworks.
- Local file system and database.
- Optional enterprise identity provider through OIDC.
- Optional object storage and PostgreSQL for sync.
- CAD tools consuming exported geometry.
