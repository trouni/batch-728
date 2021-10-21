from datetime import date


class Student:
    # class attributes
    cursus = None

    # constructor
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    # instance method
    def says(self, something):
        print(f"{self.name} says {something}")

    # class method
    @classmethod
    def from_birthyear(cls, name, birthyear):
        age = date.today().year - birthyear
        return cls(name, age)
