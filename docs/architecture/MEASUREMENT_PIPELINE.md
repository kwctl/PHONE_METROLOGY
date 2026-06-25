# Measurement Pipeline

## Planar Distance Pipeline

1. Check device capability snapshot.
2. Guide the user into acceptable distance, angle, lighting, and stability.
3. Capture multiple acceptable frames.
4. Fit or confirm the support or board plane.
5. Convert annotated image points to camera rays.
6. Intersect rays with the plane.
7. Transform points into `BoardFrame`.
8. Aggregate repeated frames.
9. Compute distance, residuals, uncertainty, and quality decision.
10. Store evidence and export only with provenance.

## Rejection Conditions

- Insufficient frames.
- Unstable motion.
- Saturated or blurred imagery.
- Degenerate geometry.
- Nearly parallel ray-plane intersection.
- Uncertainty exceeds the requested use case.
