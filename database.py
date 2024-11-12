class Database():

    def __init__(self):
        self._data = {}

    def get(self, key):
        return self._data.get(key)
    
    def put(self, key, value):
        self._data[key] = value

    def all(self):
        return self._data
    
    def delete(self, key):
        if key in self._data:
            del self._data[key]