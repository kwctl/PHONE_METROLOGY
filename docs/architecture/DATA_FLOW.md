# Data Flow

## Local Measurement Flow

1. Device capability snapshot records model, OS, camera, depth, intrinsics, thermal state, permissions, and storage state.
2. Guided capture collects RGB, depth when available, motion stability, focus, exposure, and quality metadata.
3. User annotations or confirmed candidates define visible features.
4. MeasurementCore transforms pixels through camera rays and coordinate frames into geometric primitives.
5. Fitting produces values, residuals, uncertainty, quality decisions, and evidence references.
6. Persistence stores project metadata and large artifacts with schema version and checksums.
7. ExportKit emits files that preserve units, origin, provenance, uncertainty, and warnings.

## Optional Sync Flow

Sync packages local immutable revisions for upload after explicit organizational policy and user consent. Server-side storage must enforce tenant separation, checksums, audit events, retention, and deletion.
