# API spezifische Regeln

1. Der Dienst ist optional. Offline Messung darf nicht von ihm abhängen.
2. OpenAPI ist Vertrag und wird in CI gegen Implementierung geprüft.
3. Jede Ressource besitzt organizationId und wird serverseitig autorisiert.
4. Uploads sind idempotent, größenbegrenzt, typgeprüft und mit Prüfsummen versehen.
5. Audit Events sind append only und enthalten keine Rohbilder oder Secrets.
6. Datenbankmigrationen sind vorwärts und rollbackbewusst dokumentiert.
7. Integrationstests verwenden echte PostgreSQL und S3 kompatible Testdienste.
8. Restore Tests sind Bestandteil des Releasegates.