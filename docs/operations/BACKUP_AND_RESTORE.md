# Backup and Restore

Backup and restore are required local enterprise capabilities.

Initial policy:

- Project packages are versioned.
- Large artifacts carry checksums and sizes.
- Restore validates manifest, schema version, checksums, and required files.
- Deletion must include metadata, large artifacts, indexes, derived exports, and sync objects where applicable.
