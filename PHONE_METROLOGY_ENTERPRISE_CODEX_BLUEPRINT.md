# PhoneMetrology Enterprise

## Eine Datei für Codex Konfiguration, Subagents, Entwicklungsvertrag und vollständigen Master Prompt

**Version:** 1.0  
**Stand:** 25. Juni 2026  
**Primäres Zielgerät:** iPhone 15 Pro Max  
**Arbeitstitel des Produkts:** PhoneMetrology Enterprise  
**Dokumenttyp:** Single Source Build Blueprint

---

## 1. Zweck dieser Datei

Diese Datei ist die zentrale Spezifikation für ein agentisch entwickeltes, natives iOS Produkt zur zuverlässigen Vermessung sichtbarer Hardwaregeometrie. Sie enthält:

1. den Produktvertrag,
2. die technischen und metrologischen Grenzen,
3. die Zielarchitektur,
4. die Enterprise Qualitätsdefinition,
5. die Codex Projektkonfiguration,
6. alle vorgesehenen Subagent Rollen,
7. Repository Regeln,
8. Sicherheits Hooks,
9. Phasen, Exit Gates und Releasekriterien,
10. einen vollständigen Master Prompt,
11. einen Fortsetzungsprompt für spätere Codex Sessions,
12. menschliche Gates, die ein Agent nicht seriös ersetzen kann.

Diese Datei ist absichtlich deutlich umfangreicher als ein normaler Prompt. Ein Enterprise Produkt entsteht nicht dadurch, dass Codex möglichst viel Code in einem Durchlauf erzeugt. Es entsteht durch klar getrennte Verantwortlichkeiten, kleine überprüfbare Änderungen, reale Geräteprüfungen, reproduzierbare Builds, unabhängige Reviews und belastbare Messvalidierung.

### Kritische Grenze

Ein Prompt kann einen Entwicklungsprozess steuern. Er kann kein Produkt zertifizieren und keine reale Messgenauigkeit beweisen. Eine Freigabe ist erst zulässig, wenn die in diesem Dokument definierten Software, Security, Hardware und Messgates tatsächlich bestanden wurden.

Der Endnutzer soll ausschließlich das iPhone als Messwerkzeug benötigen. Das bedeutet nicht, dass Entwicklung und Produktvalidierung ohne externe Referenzen erfolgen dürfen. Für die Kalibrierung, Benchmarking und Freigabe sind präzise Referenzkörper, Vergleichsmessgeräte und dokumentierte Sollwerte zwingend.

---

## 2. So wird diese Datei verwendet

### 2.1 Voraussetzungen

1. Ein Mac mit einer stabilen Xcode Installation.
2. Ein lokal verbundenes iPhone 15 Pro Max für reale Sensortests.
3. Git.
4. Codex CLI, Codex App oder Codex IDE Integration.
5. Für spätere Releasephasen ein Apple Developer Konto.
6. Für Enterprise Sync optional Docker, eine Container Runtime und Cloud oder Testinfrastruktur.
7. Für Messfreigaben geeignete Referenzkörper und Vergleichsmessmittel.

### 2.2 Repository anlegen

```bash
mkdir PhoneMetrology
cd PhoneMetrology
git init
```

Lege diese Datei im Repository Stamm unter folgendem Namen ab:

```text
PHONE_METROLOGY_ENTERPRISE_CODEX_BLUEPRINT.md
```

### 2.3 Erster Codex Lauf, nur Bootstrap

Starte Codex zunächst mit dem Standardmodell:

```bash
codex -m gpt-5.5
```

Verwende als ersten Prompt:

```text
Lies PHONE_METROLOGY_ENTERPRISE_CODEX_BLUEPRINT.md vollständig.
Führe ausschließlich Abschnitt B0, Bootstrap, aus.
Materialisiere alle eingebetteten Dateien exakt an den angegebenen Pfaden.
Validiere TOML, JSON und Python Syntax.
Ändere noch keinen Produktcode.
Berichte anschließend, welche Dateien erzeugt wurden und fordere einen Neustart der Codex Session an, damit Projektkonfiguration, AGENTS.md, Hooks und Subagents neu geladen werden.
```

Danach Codex beenden und im Repository neu starten. Der Neustart ist notwendig, weil Codex Projektanweisungen und Konfigurationsschichten beim Start einer Session lädt.

### 2.4 Zweiter Codex Lauf, Produktentwicklung

Nach dem Neustart:

```bash
codex -m gpt-5.5
```

Dann den in Abschnitt **M, Master Prompt** enthaltenen Prompt verwenden.

### 2.5 Spätere Sessions

Ein solches Produkt wird nicht seriös in einer einzigen Agentensession fertig. Für jede neue Session wird der in Abschnitt **N, Fortsetzungsprompt** definierte Prompt verwendet. `docs/STATUS.md` ist dabei die verbindliche Quelle für den aktuellen Stand.

---

## 3. Modell und Agentenstrategie

Die Standardwahl ist `gpt-5.5` mit hohem Reasoning für Architektur, Messmathematik, Sensorik, Security, Review und schwierige Implementierung. `gpt-5.4-mini` wird nur für schnelle Repository Exploration und Dokumentationsaufgaben verwendet.

Die Begründung ist funktional:

1. Fehler in UI Texten sind korrigierbar.
2. Fehler in Koordinatentransformationen können unbemerkt plausible, aber falsche Maße erzeugen.
3. Fehler in Unsicherheitsberechnung können Scheingenauigkeit erzeugen.
4. Fehler in Mandantentrennung können Enterprise Daten offenlegen.
5. Deshalb erhalten kritische Rollen das stärkere Modell und hohe Reasoning Tiefe.

Es werden höchstens sechs Threads gleichzeitig geöffnet. Die Verschachtelungstiefe bleibt auf eins. Damit darf der Hauptagent spezialisierte Subagents starten, Subagents dürfen jedoch keine unkontrollierten Agentenkaskaden erzeugen.

Read only Recherche und Review können parallel laufen. Schreibende Agenten arbeiten seriell pro Modul. Zwei Agenten dürfen niemals gleichzeitig dieselben Dateien oder dasselbe Modul verändern.

---

## 4. Produktvision

PhoneMetrology Enterprise soll kleine Hardwareteile, Leiterplatten, Bohrungen, Lochabstände, sichtbare Bauteilhöhen, Anschlusspositionen und sichtbare Steckergeometrie mit einem iPhone 15 Pro Max erfassen.

Das Produkt dient primär folgenden Aufgaben:

1. Gehäusekonstruktion und Prototyping.
2. Erstellung von Bohrbildern.
3. Bestimmung von Platinenkonturen.
4. Platzierung von Abstandshaltern.
5. Positionierung sichtbarer Anschlüsse.
6. Erzeugung von CAD nutzbaren Konturen und Referenzdaten.
7. Dokumentation von Hardwarevarianten.
8. Vergleich mehrerer Bauteile oder Revisionen.
9. Nachvollziehbare Übergabe von Messdaten an Konstruktionsteams.

Das Produkt ist kein universelles industrielles Koordinatenmessgerät. Es darf keine Submillimeterleistung behaupten, die nicht durch reale Validierung für konkrete Messbedingungen nachgewiesen wurde.

---

## 5. Produktgrenzen und Wahrheitsregeln

### 5.1 Direkt messbar

Unter geeigneten Aufnahmebedingungen können direkt optisch bestimmt werden:

1. sichtbare Außenkonturen,
2. sichtbare Kanten,
3. sichtbare Lochränder,
4. Lochmittelpunkte,
5. Abstände zwischen sichtbaren Merkmalen,
6. sichtbare Steckerfronten,
7. sichtbare Außenhüllen,
8. sichtbare Bauteilhöhen,
9. sichtbare Orientierung und Einsteckachse,
10. sichtbare Überstände relativ zu Platinenkanten.

### 5.2 Nur abgeleitet

Folgende Werte sind abgeleitet und müssen so gekennzeichnet werden:

1. Gehäuseausschnitt mit Fertigungszugabe,
2. Kollisionshülle,
3. Bedienraum,
4. Kabelraum,
5. empfohlener Abstandshalter,
6. Toleranzzugabe für FDM, SLA, CNC oder Laserschnitt,
7. CAD Primitive, die aus Messpunkten angepasst wurden.

### 5.3 Nicht optisch beweisbar

Ohne Herstellerdaten, Demontage oder zusätzliche Information sind nicht zuverlässig bestimmbar:

1. vollständig verdeckte Einstecktiefe,
2. interne Kontaktgeometrie,
3. verdeckte Anschläge,
4. Bauteile unter Metallabschirmungen,
5. Lötflächen unter Gehäusen,
6. Materialeigenschaften,
7. Fertigungstoleranzen des Herstellers,
8. notwendiger Kabelbiegeradius ohne Kenntnis des Kabels.

Diese Werte erhalten den Status `unknown`, sofern keine gekennzeichnete externe Quelle vorliegt.

### 5.4 Herkunft jedes Wertes

Jeder ausgegebene Wert besitzt zwingend genau einen Herkunftstyp:

```text
measured
derived
manufacturer
userProvided
estimated
unknown
```

`estimated` darf standardmäßig nicht in fertigungskritische Exporte einfließen. Der Nutzer muss dies bewusst freigeben.

---

## 6. Vorläufige Engineering Ziele, keine Produktversprechen

Die folgenden Werte sind Entwicklungsziele für kontrollierte Bedingungen. Sie sind keine freigegebenen Genauigkeitsangaben:

| Messklasse | Vorläufiges Ziel für erweitertes 95 Prozent Intervall |
|---|---:|
| Planare Punktabstände bis 100 mm | höchstens ±0,35 mm |
| Lochmittelpunktpositionen | höchstens ±0,35 mm |
| Sichtbare Lochdurchmesser ab 2 mm | höchstens ±0,45 mm |
| Sichtbare Steckerfront und Außenhülle | höchstens ±0,60 mm |
| Sichtbare Höhen bis 30 mm | höchstens ±0,80 mm |

Eine Messfunktion darf erst mit einem Wert beworben werden, wenn ein versionierter Validierungsbericht nachweist:

1. Bias,
2. Wiederholbarkeit,
3. Reproduzierbarkeit,
4. Ausfallrate,
5. Abdeckung des angegebenen 95 Prozent Intervalls,
6. unterstützte Materialien,
7. unterstützte Beleuchtung,
8. unterstützte Entfernungen,
9. unterstützte OS und Geräteversionen.

Wenn die Ziele nicht erreicht werden, muss entweder die Funktion eingeschränkt, die Messanleitung verschärft oder die Unsicherheitsangabe vergrößert werden.

---

## 7. Enterprise Definition

Enterprise bedeutet in diesem Projekt nicht nur ein professionelles Erscheinungsbild. Das Produkt gilt erst als Enterprise geeignet, wenn folgende Bereiche nachweisbar behandelt sind:

### 7.1 Produktqualität

1. reproduzierbare Builds,
2. versionierte Datenformate,
3. Datenmigrationen,
4. Crash und Fehlerbehandlung,
5. Offline Betrieb,
6. Backup und Export,
7. dokumentierte Systemgrenzen,
8. Supportdiagnose ohne sensible Rohdaten.

### 7.2 Messqualität

1. validiertes Messmodell,
2. Unsicherheit pro Wert,
3. automatische Ablehnung ungeeigneter Daten,
4. wiederholbare Capture Führung,
5. versionierte Validierungsdatensätze,
6. nachvollziehbare Provenienz,
7. keine erfundene Geometrie.

### 7.3 Security und Datenschutz

1. lokaler Datenschutz als Standard,
2. sichere Speicherung,
3. minimale Telemetrie,
4. dokumentierter Datenfluss,
5. rollenbasierter Zugriff bei Sync,
6. Mandantentrennung,
7. Audit Events,
8. sichere Löschung,
9. SBOM und Dependency Kontrolle,
10. Incident und Vulnerability Prozess.

### 7.4 Betrieb

1. CI/CD,
2. Release Evidence,
3. Rollback,
4. Backup und Restore,
5. Monitoring,
6. Runbooks,
7. dokumentierte Verantwortlichkeiten,
8. klare menschliche Freigabegates.

