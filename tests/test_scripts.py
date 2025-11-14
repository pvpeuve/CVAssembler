from core.builder import CVBuilder
from core.parser import SectionParser

def test_parser_loads_sections():
    parser = SectionParser("sections")
    result = parser.load_section()
    assert isinstance(result, list)

def test_builder_merges():
    builder = CVBuilder()
    merged = builder.merge(["# A", "# B"])
    assert "A" in merged and "B" in merged
