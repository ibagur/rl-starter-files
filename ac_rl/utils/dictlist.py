class dictlist(dict):
    """A dictionnary of lists of same size. Dictionnary items can be
    accessed using `.` notation and list items using `[]` notation.

    Example:
        >>> d = dictlist({'a': [[1, 2], [3, 4]], 'b': [[5], [6]]})
        >>> d.a
        [[1, 2], [3, 4]]
        >>> d[0]
        dictlist({'a': [1, 2], 'b': [5]})
    """

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __len__(self):
        return len(next(iter(dict.values(self))))

    def __getitem__(self, index):
        return dictlist({key: value[index] for key, value in dict.items(self)})
    
    def __setitem__(self, index, d):
        for key, value in d.items():
            dict.__getitem__(self, key)[index] = value
    
    def append(self, d):
        for key, value in d.items():
            if not(key in dict.keys(self)):
                dict.__setitem__(self, key, [])
            dict.__getitem__(self, key).append(value)