# Coordinate Systems

Coordinate frames must be named in source and target direction. Public geometry APIs cannot expose untyped matrices.

Initial frames:

- `ImagePixelFrame`: 2D image pixel coordinates.
- `RGBCameraFrame`: RGB camera optical coordinate system.
- `DepthCameraFrame`: depth sensor coordinate system.
- `ARWorldFrame`: ARKit world coordinate system for session pose.
- `SupportPlaneFrame`: fitted support plane.
- `BoardFrame`: local board coordinate system.
- `ConnectorFrame`: local connector coordinate system.

Rules:

- Transform names must include source and target.
- Units must be explicit.
- Handedness and origin must be documented.
- Orientation metadata is separate for sensor, image, display, and EXIF.
