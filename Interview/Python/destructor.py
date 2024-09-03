class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Destroying the object {self.name}")

# Create an instance of MyClass
obj = MyClass("Example")

# Perform some operations with the object.


class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')
    
    def read_file(self):
        data = self.file.read()
        print(data)
    
    def __del__(self):
        self.file.close()
        print(f"File '{self.filename}' has been closed.")

# Create an instance of FileHandler
handler = FileHandler("example.txt")

# Read the contents of the file
handler.read_file()

# The object is about to be destroyed or deallocated
# and the destructor is automatically called.
