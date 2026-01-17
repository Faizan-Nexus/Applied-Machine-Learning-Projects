# Math in Python
friends = 0
# friends = firends + 1
friends += 1
# print(friends)



# Some functions 
x = 3.14
y = 5
z = 2


import math as m
# print(m.pi)

age = 18

credit_card = "12345-5678"
print(credit_card[::-1])

emial =  input("Enter the emial:")
index = emial.index("@")
user_name = emial[1:index]
domain = emial[index+1:]

print(f"Your username is {emial[1:emial.index("@")]} and domain is {emial[emial.index("@")+1 :]}")

for x in range(1,11):
    print(x, end = "")

# [start:end:step