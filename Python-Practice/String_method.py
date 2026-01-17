fruits = ["apple", "banana", "cherry"]

# Using the join method to concatenate the list into a string
fruits_string = ", ".join(fruits)
print("Fruits:", fruits_string)

# Using the split method to convert a string into a list
fruits_list = fruits_string.split(", ")
print("Fruits List:", fruits_list)

# Using the replace method to change a part of the string
fruits_string = fruits_string.replace("banana", "orange")
print("Updated Fruits:", fruits_string)

# Using the find method to locate a substring
index = fruits_string.find("cherry")
if index != -1:
    print(f"'cherry' found at index: {index}")
    print(f"Substring found: {fruits_string[index:index+len('cherry')]}")
else:
    print("'cherry' not found")

# Using the upper method to convert the string to uppercase
fruits_string = fruits_string.upper()
print("Uppercase Fruits:", fruits_string)

# Using the lower method to convert the string to lowercase
fruits_string = fruits_string.lower()
print("Lowercase Fruits:", fruits_string)

# Using the title method to capitalize the first letter of each word
fruits_string = fruits_string.title()
print("Title Case Fruits:", fruits_string)