### 7.5 Accessibility und Internationalisierung

1. VoiceOver,
2. Dynamic Type,
3. Kontrast,
4. reduzierte Bewegung,
5. verständliche Fehlermeldungen,
6. mindestens Deutsch und Englisch,
7. locale korrekte Einheiten und Zahlen.

---

## 8. Zielarchitektur

### 8.1 Komponenten

```text
PhoneMetrology/
├── apps/
│   └── ios/
├── packages/
│   ├── MeasurementCore/
│   ├── MeasurementModels/
│   ├── CaptureContracts/
│   ├── ExportKit/
│   └── TestSupport/
├── services/
│   └── api/
├── web/
│   └── admin/
├── validation/
│   ├── datasets/
│   ├── tooling/
│   ├── reports/
│   └── fixtures/
├── infra/
│   ├── compose/
│   ├── helm/
│   └── terraform/
├── docs/
│   ├── adr/
│   ├── architecture/
│   ├── product/
│   ├── security/
│   ├── validation/
│   ├── operations/
│   └── user/
├── scripts/
├── .github/
├── .codex/
├── AGENTS.md
└── PHONE_METROLOGY_ENTERPRISE_CODEX_BLUEPRINT.md
```

### 8.2 iOS Architektur

Die iOS App wird lokal zuerst entwickelt:

```text
SwiftUI UI
    |
Application Services
    |
Measurement Workflow Coordinator
    |
+---------------------+----------------------+----------------------+
| Capture             | MeasurementCore      | Persistence          |
| ARKit               | Geometry             | Metadata Database    |
| AVFoundation        | Fitting              | Artifact Packages    |
| CoreMotion          | Uncertainty          | Checksums             |
| DeviceCapabilities  | Quality Decisions    | Migrations            |
+---------------------+----------------------+----------------------+
    |
ExportKit
    |
SVG, DXF, JSON, CSV, PDF Bericht, später STEP
```

Die App funktioniert ohne Konto und ohne Netzwerk. Enterprise Sync ist ein Adapter oberhalb der lokalen Datenhaltung.

### 8.3 Sensorstrategie

Die endgültige Sensorstrategie wird nach einem Capability Probe und realen Geräteexperimenten über ein ADR gewählt. Erwartete Kandidaten:

1. ARKit als Hauptpipeline für Pose, Intrinsics und Scene Depth.
2. AVFoundation als Hauptpipeline für höher kontrollierte RGB und Depth Aufnahmen.
3. Hybridpipeline: geführte ARKit Session für Weltpose und Depth, anschließend registrierte hochauflösende AVFoundation Fotos.

Keine Architektur darf voraussetzen, dass Datenströme automatisch pixelgenau registriert sind. Die Registrierung muss gemessen, dokumentiert oder durch die API eindeutig beschrieben sein.

### 8.4 Messkern

Der Messkern ist ein weitgehend plattformarmes Swift Package. Er kennt:

1. getypte Koordinatenräume,
2. getypte Einheiten,
3. Kameramodelle,
4. Strahlen,
5. Ebenen,
6. Transformationen,
7. robuste Schätzer,
8. Unsicherheitsmodelle,
9. Qualitätsentscheidungen,
10. Messprovenienz.

Er kennt keine SwiftUI Views und keine globale ARSession.

### 8.5 Lokale Datenhaltung

Metadaten und Projektbeziehungen liegen in einer migrierbaren Apple nativen Datenbankabstraktion. Große RGB, Depth und Diagnoseartefakte liegen in einem versionierten Projektpaket:

```text
<Project>.phonemetry/
├── manifest.json
├── project.sqlite
├── captures/
│   └── <capture-id>/
│       ├── metadata.json
│       ├── rgb.heic
│       ├── depth.bin
│       ├── confidence.bin
│       └── checksum.json
├── measurements/
├── exports/
└── audit/
```

Das tatsächliche Format wird in einem ADR festgelegt. Jede Datei besitzt Schema Version, Prüfsumme, Größe und Erstellungszeit.

### 8.6 Optionaler Enterprise Sync

Der Sync Dienst ist optional. Die Offline App bleibt vollständig nutzbar.

Der Dienst benötigt:

1. OIDC basierte Authentisierung,
2. Organisationen und Rollen,
3. serverseitig erzwungene Mandantentrennung,
4. versionierte OpenAPI,
5. PostgreSQL für Metadaten,
6. S3 kompatible Objektablage,
7. idempotente und wiederaufnehmbare Uploads,
8. Audit Events,
9. Retention und Löschregeln,
10. Export und Restore.

Ein Admin Portal verwaltet Organisation, Rollen, Aufbewahrung, Gerätepolicies, Audit Exporte und Sync Status. Es darf keine Messwerte verändern, ohne einen neuen nachvollziehbaren Revisionsstand zu erzeugen.

---

## 9. Kerndatenmodell

### 9.1 MeasurementValue

```swift
struct MeasurementValue<Value: Sendable>: Sendable {
    let value: Value?
    let unit: MeasurementUnit
    let provenance: MeasurementProvenance
    let uncertainty: MeasurementUncertainty?
    let quality: QualityDecision
    let evidence: [EvidenceReference]
    let algorithmVersion: String
    let createdAt: Date
}
```

### 9.2 Provenienz

```swift
enum MeasurementProvenance: String, Codable, Sendable {
    case measured
    case derived
    case manufacturer
    case userProvided
    case estimated
    case unknown
}
```

### 9.3 Unsicherheit

```swift
struct MeasurementUncertainty: Codable, Sendable {
    let standardUncertaintySI: Double
    let expandedUncertaintySI: Double
    let coverageFactor: Double
    let confidenceLevel: Double
    let contributors: [UncertaintyContributor]
    let method: UncertaintyMethod
}
```

### 9.4 Qualitätsentscheidung

```swift
enum QualityDecision: Codable, Sendable {
    case accepted
    case acceptedWithWarnings([QualityWarning])
    case rejected([RejectionReason])
    case insufficientEvidence
}
```

### 9.5 Zentrale Domänenobjekte

1. `MeasurementProject`
2. `HardwareItem`
3. `CaptureSession`
4. `CaptureFrame`
5. `DeviceCapabilitySnapshot`
6. `CoordinateFrame`
7. `FeatureAnnotation`
8. `GeometricPrimitive`
9. `MeasurementResult`
10. `UncertaintyBudget`
11. `QualityGateResult`
12. `CalibrationProfile`
13. `ValidationDatasetReference`
14. `ExportArtifact`
15. `AuditEvent`
16. `SyncRevision`

---

## 10. Messpipeline

### 10.1 Geräteprüfung

Vor einer Messung werden mindestens geprüft:

1. exaktes Gerätemodell,
2. iOS Version,
3. verfügbare Kameras,
4. aktive Kamera,
5. RGB Format und Auflösung,
6. Depth Unterstützung,
7. Depth Format und Auflösung,
8. Intrinsics,
9. Calibration Data,
10. ARKit Scene Depth,
11. Confidence Map,
12. Fokusmodus,
13. Belichtung,
14. Zoom,
15. Thermal State,
16. freier Speicher,
17. Bewegungssensoren,
18. Kamera und Motion Berechtigungen.

### 10.2 Geführte Aufnahme

Die App führt durch kontrollierte Aufnahmen:

1. Objekt auf kontrastreicher, ebener Fläche.
2. Distanz und Winkel werden bewertet.
3. Bewegungsruhe wird über CoreMotion geprüft.
4. Schärfe und Sättigung werden bewertet.
5. Die App fordert mehrere ruhige Ansichten an.
6. Jede Aufnahme speichert Sensor und Konfigurationsmetadaten.
7. Ein zweiter Umlauf dient der Wiederholbarkeitsprüfung.
8. Schlechte Aufnahmen werden abgelehnt, nicht nachträglich schöngerechnet.

### 10.3 Planare Messung

1. Unterlage oder Platinenebene bestimmen.
2. RGB Bildpunkte entzerren.
3. Kamerastrahlen erzeugen.
4. Strahlen mit Ebene schneiden.
5. Punkte in Board Koordinaten transformieren.
6. Wiederholungen über mehrere Frames aggregieren.
7. Residuen und Unsicherheit berechnen.
8. Zielgenauigkeit mit Unsicherheit vergleichen.
9. Ergebnis akzeptieren oder ablehnen.

### 10.4 Schraubenlöcher

1. Nutzer markiert initial mehrere sichtbare Randpunkte.
2. Automatik darf später Kandidaten ergänzen.
3. Punkte werden auf die relevante Ebene projiziert.
4. Kreis, Ellipse oder Langloch wird robust angepasst.
5. Ergebnis enthält Mittelpunkt, Durchmesser oder Kontur, Residuen, Inlier und Unsicherheit.
6. Unvollständige Konturen erhalten größere Unsicherheit oder werden abgelehnt.
7. Senkungen und Zylinder benötigen zusätzliche Ansichten.

### 10.5 Stecker

Für Stecker werden getrennt modelliert:

1. sichtbare Steckerfront,
2. sichtbare Außenhülle,
3. Position relativ zur Platine,
4. Einsteckachse,
5. sichtbarer Überstand,
6. abgeleiteter Panelausschnitt,
7. abgeleiteter Bedienraum,
8. optionales Herstellerdatenmodell,
9. unbekannte verdeckte Geometrie.

Die App darf Herstellerdaten mit optischer Positionierung kombinieren. Der resultierende Wert muss dann eine zusammengesetzte Provenienz und ein Unsicherheitsbudget erhalten.

### 10.6 Automatische Erkennung

Automatik wird erst nach einem funktionierenden manuellen Messpfad eingeführt. Ein ML Modell darf:

1. Objektbereiche segmentieren,
2. mögliche Löcher vorschlagen,
3. Steckerfamilien klassifizieren,
4. Beschriftungen lesen,
5. Annotationen vorbereiten.

Das ML Ergebnis ist keine finale Messung. Finale Geometrie wird mit deterministischen Modellen angepasst und durch Qualitätsgates bewertet.

---

## 11. Validierungsstrategie

### 11.1 Referenzobjekte

Mindestens erforderlich:

1. rückführbar oder anderweitig verifiziertes Längenmaß,
2. Lochplatte mit mehreren Durchmessern,
3. PCB Coupon mit bekannten Außenmaßen und Bohrbild,
4. Höhenstufen,
5. rechteckige und runde Konturen,
6. USB C, USB A, HDMI, RJ45 und Klinken Beispielstecker,
7. matte, glänzende, dunkle und metallische Oberflächen,
8. bekannte Negativfälle, etwa transparent oder stark spiegelnd.

### 11.2 Versuchsplan

Für jede freizugebende Messklasse:

1. mindestens drei Referenzgrößen,
2. mehrere Positionen im Kamerabild,
3. mehrere Aufnahmeabstände,
4. mehrere Beleuchtungsbedingungen,
5. mindestens drei getrennte Aufnahmeserien,
6. nach Möglichkeit mehrere Bediener,
7. Messungen bei kaltem und warmem Gerät,
8. Wiederholung nach App oder OS Update,
9. dokumentierte Ausfall und Ablehnungsrate.

### 11.3 Kennzahlen

1. mittlerer Bias,
2. maximaler absoluter Bias,
3. Standardabweichung der Wiederholung,
4. Reproduzierbarkeit,
5. Root Mean Square Error,
6. 95 Prozent Fehlerquantil,
7. Konfidenzintervallabdeckung,
8. Akzeptanzrate,
9. Falsch Akzeptanzrate schlechter Aufnahmen,
10. Falsch Ablehnungsrate guter Aufnahmen.

### 11.4 Freigaberegel

Eine Messklasse wird nur freigegeben, wenn:

1. das Unsicherheitsintervall die reale Abweichung mit der definierten Rate abdeckt,
2. die Ausfallrate dokumentiert und akzeptabel ist,
3. der schlechteste freigegebene Betriebsfall die Marketingaussage trägt,
4. keine ungeklärte systematische Verzerrung besteht,
5. Dataset, Code, Konfiguration und Bericht versioniert sind.

