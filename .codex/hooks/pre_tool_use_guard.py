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