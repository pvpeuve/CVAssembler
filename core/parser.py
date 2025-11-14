"""
parser.py
-----------

Reads structured JSON/YAML data and injects it into templates.
Useful for fully automated CV generation.

Not required for basic functionality.
"""

import json
from pathlib import Path
from typing import Dict, Any


class DataParser:
    """Utility to load user data from JSON files."""

    def load_json(self, file: Path) -> Dict[str, Any]:
        """Return dictionary loaded from a JSON file."""
        with file.open("r", encoding="utf-8") as f:
            return json.load(f)
