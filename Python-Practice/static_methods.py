#Static methods = A method that belongs to the class but does not take cls or self as the first parameter

class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def get_info(self):
        return f"Name: {self.name}, Species: {self.species}"
    
    @staticmethod
    def is_animal(x):
        return x in ["Dog", "Cat", "Rabbit", "Cow", "Goat"]

animal1 = Animals("Tommy", "Dog")
animal2 = Animals("Sheelo", "Cat")
animal3 = Animals("Toota", "Parrot")
print(animal1.get_info())
print(Animals.is_animal(animal1.species))
print(Animals.is_animal("Dog"))