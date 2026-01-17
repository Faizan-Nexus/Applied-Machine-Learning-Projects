price = 231.4234

print(f"Price $:{price:#10}") # Using # to include the decimal point
print(f"Price $:{price:10.2f}")  # Formatting to 2 decimal places
print(f"Price $:{price:<10.2f}") # Left aligned
print(f"Price $:{price:>10.2f}") # Right aligned
print(f"Price $:{price:^10.2f}") # Center aligned
print(f"Price $:{price:,}") # Using comma as a thousands separator
print(f"Price $:{price:,.2f}") # Comma as thousands separator with 2 decimal places
print(f"Price $:{price:+}") # Including sign
print(f"Price $:{price:+10.2f}") # Including sign with 2 decimal places
print(f"Price $:{price:010.2f}") # Zero padded with 2 decimal places
print(f"Price $:{price:0<10.2f}") # Zero padded left aligned with 2 decimal places
print(f"Price $:{price:0>10.2f}") # Zero padded right aligned with 2 decimal places
print(f"Price $:{price:0^10.2f}") # Zero padded center aligned with 2 decimal places
print(f"Price $:{price:0^10}") # Zero padded center aligned without decimal



#String Slicing
name = "Mark Whalberg"
print(f"First 4 characters: {name[:4]}")  # First 4 characters
print(f"Last 4 characters: {name[-4:]}")  # Last 4 characters
print(f"Middle characters: {name[4:-4]}")  # Middle characters
print(f"Every second character: {name[::2]}")  # Every second character
print(f"Reversed string: {name[::-1]}")  # Reversed string
