#Extraction of digits

# num = int(input("Enter a number to extract it's digit :"))

# while num > 0:
#     last_digit = num % 10
#     print(last_digit,end =" ")
#     num = num //10



# Count digits it's time complexity is log10(n); that is beacuse we are continiuously dividing our number by 10
n = num = 5438
# count = 0
# while num > 0:
#     count +=1
#     num = num//10
# print(f"{n} has {count} digits")
# Or alternatively

# from math import *
# def count(num):
#     return int(log10(num) + 1)

# print(f"{num} has {count(num)} digits")


#Check Pailnadrome Time complexity is log10(n)and space is O(1) as we have a constant space
# num = int(input("Input a number to cehck if it is a palindrome or not: "))
# n = num
# result = 0 
# while n>0:
#     last_digit = n%10
#     result = (result * 10) + last_digit
#     n = n // 10

# print(f"{num} is {'a palindrome' if result == num else 'not a palindrome'}")

# Armstrong Number:
# An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# For example:
# 153 is an Armstrong number because:
#   1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# Here, 153 has 3 digits, so each digit is raised to the power of 3.

# num = input("Input a number to cehck if it is a Armstrong or not: ")
# power = len(num)
# n = int(num)       
# total = 0
 
# while n > 0:
#     index = n % 10
#     total = total + pow(index,power)
#     n = n // 10

# print(f"{num} is {'an armstrong' if total == int(num) else 'not an armstrong'}")

#Factors of number
# Brute Force TC =O(N)      SC = O(K) where K are number of factors
# num = 10
# result = []
# for i in range(1,num+1):
#     if num % i == 0:
#         result.append(i)
    
# print(f"Factors of {num} are {result}")

# Or / Alternative TC = O(N/2)  or O(N) SC = O(K) where K are number of factors
#In this we will have following appraoch
# Any number will have factors tilll (number/2) after that it has no factors
# 10 will have factors tilll 5 after that it has no factors
# num = 10
# result = [num]
# for i in range(1,(num//2)+1):
#     if num % i == 0:
#         result.append(i)
    
# print(f"Factors of {num} are {result}")

# Or (Most aptimal) TC = O(sqrt(N)) where SC = O(K)
#In this we will have following appraoch
# let's say we wna tto calculate for 9
# 1 _____ 16
# 2 _____ 8
# 4 _____ 4  where (1, 4, 8, 16) are factors of 16
from math import sqrt
num = 10
result = []
for i in range(1,int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        if num // i != i:
            result.append(num//i)
    
print(f"Factors of {num} are {result}")
