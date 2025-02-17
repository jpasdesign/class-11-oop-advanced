class OrderedDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def keys(self):
        return self._keys

    def values(self):
        return self._values
    
    def __setitem__(self, key, value):
        self._keys.append(key)
        self._values.append(value)

    def items(self):
        result = []
        for key, value in zip(self._keys, self._values):
            result.append((key, value))
        return result
    
    def __getitem__(self, a_key):
        for key, value in self.items():
            if key == a_key:
                return value
        raise KeyError(a_key)
        
    def __contains__(self, key):
        return key in self.keys()
    
    def __len__(self):
        return len(self.items())
    
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for key, value in self.items():
            if key not in other or other[key] != value:
                return False
            return True
    
    def __str__(self):
        s = '{'
        for key, value in self.items():
            s += '{}: {}, '.format(repr(key), repr(value))
        s = s.rstrip(', ')
        s += '}'
        return s
    
    __repr__ = __str__
    
    def __add__(self, other):
        new = OrderedDict()
        for key, value in self.items():
            new[key] = value
        for key, value in other.items():
            new[key] = value
        return new
    
    @classmethod
    def from_keys(cls, sequence):
        new = OrderedDict()
        for elem in sequence:
            new[elem] = None
        
        return new