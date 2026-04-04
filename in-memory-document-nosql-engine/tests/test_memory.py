from dataclasses import dataclass
import sys
from typing import Dict

from src.engine.document import Document

@dataclass
class StandardDocument:
    id: str
    data: Dict

def test_StandardDoc_memory_is_more_than_slotted():

    standard = StandardDocument("standard1", {"name": "alice"})

    slotted = Document("slotted1", {"name": "alice"})

    sizeOfStandard = sys.getsizeof(standard) + sys.getsizeof(standard.__dict__)
    sizeOfSlotted = sys.getsizeof(slotted)


    assert sizeOfSlotted < sizeOfStandard


