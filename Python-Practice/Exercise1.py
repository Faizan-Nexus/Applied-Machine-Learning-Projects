# Exercise 01

# # Mads libs Game 
# # Build a story and insert nouns , verbs and ajectives 


# print(f"I went to a {adjective1} zoo , Yesterady")
# print(f"In an exhibit I saw {noun1}")

# print(f"{noun1} was {adjective2} and {verb1}ing")
# print(f" I was {noun3}")


# # Exercise 02
# # Calculate the area of rectangle 
# length = float(input("Enter the Length: "))
# width = float(input("Enter the Width: "))

# area = length* width
# print(f"The area is: {area}cm^2")

# # Exercise 03
# # Shopping Cart 
# items = input("Enter item you want to buy: ")
# price = float(input("Enter the price of the item: "))
# quatitty = int(input("How much you want to buy: "))

# total = price * quatitty

# print

#Calculator
# oper = input("Enter the operations (+,-,*,/,%): ")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# check = ["*","+","/","-","%"]
# while oper not in check:
# print(f"{oper} is not a valid operator! Try again")
# oper = input("Enter the operations (+,-,*,/,%): ")
# if oper == "+":
# result = num1+num2
# print(f"{num1} {oper} {num2} = {round(result,3)}")
# elif oper == "-":
# result = num1-num2
# print(f"{num1} {oper} {num2} = {round(result,3)}")
# elif oper == "*":
# result = num1*num2
# print(f"{num1} {oper} {num2} = {round(result,3)}")
# elif oper == "/":
# result = num1/num2
# print(f"{num1} {oper} {num2} = {round(result,3)}") 
# elif oper == "%":
# result = num1%num2
# print(f"{num1} {oper} {num2} = {round(result,3)}")

 
# name = "Ali"
# price = 231.4234
# print(f"Price $:{price:#10}")
# print(f"Price $:{price:10}")
# print(f"Price $:{price:<10}")
# print(f"Price $:{price:>10}")
# print(f"Price $:{price:^10}")
# print(f"Price $:{price:,}")
# print(f"Price $:{price:,}")
# print(f"Price $:{price:+,}")
# print(f"Price $:{price:+,}")
# print(f"Price $:{price:+,.2f}")
# name = input("Enter your name: ")
# while name == "":
#     print(f"Please enter your name")
#     print("Hello ",name)
# fruits = ["Dhruv Gaba","Faizan","Ed Sheeran"]
# for fruit in fruits:
# print(fruit)
 
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter number of columns: "))

# symbol = input("Enter any symbol of your choice: ")

# for x in range(rows):
# for y in range(rows):
# if y <= x:
# print(symbol, end = " ")
# print()


# import time as t
# my_time = int(input("Enter the time in seconds: "))

# for x in range(0, my_time+1):
# sec = x%60
# mins = int(x/60) % 60
# hour = int((x/3600))
# print(f"{hour:02}:{mins:02}:{sec:02}")
# t.sleep(1)

# print("Time's up!")

# fruits = ["Orange", "Apple", "Banana", "Berry", "Apricot"]

#Sets 
# fruits = ("Orange", "Apple", "Banana", "Berry", "Apricot")

# foods = []
# prices = []
# total = 0

# while True:
# food = input("Enter Food you wnat to Buy (q to quit): ")
# price = float(input("Enter the price of the food: "))
# if food.lower() or price.lower() == "q":
# break
# else:
# foods.append(food)
# prices.append(price)

# for price in prices:
# total += price
 
# print("-----Your Cart-----")
# for food,price in foods,prices:
# print(food, end =" ")
# print(price, end = " ")

# print("Your total bill is: {total}")

# fruits = ["Apple", "Mango", "Orange"]
# veg = ["Carrot", "Spanich","Turnip"]
# snacks = ["Cake", "Biscuits", "Fries"]

# foods = [fruits,veg,snacks]
# for food in foods:
# for x in food:
# print(x, end=" ")
# print()

# questions = ("What is the abundant gas in Atmosphere?",
# "What is the color of sky?",
# "Percentage of water on Earth?")

# options = [["A.Nitrogen","'B.'Oxygen","CHydrogen","'D'.Helium"],
# ["A.Blue","'B.'Red","'C'.Gren","'D'.Yellow"],
# ["A.21%","'B.'24%","'C'.76","'D'.79%"]]

# answers = ["A","A","'D'"]

# question_num = 0
# score = 0
# guesses = []

# print("---------Mini Quiz---------")

