# exception = AN event that intterputs the flowof thr programm
# (ZeroDivivionError, TypeEror, ValueError)
# 1.try, 2.except, 3.finally 

# try : try some code
# except Exception: Handle the exception
# finally : DO some clean up

try:
    number = int(input("Enter a number: "))
    print(1/number)
# except ZeroDivisionError:
#     print("You cannot divide by zero IDIOT")
# except ValueError:
#     print("Idiot only numbers")
except Exception:
    print("Something went wrong!")

finally :
    #Bro I always executes
    print("I can sweep some bad things")