import json
from pathlib import Path

schema_dir = Path("schemas")

for file in schema_dir.glob("*.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            json.load(f)
        print(f"OK: {file}")
    except Exception as e:
        print(f"ERROR in {file}: {e}")