# for question in questions:
# print(" ")
# print(f"Q#{question_num+1} {question}")
# for option in options[question_num]:
# print(option)
 
# guess = input("Enter {A,'B,''C','D'}: ").uper()
# if guess == answers[question_num]:
# print("CORRECT!")
# score += 1
# else:
# print("INCORRECT!")
# print(f"Correct Answer is {answers[question_num]}")
# question_num += 1
# if question_num == len(questions):
# print("Quiz is Completed")
# print("----------------------------")
# print(f"Out of {len(questions)} questions you answered {score} correctly.")
# print(f"Your Percentage is {(score/len(questions))*100:.2f}%")

capitals = {"USA" : "WASINGTON 'D'.'C'",
 "INDIA" : "NEW DEHLI",
 "PAKISTAN" : "ISLAMABAD"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("FRANCE"))

# for key in capitals.keys():
# print(key)

# print()

# for values in capitals.values():
# print(values)

# for key,values in capitals.items():
# print(key, ":",values)

# menu = {
# "biryani" : 3.99,
# "lemonade" : 1.49,
# "soda" : 2.0,
# "shawarma" : 4.25
# }

# cart = []
# total = 0

# print("----------Menu--------")
# for key,val in menu.items():
# print(f"{key:10}: ${val:.2f}")
# print("----------------------")

# while True:
# item = input("Enter item of your choice (q to quit): ").lower()
 
# if item == "q":
# break
# elif menu.get(item) is not None:
# cart.append(item)
 

# print("--------Order Summary----------")
# for i in cart:
# print(i, end=" ")
# total+= menu.get(i)
# print("\n") 
# print(f"Your total bill is ${total:.2f}")
# print("-------------------------------")


import random as r
# print(r.randint(1,100))
# options = ("A","'B"',"'C'","'D'")
# print(r.choice(options))
# card = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
# r.shuffle(card)
# print(card)

# low = 0
# high = 10
# guesses = 0
# number = r.randint(low,high)
# while True:
# guess = int(input(f"Enter your guess between {low} and {high}: "))
# guesses +=1
# if guess < number:
# print("Your gues is low. Try Again!")
# elif guess > number :
# print("Your choice is high. Try Again!")
# else:
# break

# print(f"Congrtulations! You guessed the number in {guesses}'s attempts")

# options = ("rock", "paper", "scissor")
# game = True

# while game:
# player = None
# computer = r.choice(options)
# while player not in options:
# player = input("Enter your choice (rock, paper, scissor): ").lower()
 
# print(f"Player: {player}")
# print(f"Computer: {computer}")
# if player == computer:
# print("It's a tie")
# elif player == "rock" and computer == "scissor":
# print("Rock breaks scissor")
# print("You Win!")
# elif player == "paper" and computer == "rock":
# print("Paper Wraps rock")
# print("You Win!")
# elif player == "scissor" and computer =="paper":
# print("scissor cuts paper")
# print("You Win!")
# else:
# print("You Lose!")
 
# play = input("Play Again (Y/N): ").lower()
# if not play == "y":
# game = False

# print("Thanks for Playing!")


#Encryptoin and Decryption

# import random
# import string

# chars = " " + string.punctuation + string.digits + string.ascii_letters

# chars = list(chars)

# key = chars.copy()

# random.shuffle(key)


# #Encrypt
# plain_text = input("Enter message to encrypt: ")
# cipher = ""

# for letter in plain_text:
# index = chars.index(letter)
# cipher += key[index]

# print(f"Your message is encrypted as: {cipher}")
# plain_text = ""

# for letter in cipher:
# index = key.index(letter)
# plain_text += chars[index]

# print(f"Your Message is decrypted as follows: {plain_text}")


#Fucntions
# def happy_birthday(name,age) :
# print(f"Happy Birthday to {name}")
# print(f"You are {age} years old")
# print("Happy Birthday to You!")
 
# happy_birthday("Bro",20)

#calculator function

# def add(num1,num2):
# x = num1+num2
# return x

# result = add(4,2)
# print(result)

# def name(first_name,last_name):
# first = first_name.capitalize()
# last = last_name.capitalize()
# return first+" "+last

# print(name("tom","cruise")) 
 
 
#Default Arguments
# def total_price(price,disc = 0.20,tax = 0.05):
# return (price * (1-disc) * (1+tax))

# print(f"Total price is: ${total_price(500,0.30):.2f}")

