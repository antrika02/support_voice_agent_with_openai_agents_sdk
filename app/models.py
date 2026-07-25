from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Document:
    """
    Represents one documentation page.
    """

    title: str
    content: str
    url: str
    description: str = ""
    language: str = "en"
    metadata: Dict = field(default_factory=dict)