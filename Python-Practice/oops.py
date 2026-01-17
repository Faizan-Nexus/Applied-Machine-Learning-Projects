from car import Car

car_1 = Car("Toyota", "Corolla",17,"White")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.start()

car_2 = Car("Suzuki","Mehran",2006,"White")

car_2.start()
car_2.stop()