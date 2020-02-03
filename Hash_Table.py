'''Module contains class HashTable()'''
class HashTable():
    '''Class HashTable contains HashTable'''
    def __init__(self):
        '''This function initialize hashtable'''
        self._length = int(1e5)
        self._table = [[] for i in range(self._length)]
        self._current_arr = 0
        self._current_pos = -1
        self._size = 0

    def add(self, value):
        '''This function adds a value to hashtable'''
        my_hash = hash(value)
        index = my_hash % self._length
        self.remove(value)
        self._table[index].append(value)
        self._size += 1

    def remove(self, value):
        '''This function removes a value from hashtable'''
        my_hash = hash(value)
        index = my_hash % self._length
        if value in self._table[index]:
            self._table[index].remove(value)
            self._size -= 1

    def __contains__(self, value):
        '''This function checks if a values is in hashtable'''
        my_hash = hash(value)
        index = my_hash % self._length
        return value in self._table[index]

    def __len__(self):
        '''This function returns size of hashtable'''
        return self._size

    def __iter__(self):
        '''This function makes hashtable an iterable object'''
        return self

    def __next__(self):
        '''This function returns next element in hashtable'''
        self._current_pos += 1
        if self._current_pos < len(self._table[self._current_arr]):
            return self._table[self._current_arr][self._current_pos]
        while self._current_arr < self._length:
            if  self._current_pos < len(self._table[self._current_arr]):
                break
            self._current_arr += 1
            self._current_pos = 0
        if self._current_arr < self._length:
            return self._table[self._current_arr][self._current_pos]
        self._current_arr = 0
        self._current_pos = -1
        raise StopIteration