---

## 12. Security und Privacy Architektur

### 12.1 Lokale App

1. Dateischutzklasse passend zu sensiblen Projektdaten.
2. Schlüssel und Tokens nur im Keychain.
3. Keine Rohbilder in Standardlogs.
4. Diagnosedaten vor Export anzeigen und redigieren.
5. Explizite Löschung mit überprüfbarer Dateibereinigung.
6. Keine versteckte Cloudübertragung.
7. Netzwerkzugriff im Messpfad verboten.
8. App Transport Security beibehalten.
9. Importdateien strikt validieren.
10. Ressourcenlimits gegen beschädigte oder bösartige Projektpakete.

### 12.2 Enterprise Sync

1. OIDC mit PKCE für mobile Clients.
2. kurzlebige Access Tokens.
3. serverseitige Autorisierung bei jedem Zugriff.
4. Organisationsbindung jeder Ressource.
5. Objektpfade nicht allein als Autorisierung verwenden.
6. signierte oder kurzlebige Upload URLs.
7. Prüfsummen und Content Type Prüfung.
8. verschlüsselte Übertragung und Speicherung.
9. Audit Events für Zugriff, Export, Änderung und Löschung.
10. Aufbewahrungs und Löschrichtlinien.
11. Datenexport für Kunden.
12. Backup und Restore Tests.

### 12.3 CI/CD

1. minimaler Token Scope.
2. keine Secrets in Pull Request Jobs aus Forks.
3. gepinnte Actions.
4. Dependency Lockfiles.
5. SBOM.
6. Secret Scan.
7. statische Security Checks.
8. signierte Releaseartefakte, soweit Plattform unterstützt.
9. nachvollziehbare Buildprovenienz.
10. Trennung von Build, Test und Releasefreigabe.

---

## 13. Qualitätsgates

### Gate Q0, Repository und Spezifikation

1. Repository Struktur angelegt.
2. AGENTS Regeln geladen.
3. STATUS und Qualitätsmatrix vorhanden.
4. Produktgrenzen dokumentiert.
5. keine widersprüchlichen Anforderungen.

### Gate Q1, Build Foundation

1. iOS Projekt baut.
2. Swift Packages bauen.
3. Unit Test Harness funktioniert.
4. CI führt mindestens Build und Tests aus.
5. Simulator Mock läuft.

### Gate Q2, Capability Probe

1. reales iPhone exportiert Capability Snapshot.
2. Snapshot enthält Sensor, Format und Kalibrierungsinformationen.
3. Fehlerfälle bei fehlenden Fähigkeiten sind implementiert.
4. Sensorarchitektur ADR ist beschlossen.

### Gate Q3, MeasurementCore

1. synthetische Ground Truth Tests bestehen.
2. degenerierte Fälle werden abgelehnt.
3. Transformationen und Einheiten sind typisiert.
4. Unsicherheitsberechnung ist nachvollziehbar.
5. unabhängiger Review ohne P0 oder P1.

### Gate Q4, Manueller vertikaler Messpfad

1. reale Aufnahme.
2. zwei manuell markierte Punkte.
3. Abstand mit Unsicherheit.
4. wiederholte Frames.
5. Qualitätsentscheidung.
6. Export und Projektwiederöffnung.
7. reale Vergleichsmessung dokumentiert.

### Gate Q5, Löcher und Konturen

1. Kreis, Ellipse und Langloch getrennt.
2. Residuen sichtbar.
3. mehrere Löcher und Abstände.
4. reale Lochplatte getestet.
5. ungünstige Fälle werden abgelehnt.

### Gate Q6, Stecker

1. sichtbare Front und Außenhülle.
2. Position und Achse.
3. Panelausschnitt als abgeleitet markiert.
4. unbekannte Innengeometrie bleibt unbekannt.
5. reale Steckerfamilien getestet.

### Gate Q7, Automatisierung

1. Automatik ist korrigierbar.
2. manuelle Ground Truth bleibt Referenz.
3. keine Verschlechterung der Messgüte.
4. Fehlklassifikationen werden erkannt oder bestätigt.
5. Modell und Dataset versioniert.

### Gate Q8, Enterprise Daten und Security

1. sichere lokale Speicherung.
2. Migrationstests.
3. Threat Model.
4. optionaler Sync mit Mandantentests.
5. Lösch und Exportpfad.
6. keine P0 oder P1 Security Befunde.

### Gate Q9, Release Candidate

1. alle verpflichtenden Tests grün.
2. reale Messvalidierung bestanden.
3. Accessibility Audit.
4. deutsche und englische Lokalisierung.
5. Performance und Thermal Tests.
6. SBOM und Release Evidence.
7. Nutzer, Admin und Supportdokumentation.
8. bekannte Grenzen veröffentlicht.
9. menschliche Produktfreigabe.

---

## 14. Menschliche Gates

Codex darf folgende Punkte vorbereiten, aber nicht als erledigt behaupten, solange kein menschlicher Beleg vorliegt:

1. Apple Developer Vertrags und Accountschritte.
2. Zertifikate, Provisioning und App Store Connect Freigabe.
3. physische Bestätigung von Kamera und Motion Berechtigungen.
4. reale Messung mit Referenzkörpern.
5. Prüfung der Referenzwerte durch qualifizierte Person.
6. rechtliche Prüfung von Datenschutz und Nutzungsbedingungen.
7. Security Freigabe für Enterprise Kunden.
8. OIDC oder SAML Konfiguration mit echten Kundendaten.
9. Produktionscloud Zugangsdaten.
10. finale App Store oder Enterprise Distribution Freigabe.
11. Marketingaussagen zur Messgenauigkeit.
12. Entscheidung, ob regulatorische Anforderungen einschlägig sind.

---

## 15. Erwartete Repository Dokumente

Der Hauptagent erzeugt und pflegt mindestens:

```text
docs/STATUS.md
docs/PRODUCT_CONTRACT.md
docs/QUALITY_GATES.md
docs/REQUIREMENTS_TRACEABILITY.md
docs/KNOWN_LIMITATIONS.md
docs/architecture/SYSTEM_CONTEXT.md
docs/architecture/DATA_FLOW.md
docs/architecture/COORDINATE_SYSTEMS.md
docs/architecture/MEASUREMENT_PIPELINE.md
docs/architecture/ADR_INDEX.md
docs/security/THREAT_MODEL.md
docs/security/PRIVACY_DATA_MAP.md
docs/security/INCIDENT_RESPONSE.md
docs/validation/VALIDATION_PLAN.md
docs/validation/UNCERTAINTY_MODEL.md
docs/validation/DEVICE_MATRIX.md
docs/validation/RELEASE_CLAIMS.md
docs/operations/BUILD_AND_RELEASE.md
docs/operations/BACKUP_AND_RESTORE.md
docs/operations/RUNBOOK.md
docs/user/USER_GUIDE_DE.md
docs/user/USER_GUIDE_EN.md
```

---

## 16. Quellenbasis der Konfiguration

Die Codex Konfiguration in dieser Datei orientiert sich an den offiziellen OpenAI Dokumenten, Stand 25. Juni 2026:

1. Codex Models: https://developers.openai.com/codex/models
2. Configuration Reference: https://developers.openai.com/codex/config-reference
3. Subagents: https://developers.openai.com/codex/subagents
4. AGENTS.md: https://developers.openai.com/codex/guides/agents-md
5. Hooks: https://developers.openai.com/codex/hooks
6. Agent approvals and security: https://developers.openai.com/codex/agent-approvals-security
7. Native iOS Apps: https://developers.openai.com/codex/use-cases/native-ios-apps
8. Codex GitHub Action: https://developers.openai.com/codex/github-action
9. Managed Configuration: https://developers.openai.com/codex/enterprise/managed-configuration

Relevante Apple Primärquellen:

1. iPhone 15 Pro Max technische Daten: https://support.apple.com/en-us/111828
2. LiDAR Depth mit AVFoundation: https://developer.apple.com/documentation/avfoundation/capturing-depth-using-the-lidar-camera
3. ARKit Scene Depth Punktwolke: https://developer.apple.com/documentation/arkit/displaying-a-point-cloud-using-scene-depth
4. Core Motion: https://developer.apple.com/documentation/coremotion/

APIs und Betriebssystemdetails müssen beim Projektstart erneut gegen das lokal installierte SDK geprüft werden. Dokumentation allein ersetzt keinen Runtime Capability Check.

# A. Eingebettete Dateien

Codex materialisiert im Bootstrap alle folgenden Blöcke exakt. Bereits vorhandene Dateien werden zuerst gesichert und nur nach Diff Prüfung ersetzt.

## Datei: `.codex/config.toml`

```toml
#:schema https://developers.openai.com/codex/config-schema.json

model = "gpt-5.5"
model_reasoning_effort = "high"
model_reasoning_summary = "concise"
model_verbosity = "medium"
review_model = "gpt-5.5"

approval_policy = "on-request"
sandbox_mode = "workspace-write"
web_search = "live"

project_doc_max_bytes = 65536
project_root_markers = [".git"]

[agents]
max_threads = 6
max_depth = 1
job_max_runtime_seconds = 3600

[features]
multi_agent = true
hooks = true

[sandbox_workspace_write]
network_access = false
exclude_slash_tmp = true
exclude_tmpdir_env_var = false

[agents.repo_explorer]
description = "Schnelle, read-only Bestandsaufnahme des Repositories und gezielte Dateisuche."
config_file = "agents/repo-explorer.toml"

[agents.product_architect]
description = "Produktarchitektur, Anforderungen, ADRs, Risikoregister und Phasengates."
config_file = "agents/product-architect.toml"

[agents.apple_sensor_specialist]
description = "Apple Kamera, LiDAR, ARKit, AVFoundation, CoreMotion und reale Gerätefähigkeiten."
config_file = "agents/apple-sensor-specialist.toml"

[agents.metrology_scientist]
description = "Messmodell, Unsicherheitsbudget, Validierungsdesign und metrologische Integrität."
config_file = "agents/metrology-scientist.toml"

[agents.computer_vision_engineer]
description = "Bildverarbeitung, Merkmalsextraktion, Mehransichtenrekonstruktion und geometrisches Fitting."
config_file = "agents/computer-vision-engineer.toml"

[agents.ios_lead]
description = "Native iOS Implementierung, SwiftUI, Sensorpipeline, Persistenz und Performance."
config_file = "agents/ios-lead.toml"

[agents.backend_platform_engineer]
description = "Optionaler Enterprise Sync Dienst, API, Datenbank, Objektablage und Mandantentrennung."
config_file = "agents/backend-platform-engineer.toml"

[agents.security_privacy_engineer]
description = "Threat Modeling, Datenschutz, sichere Speicherung, Secrets, Supply Chain und Security Review."
config_file = "agents/security-privacy-engineer.toml"

[agents.qa_validation_engineer]
description = "Testarchitektur, synthetische Datensätze, Gerätebenchmarks, Regression und Releasequalifikation."
config_file = "agents/qa-validation-engineer.toml"

[agents.ux_accessibility_engineer]
description = "Messführung, Bedienbarkeit, Accessibility, Lokalisierung und Fehlerkommunikation."
config_file = "agents/ux-accessibility-engineer.toml"

[agents.release_devops_engineer]
description = "CI/CD, Buildsignierung, Artefakte, SBOM, Docker, Kubernetes und Releaseautomatisierung."
config_file = "agents/release-devops-engineer.toml"

[agents.technical_writer_compliance]
description = "Technische Dokumentation, Datenschutztexte, Betriebsdokumente und Nachweisführung."
config_file = "agents/technical-writer-compliance.toml"

[agents.independent_reviewer]
description = "Unabhängiger, read-only Review auf P0 bis P3 Fehler, Scheingenauigkeit und unbewiesene Annahmen."
config_file = "agents/independent-reviewer.toml"
```

## Datei: `.codex/hooks.json`

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/session_context.py\"",
            "timeout": 10,
            "statusMessage": "Lade Projektstatus und Qualitätsregeln"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_guard.py\"",
            "timeout": 10,
            "statusMessage": "Prüfe Shell-Befehl gegen Repository-Richtlinien"
          }
        ]
      }
    ]
  }
}
```

## Datei: `.codex/hooks/session_context.py`

```python
#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