#Keywords Arguments
# def hbd(name,age):
# print(f"Happy Birthday to you {name}")
# print(f"You are {age} years old")
# print("Happy Birthday to You")

# hbd("John",21)
# print()
# hbd("Alex", age = 20)
# print()
# hbd( age = 72,name = "Tom")
# for i in range(1,11):
# print(i,end="*")

# print()
# print('1','2','3','4', sep="-")


#Abstract Argumnets
#*args unpacks to tuple
#**kwargs unpacks to dictionary
# def add(*args):
# total = 0
# for arg in args:
# total+= arg
# print(type(args))
# return total

# print(add(3,6,2,42,52))

# def hbd(**kwargs):
# for key,values in kwargs.items():
# print(f"{key}: {values}")

# hbd(name = "James", age = 20)

# def ship_label(*info,**address):
# print("Hello:")
# for detail in info:
# print(detail,end=" ")
# print("\nYour shipping address is as follows: ")
# for data in address.values():
# print(data, end=" ")
 
# ship_label("Mark","Whalberg",street = "123", state = "California", country = "USA")

# List Comprehension
# list_name = [expression for itterables and then a range]

# double = [x for x in range(0,11)]
# print(double)
# # for x in range(0,11):
# # double.append(x)
# # print(double) 
# fruits = ["Apple", "Orange", "Mango", "Strawberry"]

# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# number = [-1,-2,-4,-6,3,6]
# negative_num = [num for num in number if num<0]
# positive_num = [num for num in number if num>0]
# evn_num = [num for num in number if num%2 == 0]
# print(evn_num)

#Match Case Statement
# def weekend(day):
# match day:
# case "Saturday" | "Sunday":
# return "Hooray Weekend!"
# case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Firday":
# return "It is not weekend, Get back to work"
# case _:
# return f"{day} is not a valid Day!"

# print(weekend("Sunday"))

# Modules
# import calc
# result = calc.add(6,8.3,8)
# print(result)

# print(help("modules"))


#Scope Resolution 
#LGEB (local < Enclosed < Global < builtin)
# def func1():
# x = 1
# def func2():
# print(x)
# func2()

# x = 3
# func1()
# from math import e
# def func1(e):
# print(e)

# e= 3
# func1(e) 

# scream = print
# scream("Hello")

#GPA Calculator
# print(" Welcome to the GPA calculator.")
# print("Please enter all your letter grades, one per line.")
# print("Enter a blank line to designate the end.")
# #map from letter grade to point value
# points = { 'A+' :4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B':3.0, 'B-':2.67, 'C+' :2.33, 'C' :2.0, 'C-' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}

# num_courses = 0
# total_points = 0
# done = False
# while not done:
#     grade = input( )
#     #read line from user
#     if grade == '':
#         done = True
#     elif grade not in points:
#     #empty line was entered
#     # unrecognized grade entered
#         print(f"Unknown grade {grade} being ignored")
#     else:
#         num_courses += 1
#         total_points += points[grade]
#     if num_courses > 0:
#         #avoid division by zero
#         print(f"Your GPA is {(total_points / num_courses):.3f}")


# P.O.O.P
# from car import Car
# car1 = Car("Black",False,"BMW","2025")
# print(car1.color)
# print(car1.drive())
# print(car1.stop())


# data = [num for num in range(1,11)]
# print(data)

#Lambda Function

# double = lambda num : num*2
# add = lambda num1,num2 : num1+num2

# max = lambda x,y : x if x>y else y

# min = lambda x,y : x if x<y else y
# print(add(3,5))

# Map Function
# num = [num for num in range(1,6)]
# nums  = map(lambda x: (x+2),num)

# for num in nums:
#     print(num)


# class Student:
#     class_year = 2026
#     enrolled = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.enrolled += 1
    

# s1 = Student("James", 30)
# s1 = Student("Will Smith", 24)
# s1 = Student("Patrick", 26)
# s1 = Student("Mark", 29)
# print(f"The Graduating class of year {Student.class_year} has total of {Student.enrolled} students enrolled")

#Inheritance
# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True
#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print("Whoof")

# class Cat(Animal):
#     pass

# class Mouse(Animal):
#     pass

# d1 = Dog("Shello")
# c1 = Cat("Mano")
# m1 = Mouse("Jerry")

# print(d1.name)
# print(d1.is_alive)
# d1.eat()
# d1.sleep()

#Multiple and Multilevel

# class goodStudents:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def goodGrades(self):
#         print(f"Student {self.name} score good grades")
#         print(f"Student {self.name} is eligible for scholarship")

