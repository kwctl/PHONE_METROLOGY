# iOS spezifische Regeln

1. Nutze native SwiftUI Navigation und systemnahe Controls.
2. Sensorzugriff liegt außerhalb von Views.
3. Capture Sessions, ARSession und Motion Manager besitzen explizite Zustandsautomaten.
4. UI Updates laufen auf MainActor, rechenintensive Geometrie nicht.
5. Capture Daten werden zeitgestempelt, versioniert und mit Geräte, OS, Format, Intrinsics und Pose Metadaten gespeichert.
6. Runtime Capability Checks sind verpflichtend.
7. Fokus, Belichtung, Zoom, Stabilisierung und aktive Kamera werden pro Aufnahme protokolliert.
8. Permission Ablehnung und Unterbrechungen durch Telefonate, Hintergrundwechsel oder Thermal State sind testbare Zustände.
9. Accessibility Identifier für zentrale Flows sind verpflichtend.
10. Kein Netzwerk im Messpfad.