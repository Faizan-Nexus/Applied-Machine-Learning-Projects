import sys  # This line lets us use some extra Python tools, like checking the size of a variable.
#sys is a module in Python that provides access to some variables used or maintained by the interpreter and functions that interact with the interpreter.For example, it can be used to get the size of a variable in bytes.
print("Hola Amigo!")
age = (input("Enter Your Age: "))
if  int(age) >=18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

exp = int(age)**2
num1 =23
num2 =32
print("Floor Division", num1//3)   #After Diviosn Result is assigned back to variable 
print("Exponention Sign", exp)
print("Size of Variable age is:",sys.getsizeof(age ))