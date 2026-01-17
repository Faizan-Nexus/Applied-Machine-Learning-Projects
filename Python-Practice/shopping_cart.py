# Shopping Cart 
items = input("Enter item you want to buy: ")
price = float(input("Enter the price of the item: "))
quatitty = int(input("How much you want to buy: "))

total = price * quatitty
print(f"Your total for {quatitty} {items} is: ${total:.2f}")
print("Thank you for your purchase!")

#We can also implement it through a loop
cart = {}

while True:
    items = input("Enter item you want to buy (or 'done' to finish): ")
    if items == 'done':
        break
    price = float(input("Enter the price of the item: "))
    quantity = int(input("How much you want to buy: "))
    cart[items] = {'price': price, 'quantity': quantity}

# Calculate total
total = sum(item['price'] * item['quantity'] for item in cart.values())
print(f"Your total for the items in your cart is: ${total:.2f}")
print("Thank you for your purchase!")
# Display cart items
print("Your cart items:")
for item, details in cart.items():
    print(f"{item}: {details['quantity']} @ ${details['price']:.2f} each")
# Display total
print(f"Total: ${total:.2f}")
print("Thank you for your purchase!")
