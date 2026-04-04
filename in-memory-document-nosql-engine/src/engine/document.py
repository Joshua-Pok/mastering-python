from dataclasses import dataclass
from typing import Dict


@dataclass(slots=True)
class Document():
    id: str
    data: Dict
