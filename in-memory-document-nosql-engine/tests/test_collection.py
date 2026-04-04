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


def test_collection_yields():
    collection = Collection()

    docs = [Document(str(i), {"active": True}) for i in range(3)]

    for doc in docs:
        collection[doc.id] = doc


    res = []


    for doc in collection:
        res.append(doc)


    assert len(res) == 3
    assert docs[0] in res
    assert docs[1] in res
    assert docs[2] in res


def test_find_function():

    collection = Collection()


    doc1 = Document("1", {"status": "active", "tier": "pro"})
    doc2 = Document("2", {"status": "active", "tier": "free"})
    doc3 = Document("3", {"name": "Alice"})

    collection["1"] = doc1
    collection["2"] = doc2
    collection["3"] = doc3


    results = list(collection.find({"status": "active", "tier": "pro"}))

    assert len(results) == 1
    assert results[0] == doc1
    

    results = list(collection.find({"status": "active"}))
    assert len(results) == 2