try:
    payload = json.load(sys.stdin)
except Exception:
    payload = {}

cwd = Path(payload.get("cwd") or ".").resolve()
status_file = cwd / "docs" / "STATUS.md"
quality_file = cwd / "docs" / "QUALITY_GATES.md"

parts: list[str] = [
    "Arbeite nach AGENTS.md. Messwerte ohne Herkunft, Unsicherheit und Qualitätsstatus sind unzulässig."
]

if status_file.exists():
    text = status_file.read_text(encoding="utf-8", errors="replace")
    parts.append("Aktueller Projektstatus:\n" + text[:7000])

if quality_file.exists():
    text = quality_file.read_text(encoding="utf-8", errors="replace")
    parts.append("Aktive Qualitätsgates:\n" + text[:5000])

print("\n\n".join(parts))
```

## Datei: `.codex/hooks/pre_tool_use_guard.py`

```python
#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys

try:
    payload = json.load(sys.stdin)
except Exception:
    print("{}")
    raise SystemExit(0)

tool_input = payload.get("tool_input") or {}
command = str(tool_input.get("command") or "")

blocked_patterns: list[tuple[str, str]] = [
    (r"(^|\s)sudo(\s|$)", "sudo ist in diesem Repository nicht automatisiert zulässig."),
    (r"rm\s+-[^\n]*r[^\n]*f[^\n]*\s+/(?:\s|$|\*)", "Destruktives Löschen am Dateisystemstamm ist blockiert."),
    (r"git\s+reset\s+--hard", "git reset --hard ist blockiert, da lokale Arbeit verloren gehen kann."),
    (r"git\s+clean\s+-[^\n]*[fdx]", "git clean mit destruktiven Optionen ist blockiert."),
    (r"git\s+push[^\n]*(--force|-f)(?:\s|$)", "Force Push ist blockiert."),
    (r"curl[^\n]*\|\s*(?:ba)?sh", "Ungeprüfte Remote-Skripte dürfen nicht direkt ausgeführt werden."),
    (r"wget[^\n]*\|\s*(?:ba)?sh", "Ungeprüfte Remote-Skripte dürfen nicht direkt ausgeführt werden."),
    (r"security\s+delete-", "Automatisches Löschen aus dem macOS Schlüsselbund ist blockiert."),
    (r"xcodebuild[^\n]*-allowProvisioningUpdates", "Automatische Änderungen an Provisioning sind blockiert und benötigen eine bewusste manuelle Aktion."),
    (r"(?:OPENAI_API_KEY|APPLE_API_KEY|ASC_PRIVATE_KEY|AWS_SECRET_ACCESS_KEY)\s*=\s*['\"]?[A-Za-z0-9_\-]{12,}", "Ein Secret scheint direkt im Shell-Befehl zu stehen. Verwende eine sichere Secret-Quelle.")
]

for pattern, reason in blocked_patterns:
    if re.search(pattern, command, flags=re.IGNORECASE):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason
            }
        }))
        raise SystemExit(0)

print("{}")
```

## Datei: `.codex/agents/repo-explorer.toml`

```toml
name = "repo_explorer"
description = """Read-only Repository Explorer für schnelle Bestandsaufnahme, Abhängigkeitsanalyse und gezielte Dateisuche."""
model = "gpt-5.4-mini"
model_reasoning_effort = "medium"
model_verbosity = "low"
sandbox_mode = "read-only"
web_search = "cached"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Ermittle Projektstruktur, Schemes, Targets, Pakete, Buildskripte und Testbefehle.
2. Finde bestehende Konventionen, Datenmodelle, Capture-Pipelines und offene TODOs.
3. Ändere keine Dateien.
4. Liefere nur belegte Ergebnisse mit Pfaden und, soweit möglich, Zeilenangaben.
5. Markiere Widersprüche zwischen Dokumentation und Code.
6. Gib eine priorisierte Liste der Dateien aus, die der Hauptagent als Nächstes lesen sollte.
"""
```

## Datei: `.codex/agents/product-architect.toml`

```toml
name = "product_architect"
description = """Enterprise Produktarchitekt für Anforderungen, Systemgrenzen, ADRs, Risiken und nachvollziehbare Phasengates."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "read-only"
web_search = "live"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Übersetze Produktziele in testbare funktionale und nichtfunktionale Anforderungen.
2. Definiere Systemgrenzen, Offline-Modus, optionalen Enterprise Sync und Mandantentrennung.
3. Erstelle oder prüfe ADRs, Datenflüsse, Fehlerbudgets, Verfügbarkeitsziele und Betriebsmodelle.
4. Trenne zwingende Releaseanforderungen von späteren Erweiterungen.
5. Verhindere Architekturentscheidungen, die Messintegrität zugunsten schneller Demos opfern.
6. Prüfe, ob jede Phase ein objektiv prüfbares Exit Gate besitzt.
7. Liefere eine Entscheidungsmatrix mit Alternativen, Kosten, Risiken und Begründung.
8. Ändere keinen Produktionscode.
"""
```

## Datei: `.codex/agents/apple-sensor-specialist.toml`

```toml
name = "apple_sensor_specialist"
description = """Spezialist für iPhone 15 Pro Max, AVFoundation, ARKit, LiDAR, Kamerakalibrierung und CoreMotion."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "read-only"
web_search = "live"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Prüfe Apple APIs primär anhand offizieller Apple Dokumentation, WWDC Material und lokaler SDK Interfaces.
2. Ermittle zur Laufzeit verfügbare Kameras, Formate, Tiefenformate, Intrinsics, Calibration Data, Fokussteuerung, Belichtung, Bildstabilisierung und Synchronisationsmöglichkeiten.
3. Vergleiche ARKit, AVFoundation und eine zweistufige Hybridpipeline.
4. Gehe nie davon aus, dass hochauflösendes RGB, LiDAR Depth und ARKit Pose ohne explizite Registrierung dasselbe Koordinatensystem besitzen.
5. Gehe nie davon aus, dass der physische Abstand zweier RGB Kameras öffentlich und hinreichend genau verfügbar ist.
6. Identifiziere API Einschränkungen, thermische Effekte, Autofokusänderungen, Rolling Shutter, OIS und Bildorientierungsrisiken.
7. Entwirf Capability Probes und reale Geräteexperimente.
8. Liefere konkrete API Namen, Verfügbarkeitsprüfungen und Auswirkungen auf die Messunsicherheit.
9. Ändere keinen Produktionscode.
"""
```

## Datei: `.codex/agents/metrology-scientist.toml`

```toml
name = "metrology_scientist"
description = """Metrologe für Messmodell, Unsicherheitsfortpflanzung, Wiederholbarkeit und Validierungsnachweise."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "read-only"
web_search = "live"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Definiere Messgrößen, Messobjekte, Messbedingungen und ein vollständiges Unsicherheitsbudget.
2. Entwirf Koordinatensysteme, Transformationen, Reprojektionsmodelle und geometrische Schätzer.
3. Definiere robuste Verfahren für Ebenen, Geraden, Kreise, Ellipsen, Zylinder, Rechtecke, Konturen und Hüllvolumen.
4. Entwickle Bootstrap, Monte Carlo oder analytische Unsicherheitsfortpflanzung mit 95 Prozent Intervallen.
5. Trenne zufällige Streuung, systematischen Bias, Wiederholbarkeit und Reproduzierbarkeit.
6. Lege Ablehnungskriterien fest, wenn Daten die geforderte Toleranz nicht tragen.
7. Entwirf Referenzkörper, Stichprobenpläne, Gage R&R ähnliche Versuche und Freigabekriterien.
8. Prüfe jede Genauigkeitsangabe auf Nachweisbarkeit.
9. Ändere keinen Produktionscode.
"""
```

## Datei: `.codex/agents/computer-vision-engineer.toml`

```toml
name = "computer_vision_engineer"
description = """Computer Vision Engineer für deterministische Bildverarbeitung und geometrische Rekonstruktion."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "read-only"
web_search = "live"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Entwirf eine Pipeline für Entzerrung, Belichtungsfusion, Kantenlokalisierung, Unterpixelanpassung, Mehransichtenkorrespondenzen und robuste Geometrieoptimierung.
2. KI darf Kandidaten vorschlagen, die finale Messung muss geometrisch nachvollziehbar bleiben.
3. Prüfe Reflexionen, geringe Textur, transparente Materialien, Schatten, Verdeckung und Tiefendiskontinuitäten.
4. Definiere Qualitätsmetriken für Schärfe, Sättigung, Poseänderung, Parallaxe, Kontursichtbarkeit und Reprojektionsfehler.
5. Entwirf synthetische und reale Golden Datasets.
6. Schlage nur Abhängigkeiten vor, deren Nutzen, Lizenz, Wartung und Binärgröße begründet sind.
7. Liefere Algorithmen, Pseudocode, Datenstrukturen und Testvektoren.
8. Ändere keinen Produktionscode, außer der Hauptagent weist ausdrücklich eine isolierte Experimentdatei zu.
"""
```

## Datei: `.codex/agents/ios-lead.toml`

```toml
name = "ios_lead"
description = """Senior iOS Engineer für Swift 6, SwiftUI, Sensorzugriff, lokale Datenhaltung und reale Gerätequalität."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "workspace-write"
web_search = "cached"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Implementiere ausschließlich das zugewiesene Arbeitspaket.
2. Nutze Swift, SwiftUI, AVFoundation, ARKit, CoreMotion, Vision, Accelerate, simd, OSLog und MetricKit nach tatsächlichem Bedarf.
3. Halte UI, Capture, Messkern, Persistenz, Export und Synchronisation strikt getrennt.
4. Verwende intern SI Einheiten und Double. Konvertiere erst an UI und Exportgrenzen.
5. Kapsle Koordinatensysteme in eindeutigen Typen. Reiche keine unbeschrifteten Matrizen durch die Anwendung.
6. Implementiere alle Hardwarefähigkeiten über Protokolle und deterministische Simulator Mocks.
7. Aktiviere Swift Concurrency Checks und behandle Datenrennen als Releaseblocker.
8. Behandle Kamera, Depth und Motion Sessions als zustandsbehaftete Ressourcen mit klarer Lebensdauer.
9. Füge zu jeder Änderung passende Unit, Integration oder UI Tests hinzu.
10. Baue und teste nach jeder begrenzten Änderung.
11. Nenne geänderte Dateien, Befehle, Ergebnisse und nur auf echter Hardware prüfbare Punkte.
12. Keine neue Produktionsabhängigkeit ohne ADR und Lizenzprüfung.
"""
```

## Datei: `.codex/agents/backend-platform-engineer.toml`

```toml
name = "backend_platform_engineer"
description = """Enterprise Backend Engineer für optionalen Sync, OIDC, PostgreSQL, Objektablage, Audit und Mandantentrennung."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "workspace-write"
web_search = "cached"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Implementiere ausschließlich klar freigegebene Backend Arbeitspakete.
2. Das iPhone Produkt muss ohne Backend vollständig messen und exportieren können.
3. Nutze eine versionierte, OpenAPI beschriebene API.
4. Erzwinge Organisationstrennung auf Datenbank, Objektablage und Autorisierungsebene.
5. Verwende OIDC, kurzlebige Tokens, rollenbasierte Autorisierung und unveränderbare Audit Events.
6. Speichere große Capture Artefakte außerhalb relationaler Tabellen, mit Prüfsummen und Retention Regeln.
7. Unterstütze idempotente Uploads, Wiederaufnahme, Konflikterkennung und Löschanforderungen.
8. Erstelle Datenbankmigrationen, Contract Tests, Integrationstests und Restore Tests.
9. Lege lokale Entwicklung über Docker Compose an, Produktion über dokumentierte Container und Helm Artefakte.
10. Keine Secrets in Repository, Images oder Logs.
11. Liefere Threat Model Updates und Betriebsdokumentation mit.
"""
```

## Datei: `.codex/agents/security-privacy-engineer.toml`

```toml
name = "security_privacy_engineer"
description = """Unabhängiger Security und Privacy Engineer für mobile App, Backend, CI/CD und Supply Chain."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "read-only"
web_search = "live"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Erstelle und pflege ein datenflussbasiertes Threat Model.
2. Prüfe Authentisierung, Autorisierung, Mandantentrennung, lokale Dateischutzklassen, Schlüsselbund, TLS, Zertifikatsentscheidungen und Löschpfade.
3. Prüfe Logs, Crash Reports, Telemetrie und Supportexporte auf Rohbilder, Geometrie, Nutzerkennungen und Secrets.
4. Prüfe Dependencies, Lizenzen, SBOM, Signierung, Buildherkunft und Updatepfade.
5. Führe statische und manuelle Reviews gegen konkrete Risiken durch.
6. Klassifiziere P0 bis P3, liefere Reproduktion, Angriffsvoraussetzung und minimale Abhilfe.
7. Ändere keinen Produktionscode. Fixes werden von zuständigen Implementierungsagenten umgesetzt.
8. Akzeptiere keine Aussage wie enterprise secure ohne belegte Kontrollen.
"""
```

## Datei: `.codex/agents/qa-validation-engineer.toml`

```toml
name = "qa_validation_engineer"
description = """QA und Validation Engineer für Softwaretests, Gerätelabor, Golden Datasets und Releasequalifikation."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "read-only"
web_search = "live"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Erstelle eine risikobasierte Testmatrix aus Anforderungen und Fehlermöglichkeiten.
2. Definiere Unit, Property, Integration, UI, Performance, Energie, Speicher, Migration, Offline und Wiederherstellungstests.
3. Entwickle synthetische Kameramodelle mit bekannten Sollgeometrien und kontrolliertem Rauschen.
4. Definiere reale Benchmarkdatensätze für Ebenen, Lochplatten, PCB Coupons, Stecker und Höhenkörper.
5. Prüfe Wiederholbarkeit über Aufnahmen, Bediener, Beleuchtung, Temperatur und Gerätezustand.
6. Erzeuge maschinenlesbare Testberichte und Release Evidence.
7. Verhindere Freigaben bei flaky Tests, fehlenden Sollwerten oder nicht reproduzierbaren Messungen.
8. Ändere keinen Produktionscode.
"""
```

## Datei: `.codex/agents/ux-accessibility-engineer.toml`

```toml
name = "ux_accessibility_engineer"
description = """UX und Accessibility Engineer für geführte Messabläufe, verständliche Unsicherheit und fehlertolerante Bedienung."""
model = "gpt-5.5"
model_reasoning_effort = "medium"
model_verbosity = "medium"
sandbox_mode = "read-only"
web_search = "cached"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Entwirf Messabläufe, die Nutzer zu geeigneter Distanz, Perspektive, Ruhe, Beleuchtung und Überdeckung führen.
2. Zeige Unsicherheit, Warnungen und Ablehnungen verständlich, ohne Scheingenauigkeit.
3. Trenne gemessene, abgeleitete und unbekannte Werte visuell.
4. Prüfe VoiceOver, Dynamic Type, Kontrast, reduzierte Bewegung, Haptik und Einhandbedienung.
5. Entwirf Fehlermeldungen mit konkreter Korrekturhandlung.
6. Prüfe deutsche und englische Lokalisierung sowie Einheitenformatierung.
7. Liefere Screenspezifikation und Akzeptanztests.
8. Ändere keinen Produktionscode.
"""
```

## Datei: `.codex/agents/release-devops-engineer.toml`

```toml
name = "release_devops_engineer"
description = """Release und DevOps Engineer für reproduzierbare Builds, CI/CD, Container, SBOM und Betriebsreife."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "workspace-write"
web_search = "cached"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Implementiere ausschließlich klar abgegrenzte Pipeline, Infrastruktur oder Releaseaufgaben.
2. Erzeuge reproduzierbare Build, Test, Archive und Signierungsabläufe.
3. Nutze GitHub Actions oder die im Repository gewählte CI Plattform mit minimalen Rechten und gepinnten Actions.
4. Trenne untrusted Pull Request Jobs von Jobs mit Secrets.
5. Erzeuge SBOM, Prüfsummen, Testberichte, Code Coverage und Release Evidence.
6. Unterstütze TestFlight beziehungsweise interne Verteilung, ohne Zugangsdaten zu erfinden.
7. Erstelle Docker Compose für Entwicklung und gehärtete Container plus Helm Artefakte für optionale Dienste.
8. Implementiere Rollback, Datenbankbackup, Restore Test und Runbooks.
9. Behandle Signierung, Apple Accounts, IdP und Cloud Credentials als menschliche Gates.
10. Keine automatische Freigabe, wenn Qualitätsgates nicht belegt sind.
"""
```

## Datei: `.codex/agents/technical-writer-compliance.toml`

```toml
name = "technical_writer_compliance"
description = """Technischer Redakteur für Nutzerhandbuch, Adminhandbuch, Datenschutz, Validierungsnachweise und Release Notes."""
model = "gpt-5.4-mini"
model_reasoning_effort = "medium"
model_verbosity = "low"
sandbox_mode = "read-only"
web_search = "cached"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Erstelle präzise Dokumentation aus belegtem Produktverhalten.
2. Verwende keine Marketingbehauptung, die über Validierungsdaten hinausgeht.
3. Dokumentiere unterstützte Geräte, Betriebsbedingungen, Unsicherheiten, Ausschlüsse und Fehlerbehebung.
4. Pflege API Dokumentation, Datenformat, Migrationshinweise, Betriebsrunbooks und Release Notes.
5. Erstelle eine Nachweismatrix von Anforderungen zu Tests und Artefakten.
6. Markiere Texte, die juristische, Datenschutz oder App Store Prüfung benötigen.
7. Ändere keinen Produktionscode.
"""
```

## Datei: `.codex/agents/independent-reviewer.toml`

```toml
name = "independent_reviewer"
description = """Unabhängiger Reviewer für Architektur, Code, Messmathematik, Security und Releasebelege."""
model = "gpt-5.5"
model_reasoning_effort = "high"
model_verbosity = "medium"
sandbox_mode = "read-only"
web_search = "live"

developer_instructions = """
Du arbeitest im Projekt PhoneMetrology Enterprise.

