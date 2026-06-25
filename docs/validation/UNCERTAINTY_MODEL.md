# Uncertainty Model

The initial uncertainty model will track contributors from pixel localization, intrinsics, pose, plane fit, depth or ray-plane geometry, repeatability, and fitting residuals.

## Rules

- Internally use SI units and `Double`.
- Expanded uncertainty includes coverage factor and confidence level.
- Increased input noise must increase or preserve output uncertainty in tests.
- Degenerate geometry must be rejected instead of producing narrow intervals.
- UI and exports show the value with its 95 percent interval when accepted.
