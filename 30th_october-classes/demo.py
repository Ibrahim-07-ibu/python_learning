'''Create a Person class with attributes name and age.
Create a subClass Student that inherits from Person  (Hint: use the super keyword in python and use)
Print all attributes through a new method in Student class.'''

class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age 

class student(person):
    def __init__(self,name,age):
        super().__init__(name,age)

    def show(self):
        print(self.name)
        print(self.age)

student = student("Ibrahim",17)
student.show()

