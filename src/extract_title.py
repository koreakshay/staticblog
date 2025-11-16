"""Utility to extract the H1 title from a markdown document."""


def extract_title(markdown: str) -> str:
    """Return the text of the first H1 ('# ') heading in the markdown.

    Raises an Exception if no H1 heading is found.
    """
    for line in markdown.split("\n"):
        stripped = line.strip()
        # H1: a single leading '#' followed by a space
        if stripped.startswith("# ") and not stripped.startswith("##"):
            # Remove leading '# ' and any extra surrounding whitespace
            return stripped[2:].strip()
    raise Exception("No H1 title found in markdown")
