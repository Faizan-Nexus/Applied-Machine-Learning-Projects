menu = {"Biryani": 150,
        "Ghotala": 150,
        "Paratha": 50,
        "Omelete": 50,
        "Cholay": 30,
        "Chai": 40
        }

cart = []
total = 0

print("----------Menu----------")
for key,value in menu.items():
    print(f"{key:10}: {value: >} Rupees")
    
print("-------------------------")

while True:
    food = input("Shop an item (q to quit shopping):")
    food.lower()

    if food == "q":
        break
    
    items = int(input("Select qunaity: "))
    if items == 0 :
        items = 1
    
    elif menu.get(food) is None:
        print("Not in the Menu")
    elif menu.get(food) is not None:
        cart.append(food)

print("----------Your Order---------") 
print(" Item      Quantity       Price")    
for food in cart:
    total += menu.get(food) *items
    print(f" {food:>} {items:8} {menu[food]:15} """,)  
print("-----------------------------")

print(f"\nYour total bill is {total: .2f} Rupees")      
