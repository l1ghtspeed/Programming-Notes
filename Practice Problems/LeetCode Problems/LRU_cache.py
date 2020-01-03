def __init__(self, capacity):
        self._capacity = capacity
        self._cache = OrderedDict
    
    def get(self, key):
        if key in self._cache:
            val = self._cache[key]
            del self._cache[key]
            self._cache[key] = val
            return val
        return -1
    
    def put(self, key, val):
        if key in self._cache:
            del self._cache[key]
        self._cache[key] = val
        if len(self._cache) > self._capacity:
            self._cache.pop()
