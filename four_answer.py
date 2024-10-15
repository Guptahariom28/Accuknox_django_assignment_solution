#initializing the class Rectangle
class Rectangle:
    #implementing the constructor  and the given parameters
    def __init__(self, length: int, width: int):
        self.length= length
        self.width= width

#iterators so that every value get printed 
    def __iter__(self):
        yield('length', self.length)
        yield('width', self.width)

#making a str functions that return the data in required format
    def __str__(self):
        return f"Length: {self.length}, Width: {self.width}"


#making the object of the class and passing the claues of length and width respectively
rectangle= Rectangle(10,8)
print(rectangle)