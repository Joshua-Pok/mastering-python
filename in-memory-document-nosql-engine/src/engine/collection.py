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


