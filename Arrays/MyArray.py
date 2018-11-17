import ctypes
#nclude <Python.h>

class MyArray(object):

    def __init__(self):
        # initial state of my array has 0 elements (n) and capacity of 1 (how many elements it is able to hold before it needs to resize)
        self._n = 0
        self._capacity = 1
        # Creates a null ptr array obj
        self._array = (self._capacity * ctypes.py_object)()
        #self.array[:] = [None] * self.size
    
    """
        String representation of the array. Normally if you print(object) or in this case object is my array, the memory address of the array
        is printed. This string representation allows me to print the actual contents of the array when a call to "print(object)" is made.
    """
    def __str__(self):
        string = ""
        
        if self._n == 0:
            return "[]"

        string += "["
        for i in range(self._n):
            if i + 1 < self._n:
                string += "'{}',".format(self._array[i])
            else:
                string += "'{}'".format(self._array[i])
        string += "]"
        return string
    
    def append(self, item):
        if self._n == self._capacity:
            self.resize()
        self._array[self._n] = item
        self._n += 1

    def insert(self, index, item):
        if self._n == self._capacity:
            self.resize()

        # Creates a null ptr array obj
        new_array = (self._capacity * ctypes.py_object)()

        #index of original contents
        ind = 0
        self._n += 1
        for i in range(self._n):
            if i == index:
                new_array[i] = item
            else:
                new_array[i] = self._array[ind]
                ind += 1
        self._array = new_array

    def remove(self, item):
        if not self.contains(item):
            return None
        
        self._n -= 1

        found = False
        for i in range(self._n):
            if self._array[i] == item and not found:
                found = True
            if found:
                self._array[i] = self._array[i+1]

        return item
    
    def __len__(self):
        return self._n

    def size(self):
        return self._n
    
    def get(self, index):
        if 0 <= index < self._n:
            return self.array[index]
        else:
            raise("Index out of Bounds error.")
            
    def contains(self, item):
        for i in range(self._n):
            if self._array[i] == item:
                return True

        return False
        
    def resize(self):
        self._capacity *= 2
        # Creates a null ptr array obj
        new_array = (self._capacity * ctypes.py_object)()

        for i in range(self._n):
            new_array[i] = self._array[i]
        self._array = new_array
    