# class badstudents(goodStudents):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def badGrades(self):
#         print(f"Student {self.name} score bad grades")
#         print(f"Student  {self.name} is not eligible for scholarship")


# class averageStudents(badstudents):
#     pass
# # class averageStudents(goodStudents,badstudents):
# #     pass

# s1 = goodStudents("Ali", 24)
# s2 = badstudents("Dhruve", 23)
# s3 = averageStudents("Faizan", 22)

# s1.goodGrades()
# s2.goodGrades()
# s2.badGrades()  # This will not work as goodStudents does not have badGrades method
# s3.badGrades()
# s3.goodGrades()

# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def details(self):
#         print(f"Employee name is {self.name} and age is {self.age}")

# class PermanentEmployee(Employee):
#     def __init__(self,name,age,salary):
#         super().__init__(name, age)
#         self.salary = salary
    
#     def salaryDetails(self):
#         print(f"{self.name} is a Permanent Employee and has a salary of ${self.salary}")

# class ContractEmployee(Employee):
#     def __init__(self,name,age,hourly_rate,work_hours):
#         super().__init__(name, age)
#         self.hourly_rate = hourly_rate
#         self.work_hours = work_hours

#     def salaryDetails(self):
#         salary = self.hourly_rate * self.work_hours
#         print(f"{self.name} is a Contract Employee and has a salary of ${salary}")

# class Intern(Employee):
#     def __init__(self, name, age, stipend):
#         super().__init__(name, age)
#         self.stipend = stipend
    
#     def stipendDetails(self):
#         print(f"{self.name} is an Intern and has a stipend of ${self.stipend}")

# # class Finance(Employee,ContractEmployee,PermanentEmployee,Intern):
# #     def __init__(self, name, age, salary=0, hourly_rate=0, work_hours=0, stipend=0):
# #         Employee.__init__(self, name, age)
# #         PermanentEmployee.__init__(self, name, age, salary)
# #         ContractEmployee.__init__(self, name, age, hourly_rate, work_hours)
# #         Intern.__init__(self, name, age, stipend)
    
# #     def details(self):
# #         print(f"Finance Employee name is {self.name}, age is {self.age}, salary is ${self.salary}, hourly rate is ${self.hourly_rate}, work hours are {self.work_hours}, and stipend is ${self.stipend}")

# p1 = PermanentEmployee("Alice", 30, 50000)
# c1 = ContractEmployee("Bob", 25, 20, 160)
# i1 = Intern("Charlie", 22, 1000)
# p1.details()
# p1.salaryDetails()
# c1.details()
# c1.salaryDetails()
# i1.details()
# i1.stipendDetails()

#Abstract Classes
from abc import ABC, abstractmethod

# class Vehicle(ABC):
    
#     @abstractmethod
#     def go(self):
#         pass
    
#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def go(self):
#         print("The car is moving")
    
#     def stop(self):
#         print("The car has stopped")

# car = Car()
# car.go()

#polymorphism
# class Shape:
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         print("The area of circle is")
#         return 3.14 * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         print("The area of rectangle is")
#         return self.width * self.height

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         print("The area of Triangle is")
#         return 0.5 * self.base * self.height

# shapes = [Circle(5),Rectangle(4, 6),Triangle(3, 7)]

# for shape in shapes:
#     print(f"{shape.area()} cm 2")

# #Duck Typing
# class Animal:
#     alive = True
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof Woof"

# class Cat(Animal):
#     def speak(self):
#         return "Meow Meow"

# class Car:
#     alive = False
#     def speak(self):
#         return "Beep Beep"

# animals = [Dog(), Cat(),Car()]

# for animal in animals:
#     print(animal.speak())
#     print(animal.alive)

#Aggregation
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def addbook(self,book):
        self.books.append(book)
    
    def listBooks(self):
        return [f"{book.title} by {book.author} " for book in self.books]
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library1 = Library("City Library")
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Start with Why", "Simon Sneak")
print(f"Welcome to {library1.name}")
library1.addbook(book1)
library1.addbook(book2)
library1.addbook(book3)
print(library1.listBooks(), "are available in the library.", end="\n")
# # Encapsulation
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says Woof Woof")

# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says Meow Meow")

# class Mouse(Animal):
#     def speak(self):
#         print(f"{self.name} says Squeak Squeak")

# def animal_sound(animal):
#     animal.speak()
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# mouse = Mouse("Jerry")
# animal_sound(dog)
# animal_sound(cat)
# animal_sound(mouse)