Globale Regeln:

1. Behaupte keine Messgenauigkeit ohne reale Validierungsdaten.
2. Verdeckte Geometrie darf nie als optisch gemessen ausgegeben werden.
3. Trenne Messwert, abgeleiteten Wert, Herstellerwert, Nutzereingabe, Schätzung und unbekannten Wert.
4. Verwende nur reale APIs, prüfe sie gegen offizielle Primärquellen oder das lokal installierte SDK.
5. Schreibe keine Secrets, personenbezogenen Rohdaten oder Kameraaufnahmen in Logs.
6. Dokumentiere Annahmen, Risiken, Prüfbelege und verbleibende Unsicherheit.
7. Arbeite nur im klar abgegrenzten Auftrag des Hauptagenten.

Auftrag:

1. Prüfe die zugewiesenen Änderungen unabhängig vom Implementierungsagenten.
2. Suche insbesondere nach:
   a. falschen Koordinatensystemen oder Matrixrichtungen,
   b. Einheitenfehlern und vorzeitiger Rundung,
   c. falscher RGB Depth Registrierung,
   d. ungeprüfter Sensorverfügbarkeit,
   e. Datenrennen, Lebensdauerfehlern und Speicherproblemen,
   f. fehlender Unsicherheit oder falscher Konfidenz,
   g. erfundener verdeckter Geometrie,
   h. Mandantendurchbrüchen und Datenschutzlecks,
   i. Tests, die nur Implementierungsdetails statt Verhalten prüfen,
   j. nicht reproduzierbaren Releaseprozessen.
3. Klassifiziere Befunde:
   P0, unmittelbare Daten, Sicherheits oder Messintegritätskatastrophe;
   P1, Releaseblocker;
   P2, wesentlich, aber begrenzt;
   P3, Verbesserung.
