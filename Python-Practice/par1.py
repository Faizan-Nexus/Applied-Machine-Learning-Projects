# print("Python")
# # scream = print

# # scream("Python")

# #int
# a = 3
# b = 3.45
# c = "Python"
# d = False

# # print(a)
# # print(b)
# # print(c)
# # print(d)

# #type casting
# price  = 345


# for loops

# name  = ["Mark Whalberg", "Tom Cruise", "Brad Pitt", "Leonardo DiCaprio"]

# for char in name:
#     print(char)

# name = input("Enter your name: ")

# while name == "":
#     print("Enter your name")
#     name = input()

# print(f"Hello, {name}")

# name = ["Mark Whalberg"]
# for char in name:
#     print(char)

# # Nested loops
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"i: {i}, j: {j}" , end = " - ")
#     print()  # New line after inner loop completes


# #triangle pattern
# rows = 4
# for row in range(rows):
#     for col in range(row + 1):
#         print("*", end=" ")
#     print()  # New line after each row
 
 #[start:end:step]

# Ordered

list = [1, 2, 3, 4, 5]

# print(list) 


# # set {}
# set = {"Apple", "Banana", "Cherry"}
# print(set)

# tuple ()
# tuple = ("Python", "Java", "C++")
# print(tuple.count("Python"))  # Count occurrences of "Python"
# print(tuple.index("Python"))  # Count occurrences of "Python"

# fruits = ("Orange", "Apple", "Banana")
# vegetables = ("Carrot", "Potato", "Tomato")
# pulses = ("Lentils", "Chickpeas", "Beans")

# gorceryy = [fruits, vegetables, pulses]

# for category in gorceryy:
#     for item in category:
#         print(item, end=" ")
#     print()  # New line after each category

# capital_cities = {
#     "Pakistan": "Islamabad",
#     "India": "New Delhi",
#     "USA": "Washington, D.C."
# }
# print(capital_cities)

# #get Item
# print(capital_cities.get("Pakistan"))  # Output: Islamabad


# for country, city in capital_cities.items():
#     print(f"The capital of {country} is {city}")
    
# for  in capital_cities.values():
#     print(f"Capitals {capital}") 
    
# capital_cities.keys()  # Get all keys

# capital_cities.values()  # Get all values

# print(dir(capital_cities))  # List all methods and attributes of the dictionary

# import math
# print(math.pi)  # Print the value of pi from the math module

# import random
# list = [1, 2, 3, 4, 5]
# print(random.choice(list))
# print(list)  # Output: The list will be shuffled randomly
# # Shuffle the list randomly

# def HappyBirthday(name,gender,age =18,):
#     print(gender)
#     print(f"Happy Birthday, {name}!")
#     print(f"You are now {age} years old!")
# def add(x,y):
#     return x + y
    
# print(add(5, 10))  # Output: 15
    
# HappyBirthday("Zohaib")

# class Student:
#     #class variable
#     school_name = "ABC High School"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#         print(f"School: {self.school_name}")

# s1 = Student("Zohaib", 30)
# s1.display_info()  # Output: Name: Zohaib, Age: 30
# print(s1.school_name)  # Output: ABC High School

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")
    
#     def eat(self):
#         print(f"{self.name} is eating.")   
    
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks.")

# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} meows.")
        
# # Create instances of Dog and Cat
# dog = Dog("Buddy")
# dog.eat()  # Call the eat method from the Animal class
# dog.speak()  # Output: Buddy barks.
# cat = Cat("Whiskers")
# cat.eat()  # Call the eat method from the Animal class
# cat.speak()  # Output: Whiskers meows.

# def bfs(graph, start):
#     queue = [start]  # Use a list as a queue
#     visited = set([start])
#     print(visited)

#     while queue:
#         node = queue.pop(0)  # Remove the first element
#         # print(node, end=" ")

#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 visited.add(neighbor)
#         print("Queue",queue)
#         print("Visited",visited)

# # Example graph
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': ['H'],
#     'F': [],
#     'G': [],
#     'H': []
# }

# # Run BFS
# bfs(graph, 'A')


import heapq

# Define the tree-like graph with edge costs
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 4)],
    'D': [],
    'E': [('G', 2), ('H', 3)],
    'F': [],
    'G': [],
    'H': []
}

# Heuristic values for each node (example: estimated cost to goal)
heuristic = {
    'A': 6, 'B': 4, 'C': 5, 'D': 3, 'E': 2, 'F': 6, 'G': 1, 'H': 0
}

# A* Search Algorithm
def a_star_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (cost, node)
    print(priority_queue)
    came_from = {start: None}
    cost_so_far = {start: 0}
    

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current == goal:
            break

        for neighbor, cost in graph.get(current, []):
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct the shortest path
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from[node]
    path.reverse()

    return path

# Run A* from 'A' to 'H'
path = a_star_search(graph, 'A', 'H')
print("Shortest Path:", path)


#