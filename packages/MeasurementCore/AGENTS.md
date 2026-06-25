# MeasurementCore spezifische Regeln

1. Dieses Modul kennt weder SwiftUI noch ARKit UI Typen.
2. Alle öffentlichen geometrischen Typen tragen Einheit und Koordinatenraum.
3. Algorithmen sind deterministisch, sofern kein explizit geseedeter Zufall verwendet wird.
4. Jeder Fit liefert Parameter, Residuen, Inlier, Konvergenzstatus und Diagnostik.
5. Jede Messung liefert MeasurementValue, Provenance, Uncertainty, QualityDecision und EvidenceReference.
6. Property Tests prüfen Invarianz gegen Translation, Rotation und zulässige Skalierung.
7. Degenerierte Eingaben werden als typisierte Fehler abgelehnt.
8. Tests enthalten Ground Truth, Grenzfälle und numerisch schwierige Fälle.