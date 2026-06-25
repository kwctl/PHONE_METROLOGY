# Threat Model

## Assets

- Raw RGB and depth captures.
- Measurement results and evidence.
- Project packages and local database.
- Export artifacts.
- Organization identity and roles for optional sync.
- CI secrets and signing material.

## Threat Surfaces

- iOS capture and local storage.
- Import and export parsers.
- Diagnostics and support packages.
- Optional sync API and object storage.
- Admin portal.
- CI/CD and release artifacts.

## Initial Controls

- Local processing by default.
- No sensitive raw data in production logs.
- Explicit upload policy and consent for sync.
- Checksums and schema versions for large artifacts.
- Tenant isolation and audit events for sync.
- Secret scanning and dependency inventory before release.
