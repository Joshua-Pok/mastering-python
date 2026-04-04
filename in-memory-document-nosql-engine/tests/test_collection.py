import pytest
from src.engine.collection import Collection
from src.engine.document import Document


def test_collections_class():
    collection = Collection()


    docs = [Document(str(i), {"active": True}) for i in range(10)]


    for doc in docs:
        collection[f"{doc.id}"] = doc


    assert collection["1"] == docs[1]
    assert len(collection) == 10
    assert "1" in collection 
    
    with pytest.raises(KeyError):
        collection["20"]

