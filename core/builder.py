"""
builder.py
-----------

Responsible for merging CV sections into a single Markdown file.
This module provides the CVBuilder class with basic structure.

The logic is implemented progressively as the framework evolves.
"""

from pathlib import Path
from typing import List


class CVBuilder:
    """
    CVBuilder merges multiple Markdown sections into a unified CV.

    Parameters
    ----------
    sections_dir : Path
        Directory containing markdown sections.
    output_file : Path
        Where the merged MD file will be generated.
    """

    def __init__(self, sections_dir: Path, output_file: Path):
        self.sections_dir = sections_dir
        self.output_file = output_file

    def list_sections(self) -> List[Path]:
        """Return a list of markdown files in the sections directory."""
        return sorted(self.sections_dir.glob("*.md"))

    def build(self) -> None:
        """
        Merge all markdown sections in alphabetical order into a single CV.

        This is a stub implementation — real logic will be added later.
        """
        raise NotImplementedError("build() will be implemented in later versions.")
