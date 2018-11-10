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
        for i, val in enumerate(self._array):
            if i + 1 < len(self._array):
                string += "'{}',".format(str(val))
            else:
                string += "'{}'".format(str(val))
        string += "]"
        return string
    
    def append(self, item):
        pass

    def insert(self, index, item):
        pass

    def remove(self, item):
        pass
    
    def size(self):
        return self._n
    
    def contains(self, item):
        pass
    