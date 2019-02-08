''' An implementation of Hash Table in Python'''
from collections import MutableMapping
from random import randrange
from abc import abstractmethod

class MapBase(MutableMapping):
    
    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)
        
        def __lt__(self, other):
            return self._key < other._key

class HashMapBase(MapBase):

    def __init__(self, capacity, p=109345121):
        self._table = [None,] * capacity
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)
        
    def _hash_function(self, k):
        return ((self._scale * hash(k) + self._shift) % self._prime) % len(self._table)
    
    def __len__(self):
        return self._n

    @abstractmethod
    def _bucket_getitem(self, j, k):
        pass
    
    @abstractmethod
    def _bucket_setitem(self, j, k, v):
        pass

    @abstractmethod
    def _bucket_delitem(self, j, k):
        pass
    
    @abstractmethod
    def __iter__(self):
        pass

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)
    
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(len(self._table) * 2 - 1)


    def __delitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_delitem(j, k)
    
    def _resize(self, c):
        old_items = list(self.items())
        self._table = [None, ] * c
        self._n = 0
        for (k, v) in old_items:
            self[k] = v
    
class ChainHashMap(HashMapBase):
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('KeyError: %s'%j)
        return bucket[k]
    
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = {}
        old_size = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > old_size:
            self._n += 1
    
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('KeyError: %s'%j)
        del bucket[k]
    
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

class ProbeHashMap(HashMapBase):
    _AVAIL = object()

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    
    def _find_slot(self, j, k):
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
                elif k == self._table[j]._key:
                    return (True, j)
            j = (j + 1) % len(self._table)
    
    def _bucket_getitem(self, j, k):
        found, loc = self._find_slot(j, k)
        if not found:
            raise KeyError('%s'%j)
        return self._table[j]._value
    
    def _bucket_setitem(self, j, k, v):
        found, loc = self._find_slot(j, k)
        if not found:
            self._table[loc] = self._Item(k, v)
            self._n += 1
        else:
            self._table[j]._value = v
        
    def _bucket_delitem(self, j, k):
        found, loc = self._find_slot(j, k)
        if not found:
            raise KeyError('%s'%j)
        self._table[j] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
    


