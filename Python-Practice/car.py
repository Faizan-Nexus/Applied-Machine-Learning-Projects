#Attributes = What an Object has/is
#Methods = What an Object does
#Class = Blueprint for Objects
#Object = Instance of a Class
class Car:
    def __init__(self,color,for_sale,model,year):
        self.color =  color
        self.model = model
        self.for_sale = for_sale
        self.year = year
    
    def drive(self):
        print(f"{self.model} starts")
    
    def stop(self):
        print(f"{self.model} stops")

