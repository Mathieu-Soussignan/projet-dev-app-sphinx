# docs/export_openapi.py
import json
import os
import sys
from pathlib import Path

# Ajoute la racine du projet au PYTHONPATH (projet-dev-app-sphinx/)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from API.main import app  # noqa: E402

OUT = ROOT / "docs" / "source" / "_static" / "openapi.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

spec = app.openapi()
OUT.write_text(json.dumps(spec, indent=2), encoding="utf-8")

print(f"Wrote {OUT}")