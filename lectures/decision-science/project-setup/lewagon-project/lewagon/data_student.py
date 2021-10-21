from lewagon.student import Student


class DataStudent(Student):
    cursus = "datascience"

    def __init__(self, name, age, major):
        super().__init__(name, age)
        print(__file__)
        self.major = major
