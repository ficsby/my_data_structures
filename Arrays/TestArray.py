from MyArray import MyArray
class TestArray(object):
    if __name__== "__main__":
        array = MyArray()
        print(array)
        print(array.size())
        print(len(array))
        
        for i in range(20):
            array.append(i)

        array.insert(0, 10)
        array.remove(10)
        print(array)