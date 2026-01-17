age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Ternary if-else statement
status = "minor" if age < 18 else "adult" if age < 65 else "senior"
print(f"You are a {status}.")
