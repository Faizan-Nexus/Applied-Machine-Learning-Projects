def show_balance():
    print()
    print("**********************************")
    print(f"Your Current Balance is ${balance}")
    print("**********************************")
    print()
    
def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print()
        print("*******************")
        print("Insufficient Funds!")
        print("*******************")
        print()
        return 0
    elif amount < 0 :
        print()
        print("***************")
        print("Invalid Amount!")
        print("***************")
        print()
        return 0
    else:
        return amount

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    
    if amount < 0 :
        print()
        print("Invalid Amount")
        print()
        return 0
    else:
        amount += balance
    return amount

balance = 0
is_running = True

while is_running:
    print("Welcome to ATM")
    print("**************************")
    print("1.Show Balance")
    print("2.Withdraw Amount")
    print("3.Deposit Amount")
    print("4.Log out")
    print("**************************")
    
    option = input("Please enter a number to proceed (1-4) : ")
    
    if option == "1":
        show_balance()
    elif option == "2":
        amount = withdraw()
        balance -= amount
        if amount > 0:
            print()
            print("**************************************************")
            print(f"${amount} sucessfully withdrawn from your account")
            print("**************************************************")
            print()
        amount = 0
    elif option == "3":
        amount =  deposit()
        balance += amount
        print()
        print("**************************************************")
        print(f"${amount} sucessfully deposited into your account")
        print("**************************************************")
        print()
        amount = 0
    elif option == "4":
        is_running = False
    else:
        print()
        print("**************************")
        print("Invalid Choice, Try Again!")
        print("**************************")
        print()
print()        
print("Sucessfully Logged Out from account!")
print("Thank You for Using ATM") 
print("*********** 😊 ************")   