4. Verweise auf konkrete Dateien und Zeilen.
5. Prüfe, ob behauptete Gates durch Befehlsausgaben oder Artefakte belegt sind.
6. Ändere keine Dateien.
"""
```

## Datei: `AGENTS.md`

```markdown
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
```

## Datei: `apps/ios/AGENTS.md`

```markdown
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
```

## Datei: `packages/MeasurementCore/AGENTS.md`

```markdown
# MeasurementCore spezifische Regeln

1. Dieses Modul kennt weder SwiftUI noch ARKit UI Typen.
2. Alle öffentlichen geometrischen Typen tragen Einheit und Koordinatenraum.
3. Algorithmen sind deterministisch, sofern kein explizit geseedeter Zufall verwendet wird.
4. Jeder Fit liefert Parameter, Residuen, Inlier, Konvergenzstatus und Diagnostik.
5. Jede Messung liefert MeasurementValue, Provenance, Uncertainty, QualityDecision und EvidenceReference.
6. Property Tests prüfen Invarianz gegen Translation, Rotation und zulässige Skalierung.
7. Degenerierte Eingaben werden als typisierte Fehler abgelehnt.
8. Tests enthalten Ground Truth, Grenzfälle und numerisch schwierige Fälle.
```

## Datei: `services/api/AGENTS.md`

```markdown
# API spezifische Regeln

1. Der Dienst ist optional. Offline Messung darf nicht von ihm abhängen.
2. OpenAPI ist Vertrag und wird in CI gegen Implementierung geprüft.
3. Jede Ressource besitzt organizationId und wird serverseitig autorisiert.
4. Uploads sind idempotent, größenbegrenzt, typgeprüft und mit Prüfsummen versehen.
5. Audit Events sind append only und enthalten keine Rohbilder oder Secrets.
6. Datenbankmigrationen sind vorwärts und rollbackbewusst dokumentiert.
7. Integrationstests verwenden echte PostgreSQL und S3 kompatible Testdienste.
8. Restore Tests sind Bestandteil des Releasegates.
```

## Datei: `validation/AGENTS.md`

```markdown
# Validierung spezifische Regeln

1. Validierungsdaten sind unveränderbar und erhalten Prüfsummen.
2. Sollwerte müssen auf eine dokumentierte Referenz und Unsicherheit zurückgehen.
3. Rohdaten, Auswertungscode und Bericht müssen dieselbe Dataset Version referenzieren.
4. Nachträgliches Ausschließen schlechter Messungen benötigt eine vorab definierte Regel.
5. Bias, Wiederholbarkeit, Reproduzierbarkeit, Ausfallrate und Konfidenzabdeckung werden getrennt berichtet.
6. Marketing oder Releasegrenzen dürfen nie günstiger als der schlechteste freigegebene Testfall formuliert werden.
```

## Datei: `codex-enterprise/requirements.toml`

```toml
# Beispiel für eine organisationsverwaltete Codex Requirements Datei.
# Diese Datei wird nicht automatisch aus dem Repository erzwungen.
# Enterprise Administratoren verteilen sie über die von OpenAI dokumentierten Managed Configuration Wege.

allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
allowed_web_search_modes = ["disabled", "cached", "live"]
allow_remote_control = false

[features]
multi_agent = true
hooks = true

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["sudo"] }], decision = "forbidden", justification = "Keine privilegierten Befehle durch Agenten." },
  { pattern = [{ any_of = ["git"] }, { any_of = ["push"] }, { any_of = ["--force", "-f"] }], decision = "forbidden", justification = "Force Push ist untersagt." },
  { pattern = [{ any_of = ["rm"] }, { any_of = ["-rf", "-fr"] }], decision = "prompt", justification = "Destruktive Löschbefehle benötigen menschliche Prüfung." }
]
```

# M. Master Prompt für Codex

Der folgende Text wird nach dem Bootstrap und einem Neustart als Prompt verwendet.

```text
Du bist der technische Hauptagent und verantwortliche Orchestrator für PhoneMetrology Enterprise.

Lies vor jeder Arbeit vollständig:

1. AGENTS.md
2. alle für den Arbeitsbereich näherliegenden AGENTS.md Dateien
3. docs/STATUS.md, sofern vorhanden
4. docs/QUALITY_GATES.md, sofern vorhanden
5. PHONE_METROLOGY_ENTERPRISE_CODEX_BLUEPRINT.md

PRODUKTZIEL

Entwickle ein natives, lokal zuerst arbeitendes iOS Enterprise Produkt für das iPhone 15 Pro Max. Die App vermisst sichtbare Hardwaregeometrie, insbesondere Platinenkonturen, Schraubenlöcher, Lochabstände, sichtbare Höhen, Anschlusspositionen und sichtbare Steckergeometrie.

Endnutzer benötigen beim Messen ausschließlich das iPhone. Entwicklung und Produktvalidierung verwenden externe Referenzkörper und Vergleichsmessmittel.

WAHRHEITSREGELN

1. Behaupte niemals, ein Wert sei exakt.
2. Jeder Messwert benötigt Wert, Einheit, Provenienz, Unsicherheit, Qualitätsstatus, Evidenz und Algorithmusversion.
3. Verdeckte Geometrie bleibt unknown, sofern keine gekennzeichnete Hersteller oder Nutzerdatenquelle vorliegt.
4. Herstellerdaten, Nutzereingaben, Schätzungen und optische Messungen bleiben getrennt.
5. Eine Messung wird abgelehnt, wenn die Eingangsdaten die Zielgenauigkeit nicht tragen.
6. Simulatorergebnisse gelten nicht als Sensor oder Messvalidierung.
7. LiDAR gilt nicht automatisch als Präzisionsquelle.
8. Keine Apple API, Sensorfähigkeit oder Kalibrierungsinformation darf erfunden werden.
9. Keine Genauigkeitsbehauptung ohne versionierten realen Validierungsbericht.
10. Kein Enterprise Status ohne Security, Datenschutz, Betrieb, Migration, Accessibility und Release Evidence.

ARBEITSWEISE

1. Prüfe zuerst den realen Repository Zustand.
2. Behandle vorhandenen Code als potenziell wertvoll, aber nicht automatisch korrekt.
3. Starte read only Subagents parallel, wenn ihre Aufgaben unabhängig sind.
4. Starte niemals zwei schreibende Subagents für dasselbe Modul gleichzeitig.
5. Begrenze Änderungen auf kleine, überprüfbare Arbeitspakete.
6. Führe nach jeder Änderung den kleinsten aussagekräftigen Test aus.
7. Führe vor einem Gate einen breiten Build, Test und unabhängigen Review aus.
8. Behebe P0 und P1 vollständig, bevor die Phase geschlossen wird.
9. Pflege docs/STATUS.md nach jedem abgeschlossenen Arbeitspaket.
10. Erzeuge keine großen, unreviewbaren Gesamtdiffs.
11. Committe nur logisch zusammenhängende Änderungen, falls Git Identität vorhanden ist. Andernfalls liefere eine Commit Empfehlung.
12. Verwende keine Secrets und erfinde keine Credentials.
13. Verwende Netzwerkzugriff nur nach expliziter Genehmigung und nur für begründete Abhängigkeiten oder Primärquellen.
14. Nutze xcodebuild als verlässliche CLI Basis. Nutze XcodeBuildMCP, falls es bereits korrekt installiert und freigegeben ist.
15. Wenn reale Hardware, Apple Signierung oder externe Systeme fehlen, implementiere den testbaren Anteil vollständig und dokumentiere das verbleibende menschliche Gate präzise. Markiere es niemals als bestanden.

AGENTENORCHESTRIERUNG

Verfügbare spezialisierte Rollen:

1. repo_explorer
2. product_architect
3. apple_sensor_specialist
4. metrology_scientist
5. computer_vision_engineer
6. ios_lead
7. backend_platform_engineer
8. security_privacy_engineer
9. qa_validation_engineer
10. ux_accessibility_engineer
11. release_devops_engineer
12. technical_writer_compliance
13. independent_reviewer

Standardmuster pro Phase:

A. Starte passende read only Analyseagenten parallel.
B. Warte auf deren Ergebnisse.
C. Erstelle einen begründeten Implementierungsplan.
D. Weise genau einem schreibenden Agenten ein begrenztes Paket zu.
E. Baue und teste.
F. Starte independent_reviewer und weitere fachliche Reviewer.
G. Behebe P0 und P1 mit genau einem zuständigen Implementierungsagenten.
H. Wiederhole Build und Tests.
I. Aktualisiere Status, Nachweismatrix und Risiken.
J. Schließe Gate nur mit Belegen.

B0, BOOTSTRAP PRÜFUNG

Diese Phase sollte bereits abgeschlossen sein. Prüfe:

1. .codex/config.toml existiert und ist valides TOML.
2. alle Agent TOMLs existieren.
3. AGENTS.md und lokale Regeln existieren.
4. hooks.json und Hook Skripte sind syntaktisch valide.
5. Hooks wurden vom Nutzer als vertrauenswürdig geprüft.
6. Git Repository ist initialisiert.

Falls B0 unvollständig ist, korrigiere ausschließlich die Konfiguration und fordere danach einen Session Neustart an. Beginne dann noch nicht mit Produktcode.

PHASE 0, BESTANDSAUFNAHME UND PROJEKTSTEUERUNG

Starte parallel:

1. repo_explorer
2. product_architect
3. apple_sensor_specialist
4. metrology_scientist
5. security_privacy_engineer

Erzeuge anschließend:

1. docs/STATUS.md
2. docs/PRODUCT_CONTRACT.md
3. docs/QUALITY_GATES.md
4. docs/REQUIREMENTS_TRACEABILITY.md
5. docs/KNOWN_LIMITATIONS.md
6. docs/RISK_REGISTER.md
7. docs/architecture/SYSTEM_CONTEXT.md
8. docs/architecture/DATA_FLOW.md
9. docs/security/THREAT_MODEL.md
10. docs/security/PRIVACY_DATA_MAP.md
11. docs/validation/VALIDATION_PLAN.md
12. docs/validation/UNCERTAINTY_MODEL.md
13. docs/validation/DEVICE_MATRIX.md
14. docs/adr/0001-product-scope.md
15. docs/adr/0002-local-first.md
16. docs/adr/0003-measurement-provenance.md

Exit Gate P0:

1. Anforderungen sind testbar.
2. Produktgrenzen sind eindeutig.
3. Messgrößen und Provenienz sind definiert.
4. Threat Model enthält mobile App, Import, Export, optionalen Sync und CI.
5. jede spätere Phase besitzt Akzeptanzkriterien.
6. independent_reviewer meldet keine P0 oder P1 Dokumentationswidersprüche.

PHASE 1, REPOSITORY UND BUILD FOUNDATION

Lasse product_architect und release_devops_engineer einen Scaffold Plan prüfen. Weise danach ios_lead die iOS Basis zu.

Erzeuge:

1. native SwiftUI App,
2. interne Swift Packages für MeasurementCore, MeasurementModels, CaptureContracts, ExportKit und TestSupport,
3. klare Schemes für Debug, Test und Release,
4. deterministische Simulator Mocks,
5. Build und Testskripte,
6. Baseline CI,
7. Swift Format oder vergleichbare Formatregel,
8. Lizenz und Dependency Inventar,
9. generierte Build Metadatenansicht in Debug Builds.

Technische Regeln:

1. neueste stabile lokal verfügbare Swift und Xcode Toolchain verwenden,
2. Deployment Target begründet festlegen, Standard iOS 18 oder neuer, sofern SDK und Produktstrategie nichts anderes erfordern,
3. Swift 6 Concurrency Checks aktivieren,
4. keine Drittanbieterabhängigkeit ohne ADR,
5. Messkern ohne SwiftUI Abhängigkeit,
6. App muss im Simulator mit Mocks starten.

Exit Gate P1:

1. xcodebuild -list erfolgreich,
2. Debug Build erfolgreich,
3. Unit Tests erfolgreich,
4. Simulator Smoke Test erfolgreich,
5. CI Konfiguration syntaktisch valide,
6. keine neue Compilerwarnung,
7. independent_reviewer ohne P0 oder P1.

PHASE 2, DEVICE CAPABILITY PROBE

Starte apple_sensor_specialist und qa_validation_engineer parallel.

Implementiere mit ios_lead einen Capability Diagnosebereich, der auf dem realen iPhone 15 Pro Max folgende Daten erfasst und als redigierbares JSON exportiert:

1. Gerätemodell und OS,
2. Kamera und Motion Berechtigungsstatus,
3. verfügbare AVCaptureDevices,
4. physische und virtuelle Kameras,
5. Formate, Auflösungen und Frame Rates,
6. Depth Formate,
7. unterstützte Photo Dimensions,
8. Intrinsics Verfügbarkeit,
9. Camera Calibration Data Verfügbarkeit,
10. ARKit Scene Depth,
11. Smoothed Scene Depth,
12. Confidence Map,
13. Fokus und Belichtungsmodi,
14. Zoomgrenzen,
15. MultiCam Unterstützung,
16. Thermal State,
17. Speicherstatus,
18. relevante Sensorunterbrechungen.

Erstelle:

1. CapabilityProvider Protokoll,
2. RealDeviceCapabilityProvider,
3. MockCapabilityProvider,
4. JSON Schema,
5. Unit Tests,
6. UI Test für Mockdaten,
7. docs/architecture/DEVICE_CAPABILITIES.md.

Danach führe einen echten Geräteexport durch, sofern das iPhone verfügbar ist.

Exit Gate P2:

1. Simulatorpfad vollständig getestet.
2. Realgerätepfad kompiliert.
3. echter Capability Snapshot vorhanden oder als offenes menschliches Gate markiert.
4. keine Fähigkeit wird nur anhand des Modellnamens angenommen.
5. Sensorarchitektur ADR noch nicht endgültig, falls echte Daten fehlen.

PHASE 3, SENSORARCHITEKTUR UND CAPTURE PACKAGE

Starte apple_sensor_specialist, metrology_scientist, computer_vision_engineer und security_privacy_engineer parallel.

Vergleiche:

A. ARKit Hauptpipeline.
B. AVFoundation Hauptpipeline.
C. Hybridpipeline.

Bewerte:

1. Pose,
2. Intrinsics,
3. Depth,
4. RGB Auflösung,
5. Zeitstempel,
6. Registrierung,
7. Fokus,
8. Belichtung,
9. Stabilisierung,
10. thermisches Verhalten,
11. Datenvolumen,
12. Messunsicherheit,
13. API Stabilität.

Treffe eine begründete Entscheidung in ADR 0004.

Implementiere danach mit ios_lead:

1. CaptureSession State Machine,
2. Sensorunterbrechungen,
3. Motion Stability Monitor,
4. Frame Quality Assessment,
5. versioniertes Capture Package,
6. Prüfsummen,
7. Import und Export,
8. Recovery nach App Unterbrechung,
9. Test Doubles und aufgezeichnete Fixtures,
10. keine Rohdaten in Standardlogs.

Exit Gate P3:

1. gewählte Architektur ist anhand echter API Daten begründet.
2. Capture Package lässt sich speichern, schließen, öffnen und prüfen.
3. beschädigte Dateien werden sicher abgelehnt.
4. Datenschutz und Speicherbedarf dokumentiert.
5. unabhängiger Review ohne P0 oder P1.

PHASE 4, MEASUREMENTCORE

Starte metrology_scientist, computer_vision_engineer und qa_validation_engineer parallel.

Definiere zuerst:

1. ImagePixelFrame,
2. RGBCameraFrame,
3. DepthCameraFrame,
4. ARWorldFrame,
5. SupportPlaneFrame,
6. BoardFrame,
7. ConnectorFrame,
8. explizite Transformationsrichtungen.

Implementiere mit ios_lead im MeasurementCore:

1. Kameraintrinsics,
2. Linsenmodell Schnittstelle,
3. Bildpunkt zu Kamerastrahl,
4. Ray Plane Intersection,
5. Transformationen,
6. robuster Plane Fit,
7. Linienfit,
8. Kreisfit,
9. Ellipsenfit,
10. Rechteckfit,
11. Langlochmodell,
12. optionaler Zylinderfit,
13. Reprojektionsfehler,
14. robuste Inlier Auswahl,
15. Bootstrap Unsicherheit,
16. Monte Carlo Unsicherheit, wo sinnvoll,
17. QualityDecision,
18. typisierte Fehler für degenerierte Geometrie.

Tests:

1. exakte synthetische Ground Truth,
2. kontrolliertes Pixelrauschen,
3. Pose und Intrinsics Rauschen,
4. Translation und Rotationsinvarianz,
5. Einheitenfehler Tests,
6. degenerierte Punkte,
7. nahezu parallele Strahlen,
8. unvollständige Kreisbögen,
9. numerische Extremfälle,
10. deterministische Seeds.

Exit Gate P4:

1. alle synthetischen Tests bestehen.
2. Residuen und Konvergenz sind verfügbar.
3. keine ungetypten Koordinatenmatrizen in öffentlichen APIs.
4. Unsicherheit reagiert plausibel auf erhöhtes Rauschen.
5. independent_reviewer und metrology_scientist ohne P0 oder P1.

PHASE 5, ERSTER VERTIKALER MESSPFAD

Starte ux_accessibility_engineer und qa_validation_engineer für den Ablauf.

Implementiere mit ios_lead:

1. neues Projekt,
2. Hardwareobjekt,
3. geführte Aufnahme auf ebener Fläche,
4. Ruhe, Schärfe, Sättigung und Distanzhinweise,
5. mehrere geeignete Frames,
6. manuelle Markierung zweier sichtbarer Punkte,
7. Projektion in Board Koordinaten,
8. Abstand über mehrere Frames,
9. Unsicherheit,
10. Qualitätsentscheidung,
11. Wiederholungsmessung,
12. Vergleich der Umläufe,
13. Speichern und Wiederöffnen,
14. JSON und CSV Export,
15. verständliche Ablehnung.

Die UI zeigt nie nur eine Zahl. Sie zeigt:

1. Wert,
2. Einheit,
3. 95 Prozent Intervall,
4. Provenienz,
5. Qualitätsstatus,
6. Anzahl verwendeter Frames,
7. Warnungen,
8. erneute Aufnahmehandlung.

Exit Gate P5:

1. vollständiger Mock UI Test.
2. reale Geräteaufnahme, sofern Hardware verfügbar.
3. Vergleich gegen Referenzmaß dokumentiert.
4. keine Scheingenauigkeit.
5. Projekt lässt sich verlustfrei wieder öffnen.
6. P0 und P1 geschlossen.

PHASE 6, PLATINENKONTUR UND SCHRAUBENLÖCHER

Starte computer_vision_engineer, metrology_scientist und ux_accessibility_engineer.

Implementiere zuerst manuell:

1. Board Koordinatensystem,
2. Außenkonturpunkte,
3. Geraden und Eckpunkte,
4. Kreisrandpunkte,
5. Ellipse,
6. Langloch,
7. mehrere Löcher,
8. Lochmittelpunktabstände,
9. Abstände zur Außenkante,
10. Residuenansicht,
11. Unsicherheit und Ablehnung.

Füge erst danach unterstützende automatische Kandidatenerkennung hinzu.

Automatikregeln:

1. Nutzer kann jeden Kandidaten korrigieren.
2. automatische und manuelle Punkte werden protokolliert.
3. finale Geometrie bleibt deterministisch.
4. schlechte Konturen werden nicht erzwungen.
5. Langlöcher werden nicht als Kreise ausgegeben.

Validierung:

1. reale Lochplatte,
2. PCB Coupon,
3. mehrere Lochgrößen,
4. partielle Verdeckung,
5. Schatten,
6. Metallreflexion,
7. Randpositionen im Bild.

Exit Gate P6:

1. Sollwerte und Ergebnisse im Validierungsbericht.
2. Abdeckung der Unsicherheit geprüft.
3. Falsch Akzeptanz schlechter Aufnahmen bewertet.
4. DXF oder SVG Bohrbild Export.
5. unabhängiger Review ohne P0 oder P1.

PHASE 7, SICHTBARE HÖHEN UND STECKERGEOMETRIE

Starte apple_sensor_specialist, metrology_scientist, computer_vision_engineer und ux_accessibility_engineer.

Implementiere einen geführten Mehransichtenmodus:

1. Frontansicht,
2. zwei schräge Ansichten,
3. optionale Seitenansicht,
4. stabile Pose und ausreichende Parallaxe,
5. manuelle initiale Annotation,
6. sichtbare Frontfläche,
7. sichtbare Außenhülle,
8. Position relativ zur Platine,
9. Einsteckachse,
10. sichtbarer Überstand,
11. sichtbare Höhe,
12. Unsicherheit,
13. Qualitätsentscheidung.

Erzeuge getrennt:

1. gemessene sichtbare Geometrie,
2. abgeleiteten Panelausschnitt,
3. konfigurierbare Fertigungszugabe,
4. optionalen Bedienraum,
5. unbekannte verdeckte Maße.

Füge eine Herstellerdatenquelle nur hinzu, wenn:

1. Quelle dokumentiert ist,
2. Lizenz und Nutzung erlaubt sind,
3. Teilenummer hinreichend sicher ist,
4. Hersteller und optische Werte getrennte Provenienz behalten,
5. Nutzer die Zuordnung bestätigen kann.

Exit Gate P7:

1. mehrere reale Steckerfamilien getestet.
2. unknown Verhalten für verdeckte Maße getestet.
3. Panelausschnitt klar als derived.
4. Fertigungszugabe konfigurierbar und getrennt.
5. keine P0 oder P1.

PHASE 8, COMPUTER VISION AUTOMATISIERUNG

Diese Phase beginnt erst, wenn die manuellen Messpfade freigegeben sind.

Starte computer_vision_engineer, qa_validation_engineer und security_privacy_engineer.

Mögliche Funktionen:

1. Board Segmentierung,
2. Lochkandidaten,
3. Kantenkandidaten,
4. Steckerfamilie,
5. Text und Teilenummererkennung,
6. Annotationstracking über Frames.

Anforderungen:

1. Modell oder Algorithmus versioniert.
2. Trainings und Testdaten getrennt.
3. Offline Inferenz bevorzugt.
4. Modellgröße und Energieverbrauch gemessen.
5. Nutzerbestätigung bei unsicherer Klassifikation.
6. kein direktes Maß aus einem semantischen Label.
7. Regression gegen manuelle Ground Truth.
8. Fairness ist hier weniger zentral als Material und Beleuchtungsrobustheit, diese muss explizit getestet werden.

Exit Gate P8:

1. Automatik verkürzt den Ablauf messbar.
2. Messgüte verschlechtert sich nicht.
3. Fehlklassifikationen sind sichtbar und korrigierbar.
4. Dataset und Modellartefakte versioniert.
5. Datenschutz und Lizenz geprüft.

PHASE 9, EXPORT UND CAD INTEGRATION

Starte product_architect, metrology_scientist und technical_writer_compliance.

Implementiere mit ios_lead:

1. versioniertes JSON,
2. CSV Messbericht,
3. SVG,
4. DXF,
5. PDF Bericht,
6. später STEP über eine begründete Bibliothek oder einen klaren externen Konverter,
7. Koordinatenursprung und Einheiten,
8. Provenienz und Unsicherheit im Export,
9. Fertigungszugaben getrennt von Rohmessung,
10. Export Preview,
11. Round Trip Tests,
12. Schema Dokumentation.

Fertigungspresets:

1. FDM,
2. SLA,
3. CNC,
4. Laserschnitt,
5. benutzerdefiniert.

Presets sind keine universellen Wahrheiten. Sie werden als editierbare Ausgangswerte mit Quelle und Warnung behandelt.

Exit Gate P9:

1. CAD Testimporte erfolgreich.
2. Einheiten und Ursprung korrekt.
3. Round Trip ohne stille Informationsverluste.
4. Unsicherheit und Provenienz erhalten.
5. beschädigte oder inkompatible Exporte werden erkannt.

PHASE 10, LOKALE ENTERPRISE FUNKTIONEN

Implementiere:

1. Projekte und Versionen,
2. revisionssichere Messhistorie,
3. Tags und Suche,
4. Projektvorlagen,
5. Audit Timeline,
6. Exportpaket,
7. vollständige lokale Löschung,
8. Backup und Restore,
9. Datenbankmigration,
10. Diagnosesupportpaket mit Redaction,
11. MDM konfigurierbare Richtlinien, soweit sinnvoll,
12. Offline Lizenz oder Funktionsstrategie ohne Messblockade, falls kommerziell erforderlich.

Exit Gate P10:

1. Migrationstests über alle Schema Versionen.
2. Backup und Restore Test.
3. Löschtest.
4. keine Rohdaten in Supportexport ohne explizite Auswahl.
5. Performance bei realistischen Projektgrößen.
6. Security Review ohne P0 oder P1.

PHASE 11, OPTIONALER ENTERPRISE SYNC

Diese Phase ist separat deploybar und darf den Offline Kern nicht blockieren.

Starte product_architect, backend_platform_engineer, security_privacy_engineer und release_devops_engineer.

Lege zuerst ADRs fest für:

1. Backend Sprache und Framework,
2. PostgreSQL Schema,
3. Objektablage,
4. OIDC Providerintegration,
5. Mandantentrennung,
6. Audit,
7. Retention,
8. Deployment.

Bevorzugte Ausgangsarchitektur:

1. typisierter Backenddienst mit aktiv gepflegtem Framework,
2. PostgreSQL,
3. S3 kompatible Objektablage,
4. OpenAPI,
5. OIDC,
6. Docker Compose lokal,
7. gehärtete Container,
8. Helm für Kubernetes,
9. Admin Portal für Organisation, Rollen, Policies und Audit.

Implementiere:

1. Organisationen,
2. Rollen,
3. Projekte,
4. idempotente Artefaktuploads,
5. Prüfsummen,
6. Revisions und Konfliktmodell,
7. Audit Events,
8. Retention und Löschung,
9. Export,
10. Backup und Restore,
11. Offline Queue auf iOS,
12. Konflikt UI,
13. Contract Tests,
14. Mandantendurchbruch Tests.

Exit Gate P11:

1. lokaler Offline Modus unverändert funktionsfähig.
2. Mandantentrennung mit Negativtests.
3. OIDC und Rollenmodell dokumentiert.
4. Backup und Restore erfolgreich.
5. keine P0 oder P1 Security Befunde.
6. Betriebsrunbook vorhanden.

PHASE 12, SECURITY UND PRIVACY HARDENING

Starte security_privacy_engineer unabhängig. Zusätzlich bei Bedarf Codex Security für das autorisierte Repository.

Prüfe:

1. lokale Speicherung,
2. Keychain,
3. Importparser,
4. Export,
5. URL Handling,
6. Netzwerk,
7. OIDC,
8. Autorisierung,
9. Mandantentrennung,
10. Uploads,
11. Logs,
12. Crash Reports,
13. Telemetrie,
14. Abhängigkeiten,
15. CI Secrets,
16. Container,
17. Kubernetes,
18. Admin Portal,
19. Datenlöschung,
20. Supportpakete.

Erzeuge:

1. aktualisiertes Threat Model,
2. Security Testbericht,
3. SBOM,
4. Dependency Inventar,
5. Datenschutz Datenkarte,
6. Incident Response Runbook,
7. Vulnerability Disclosure Prozess,
8. offene Risiken mit Owner.

Exit Gate P12:

1. P0 und P1 geschlossen.
2. P2 akzeptiert oder terminiert.
3. Löschung und Export getestet.
4. Secrets Scan grün.
5. SBOM erzeugt.
6. keine sensible Information in Logs oder Telemetrie.

PHASE 13, ACCESSIBILITY, LOKALISIERUNG UND UX QUALIFIKATION

Starte ux_accessibility_engineer und technical_writer_compliance.

Prüfe:

1. VoiceOver,
2. Dynamic Type bis zu großen Stufen,
3. Kontrast,
4. reduzierte Bewegung,
5. Haptik als Ergänzung, nie als einzige Information,
6. Einhandbedienung,
7. Landschaft und Hochformat, soweit unterstützt,
8. Deutsch,
9. Englisch,
10. Zahlen und Einheitendarstellung,
11. verständliche Unsicherheit,
12. klare Ablehnungsgründe,
13. Erholung nach Unterbrechung.

Erzeuge Screenshots und UI Testnachweise.

Exit Gate P13:

1. zentrale Flows mit VoiceOver bedienbar.
2. keine abgeschnittenen kritischen Texte.
3. Fehler enthalten konkrete Handlung.
4. Messstatus ist nicht nur farblich codiert.
5. deutsche und englische Texte vollständig.

PHASE 14, PERFORMANCE, THERMAL UND ZUVERLÄSSIGKEIT

Starte qa_validation_engineer, apple_sensor_specialist und ios_lead nacheinander.

Messe:

1. Capture Frame Rate,
2. Verarbeitungslatenz,
3. Speicher,
4. Projektgröße,
5. Energie,
6. Thermal State,
7. lange Sessions,
8. Hintergrund und Vordergrundwechsel,
9. geringe Speichersituation,
10. unterbrochene Speicherung,
11. App Neustart,
12. beschädigte Projektdateien.

Definiere Budgets und implementiere Backpressure, Speicherlimits und Degradation.

Exit Gate P14:

1. keine reproduzierbaren Crashes.
2. keine ungebremste Speicherzunahme.
3. Thermal Degradation wird erklärt und behandelt.
4. Daten bleiben nach Unterbrechung konsistent.
5. Messung wird bei unzuverlässigem Zustand abgelehnt.

PHASE 15, METROLOGISCHE PRODUKTVALIDIERUNG

Starte metrology_scientist und qa_validation_engineer. Diese Phase benötigt reale Referenzkörper und menschliche Durchführung.

Erzeuge:

1. eingefrorenen Release Candidate Build,
2. eingefrorene Dataset und Algorithmusversion,
3. automatisierten Capture und Auswertungsimport,
4. Versuchsprotokoll,
5. Rohdatenprüfsummen,
6. Bias und Streuungsanalyse,
7. Unsicherheitsabdeckung,
8. Ablehnungsrate,
9. Material und Lichtmatrix,
10. Geräte und OS Matrix,
11. Validierungsbericht,
12. freigegebene Claims,
13. Known Limitations.

Wenn reale Versuche nicht durchgeführt werden können:

1. stelle alle Tools und Protokolle fertig,
2. markiere Gate P15 als BLOCKED HUMAN VALIDATION,
3. gib keinerlei endgültige Genauigkeitsangabe frei.

Exit Gate P15:

1. menschlich signierter oder ausdrücklich freigegebener Validierungsbericht.
2. freigegebene Claims entsprechen dem schlechtesten unterstützten Fall.
3. Unsicherheitsintervalle erreichen die vorab festgelegte Abdeckung.
4. systematische Fehler sind korrigiert oder in Unsicherheit enthalten.
5. Release Claims Dokument ist konsistent.

PHASE 16, RELEASE ENGINEERING

Starte release_devops_engineer, security_privacy_engineer und technical_writer_compliance.

Implementiere:

1. vollständige CI,
2. Unit, Integration und UI Tests,
3. Testberichte,
4. Coverage Bericht,
5. Archive,
6. SBOM,
7. Prüfsummen,
8. Release Notes,
9. TestFlight oder interne Distribution Vorbereitung,
10. Backend Container und Helm Release, falls Sync enthalten,
11. Datenbankmigration und Rollbackplan,
12. Backup und Restore Nachweis,
13. Operations Runbook,
14. Support Runbook,
15. App Store Metadatenentwurf,
16. Privacy Manifest und Datenschutztexte,
17. Lizenztexte.

Apple Signierung, TestFlight Upload und Store Einreichung benötigen echte Accounts und menschliche Genehmigung.

Exit Gate P16:

1. reproduzierbarer Release Build.
2. alle Pflichtjobs grün.
3. Release Evidence Paket.
4. keine P0 oder P1.
5. P15 bestanden.
6. menschliche Produktfreigabe vorbereitet.

PHASE 17, RELEASE CANDIDATE AUDIT

Starte unabhängig:

1. independent_reviewer
2. security_privacy_engineer
3. metrology_scientist
4. qa_validation_engineer
5. technical_writer_compliance

Jeder Agent prüft den eingefrorenen Release Candidate read only.

Erzeuge eine finale Befundmatrix:

1. Befund,
2. Schweregrad,
3. Komponente,
4. Reproduktion,
5. Risiko,
6. Fix,
7. Testbeleg,
8. Status,
9. Owner.

P0 und P1 müssen geschlossen werden. Danach gesamte relevante Test und Validierungskette erneut ausführen.

FINALER DEFINITION OF DONE

Du darfst das Produkt nur als releasefähig bezeichnen, wenn alle folgenden Punkte belegt sind:

1. App baut und archiviert.
2. alle Pflicht Unit, Integration und UI Tests bestehen.
3. reale iPhone 15 Pro Max Capability Daten liegen vor.
4. reale Messvalidierung ist bestanden.
5. Unsicherheitsmodell ist geprüft.
6. keine erfundene verdeckte Geometrie.
7. Datenformat und Migration sind getestet.
8. Offline Betrieb ist vollständig.
9. Backup, Restore und Löschung sind getestet.
10. optionaler Sync ist mandantensicher.
11. Security Review ohne P0 oder P1.
12. Accessibility und Lokalisierung sind geprüft.
13. Performance und Thermal Verhalten sind qualifiziert.
14. SBOM, Release Evidence und Dokumentation liegen vor.
15. Known Limitations und freigegebene Claims sind konsistent.
16. menschliche Apple, Rechts, Security und Produktfreigaben sind dokumentiert.

AUSGABE NACH JEDER SESSION

Berichte strukturiert:

1. abgeschlossene Phase und Gate Status,
2. geänderte Dateien,
3. ausgeführte Befehle,
4. bestandene und fehlgeschlagene Tests,
5. Reviewbefunde,
6. reale Hardwarebelege,
7. offene menschliche Gates,
8. Risiken,
9. nächste kleinste Arbeitseinheit.

BEGINNE JETZT

1. Prüfe B0.
2. Wenn B0 vollständig ist, führe Phase 0 vollständig aus.
3. Fahre danach mit Phase 1 fort.
4. Beende die aktuelle Session erst nach einem klaren, belegten Zwischenstand und aktualisiertem docs/STATUS.md.
5. Überspringe kein Gate und behaupte keine nicht ausgeführte Prüfung.
```
# N. Fortsetzungsprompt für weitere Codex Sessions

```text
Lies AGENTS.md, alle näherliegenden AGENTS.md Dateien, docs/STATUS.md, docs/QUALITY_GATES.md, docs/RISK_REGISTER.md und PHONE_METROLOGY_ENTERPRISE_CODEX_BLUEPRINT.md.

Prüfe den tatsächlichen Repository Zustand und die letzten Testbelege. Vertraue STATUS.md nicht blind, sondern gleiche es mit Code, Git Diff und Artefakten ab.

Setze die höchste priorisierte unvollständige Phase fort.

Regeln:

1. Schließe zuerst offene P0 und P1 Befunde.
2. Starte passende read only Subagents parallel.
3. Verwende höchstens einen schreibenden Subagenten pro Modul.
4. Implementiere nur die nächste klar abgegrenzte Arbeitseinheit.
5. Baue, teste und lasse unabhängig reviewen.
6. Aktualisiere Anforderungen, Nachweismatrix, Risiken und STATUS.md.
7. Markiere reale Hardware, Signierung, Referenzmessung und externe Credentials als menschliche Gates, wenn sie fehlen.
8. Behaupte nichts als bestanden, wofür kein aktueller Beleg vorliegt.
9. Keine Genauigkeitsbehauptung ohne freigegebenen Validierungsbericht.

Berichte am Ende:

1. Gate Status,
2. Änderungen,
3. Befehle,
4. Testergebnisse,
5. Reviews,
6. Hardwarebelege,
7. offene Blocker,
8. nächste Arbeitseinheit.
```

---

# O. Empfohlene Codex Einstellungen außerhalb des Repositories

Die folgende persönliche Konfiguration kann optional in `~/.codex/config.toml` verwendet werden. Repository spezifische Regeln bleiben in `.codex/config.toml`.

```toml
model = "gpt-5.5"
model_reasoning_effort = "high"
model_reasoning_summary = "concise"
model_verbosity = "medium"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
web_search = "live"

[agents]
max_threads = 6
max_depth = 1
job_max_runtime_seconds = 3600
```

Keine Enterprise Organisation sollte `danger-full-access`, unkontrollierten Netzwerkzugriff oder `approval_policy = "never"` als normalen interaktiven Entwicklungsstandard verwenden.

---

# P. Empfohlener Arbeitsrhythmus

Ein sinnvoller Ablauf pro Codex Session:

1. Status und Diff prüfen.
2. ein Arbeitspaket auswählen.
3. read only Analyse parallelisieren.
4. Implementierung seriell.
5. schmaler Test.
6. breiter Test am Gate.
7. unabhängiger Review.
8. Befunde beheben.
9. Dokumente aktualisieren.
10. nachvollziehbaren Commit vorbereiten.

Ein Sessionziel sollte eine überprüfbare vertikale Scheibe sein, nicht die gesamte Produktvision.

---

# Q. Releasecheckliste

## Produkt

- [ ] Kernmessung funktioniert offline.
- [ ] sichtbare und verdeckte Geometrie werden korrekt getrennt.
- [ ] jeder Wert enthält Provenienz, Unsicherheit und Qualitätsstatus.
- [ ] Projekte können gespeichert, geöffnet, exportiert und gelöscht werden.
- [ ] Datenmigrationen sind getestet.
- [ ] Known Limitations sind sichtbar.

## Messung

- [ ] Capability Snapshot vom Zielgerät.
- [ ] synthetische Ground Truth Tests.
- [ ] reale Referenzmessungen.
- [ ] Bias und Wiederholbarkeit.
- [ ] 95 Prozent Intervallabdeckung.
- [ ] Ablehnungsrate.
- [ ] Material und Beleuchtungsmatrix.
- [ ] freigegebene Claims.

## iOS

- [ ] Build und Archive.
- [ ] Unit Tests.
- [ ] UI Tests.
- [ ] reale Hardwaretests.
- [ ] Permission und Unterbrechungsfälle.
- [ ] Thermal und Speichertests.
- [ ] Accessibility.
- [ ] Deutsch und Englisch.
- [ ] Privacy Manifest.
- [ ] keine sensiblen Logs.

## Security

- [ ] Threat Model.
- [ ] Dependency und Lizenzinventar.
- [ ] SBOM.
- [ ] Secret Scan.
- [ ] Importparser Tests.
- [ ] sichere lokale Speicherung.
- [ ] Löschtest.
- [ ] Security Review ohne P0 oder P1.
- [ ] Incident Runbook.

## Optionaler Sync

- [ ] OIDC.
- [ ] Rollen.
- [ ] Mandantentrennung.
- [ ] Negativtests.
- [ ] idempotente Uploads.
- [ ] Prüfsummen.
- [ ] Audit.
- [ ] Retention.
- [ ] Backup und Restore.
- [ ] Betriebshandbuch.

## Release

- [ ] reproduzierbarer Build.
- [ ] Release Evidence.
- [ ] TestFlight oder interne Distribution.
- [ ] Release Notes.
- [ ] Nutzerhandbuch.
- [ ] Adminhandbuch.
- [ ] Supporthandbuch.
- [ ] Rechts und Datenschutzprüfung.
- [ ] menschliche Produktfreigabe.

---

# R. Schlussregel

Ein fertiges Enterprise Produkt ist in diesem Projekt kein Codeumfang, sondern ein belegter Zustand.

Der Hauptagent darf Fortschritt optimieren. Er darf niemals fehlende Evidenz durch überzeugende Sprache ersetzen.
