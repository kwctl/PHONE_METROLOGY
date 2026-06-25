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