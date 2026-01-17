#Class Methods = Allows Operation related to the class itself
# Take(cls) as the first parameter , which represents the class itself
# Use @classmethod decorator
# Class methods can be called on the class itself, not on the instance of the class

class student:

    count = 0
    avg_age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.count += 1
        student.avg_age += age

    # Instance Method
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    # Class Method
    @classmethod
    def get_count(cls):
        return f"Total Number of Students: {cls.count}"
    
    @classmethod
    def get_avg_age(cls):
        return f"Average Age of Class Students: {cls.avg_age / cls.count}"

student1 = student("Ali", 20)
student2 = student("Ahmed", 22)
student3 = student("Asad", 21)

#Note: Class Variables are shared among all instances of a class
print("Aceesing the class variable through instances",student1.count)
print(student.get_count())
print(student.get_avg_age())