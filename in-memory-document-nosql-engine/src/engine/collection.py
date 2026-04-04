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
            is_match = all(self._resolve_path(doc.data, key) == value for key, value in query.items())
            if is_match:
                yield(doc)


    def _resolve_path(self, data, path_string):

        if not isinstance(data, dict):
            return None

        parts = path_string.split(".", 1)

        if len(parts) == 1:
            return data.get(parts[0])

        current_key = parts[0] #take only the first one to check

        if current_key in data:
            return self._resolve_path(data.get(current_key), parts[1]) # bubbles up the final value





