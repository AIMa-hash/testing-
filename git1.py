class Reverse:
    def __init__(self, data):
        self.data = data 
        self.index = len(data)

    def __iter__(self):
        return self 
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

str_back = Reverse("manish")
print(str_back)
print(next(str_back))
print()
for i in str_back:
    print(i)
print(next(str_back))

class Manish:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.repr =  f"{self.name}1{self.age}2"
        self.index = len(self.repr)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.repr[self.index]

a = Manish("manish", 25)
print(a.repr)
print(a)
print(next(a))
b = iter(a) #both 'a' and iter(a) have the same memory location.
print(b)
print(next(b))
print(next(b))
print()
for i in a:
    print(i)


class Manish:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.repr =  f"{self.name}1{self.age}2"
        self.index = len(self.repr)
    
    def __str__(self):
        return f"[{self.name}, {self.age}]"

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.repr[self.index]

a = Manish("manish", 25)
print(str(a))
print(a.repr)
print(a)
print(next(a))
b = iter(a) #both 'a' and iter(a) have the same memory location.
print(b)
print(next(b))
print(next(b))
print()
for i in a:
    print(i)


