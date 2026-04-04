from typing import Dict


class Collection():

    def __init__(self):
        self._documents = {}


    def __setitem__(self, key, value):
        self._documents[key] = value


    def __getitem__(self, key):
        if key not in self._documents:
            raise KeyError

        return self._documents[key]


    def __len__(self):
        return len(self._documents)

    def __contains__(self, key):
        if key not in self._documents:
            return False

        return True


    def __iter__(self):
        for doc in self._documents.values():
            yield doc


    def find(self, query:Dict):

        for doc in self._documents.values():
            is_match = all(doc.data.get(key) == value for key, value in query.items())
            if is_match:
                yield(doc)



