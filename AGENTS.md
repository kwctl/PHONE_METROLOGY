# PhoneMetrology Enterprise, Arbeitsvertrag für Agenten

## Mission

Dieses Repository entwickelt ein natives iPhone Messsystem für sichtbare Hardwaregeometrie. Primäres Freigabegerät der ersten Produktgeneration ist das iPhone 15 Pro Max. Die Endnutzer benötigen beim Messen ausschließlich das iPhone. Entwicklung, Kalibrierung und Produktvalidierung dürfen und müssen externe Referenzkörper und Laborgeräte verwenden.

## Unverhandelbare Messintegrität

1. Ein Zahlenwert ist nur zulässig, wenn Herkunft, Einheit, Unsicherheit, Qualitätsstatus und verwendete Daten dokumentiert sind.
2. Verdeckte Geometrie wird niemals als optisch gemessen ausgegeben.
3. Herkunftstypen bleiben getrennt: measured, derived, manufacturer, userProvided, estimated, unknown.
4. Mehr Nachkommastellen bedeuten keine höhere Genauigkeit.
5. Eine Messung wird abgelehnt, wenn Eingangsdaten die gewünschte Toleranz nicht tragen.
6. Genauigkeitsbehauptungen entstehen ausschließlich aus realen, versionierten Validierungsberichten.
7. Simulatorergebnisse sind keine Sensorvalidierung.
8. LiDAR ist ein Messkanal und Plausibilitätssignal, kein automatischer Präzisionsnachweis.
9. Hochauflösende RGB Bilder bestimmen sichtbare Kanten, sofern das Messmodell dies trägt.
10. Alle Koordinatensysteme und Transformationsrichtungen müssen im Typ oder Namen erkennbar sein.

## Produktgrenzen

Der Offline Kern muss ohne Konto, Netzwerk und Backend messen, speichern und exportieren können. Enterprise Sync ist optional und darf keine Abhängigkeit des Messkerns erzeugen.

Die App darf keine Aussage über interne Kontakte, verdeckte Anschläge, nicht sichtbare Einstecktiefen oder Bauteile unter Abschirmungen erfinden. Herstellerdaten dürfen ergänzen, müssen aber als Herstellerquelle gekennzeichnet werden.

## Architektur

Trenne mindestens:

1. AppUI
2. Capture
3. DeviceCapabilities
4. MeasurementCore
5. MeasurementModels
6. Persistence
7. Export
8. EnterpriseSync
9. Diagnostics
10. TestSupport
11. ValidationToolkit

Messmathematik darf nicht von SwiftUI, ARView oder globalen Singletons abhängen. Hardwarezugriff erfolgt über Protokolle und injizierbare Implementierungen.

Große Capture Artefakte liegen als versionierte Dateien mit Prüfsummen vor. Metadaten liegen in einer migrierbaren lokalen Datenbank. Das Dateiformat muss dokumentiert und vorwärtskompatibel versioniert sein.

## Numerische Regeln

1. Intern SI Einheiten und Double verwenden.
2. Millimeter nur an UI und Exportgrenzen.
3. Keine vorzeitige Rundung.
4. Keine Pixel zu Millimeter Konstante ohne geometrisches Modell.
5. Bildorientierung, Sensororientierung, Displayorientierung und EXIF Orientierung getrennt behandeln.
6. Jede Transformation dokumentiert Quelle, Ziel, Einheit, Händigkeit und Zeitpunkt.
7. Robust Fitting benötigt Residuen, Inlier Definition und Abbruchkriterium.
8. Unsicherheitsfortpflanzung muss testbar und deterministisch reproduzierbar sein.

## Sicherheits und Datenschutzregeln

1. Lokale Verarbeitung ist Standard.
2. Upload benötigt eine explizite Organisationsrichtlinie und verständliche Nutzereinwilligung.
3. Keine Rohbilder, Depth Maps, Zugangsdaten oder vollständigen Dateipfade in Produktionslogs.
4. Secrets ausschließlich aus sicheren Secret Stores.
5. Große Dateien erhalten Prüfsumme, Größenlimit und Typprüfung.
6. Mandantentrennung muss in Autorisierung und Datenzugriff erzwungen werden.
7. Jede Datenlöschung muss lokale Dateien, Datenbankeinträge, Cloudobjekte und abgeleitete Indizes berücksichtigen.
8. Neue Abhängigkeiten benötigen Lizenz, Wartungs, Security und Binärgrößenprüfung.

## Engineering Regeln

1. Swift 6 Concurrency Warnungen werden nicht ignoriert.
2. Keine force unwraps im Sensor, Persistenz, Sync oder Messpfad ohne nachgewiesene Invariante.
3. Keine stummen Fehler. Fehler werden typisiert, geloggt ohne sensible Daten und der UI handlungsorientiert erklärt.
4. Keine globale mutable State außerhalb klarer Actor oder MainActor Grenzen.
5. Keine Produktionsfunktion mit statischen Demoergebnissen.
6. TODO, FIXME und Platzhalter im Releasepfad sind Releaseblocker, sofern sie nicht in einer freigegebenen Known Limitations Liste stehen.
7. Änderungen klein halten, testen, reviewen und dokumentieren.
8. Nie mehr als einen schreibenden Subagenten gleichzeitig am selben Modul einsetzen.

## Testpflicht

Für jede Verhaltensänderung ist der kleinste aussagekräftige Test auszuführen. Vor Merge sind zusätzlich erforderlich:

1. Build
2. Unit Tests
3. relevante Integrationstests
4. relevante UI Tests
5. Lint und Formatprüfung
6. unabhängiger Review
7. Dokumentationsaktualisierung
8. bei Sensoränderungen ein Eintrag im Gerätevalidierungsplan

Synthetische Geometrietests müssen bekannte Ground Truth, kontrolliertes Rauschen und Fehlerfälle enthalten. Golden Datasets sind versioniert und unveränderbar.

## Definition of Done

Eine Aufgabe ist nur abgeschlossen, wenn:

1. Anforderungen und Akzeptanzkriterien erfüllt sind.
2. Code kompiliert.
3. relevante Tests bestehen.
4. keine neue Warnung entstanden ist.
5. P0 und P1 Reviews geschlossen sind.
6. Datenmigration und Rückwärtskompatibilität geprüft sind, sofern betroffen.
7. Security und Privacy Auswirkungen bewertet sind.
8. Dokumentation und STATUS.md aktualisiert sind.
9. reale Hardwareprüfungen entweder bestanden oder explizit als offenes menschliches Gate dokumentiert sind.

## Projektstatus

Der Hauptagent pflegt docs/STATUS.md als einzige aktuelle Phasenübersicht. Jede Session liest zuerst AGENTS.md, docs/STATUS.md, docs/QUALITY_GATES.md und die für das Modul zuständige lokale AGENTS.md.