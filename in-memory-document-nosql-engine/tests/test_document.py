import pytest
from src.engine.document import Document

def test_initialize_doc_and_reject_new_attributes():
    newDoc = Document("doc_1", {"user": "Alice"})


    with pytest.raises(AttributeError):
        newDoc.newAttr = "Hello World"


    assert newDoc.id == "doc_1"
    assert newDoc.data["user"] == "Alice"
