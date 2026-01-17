#Format Specifiers = {:flags} format a value based on what flags are inserted

# :<  = left Justify
# :>  = right justify
# :^  = center align
# :+  = use plus to indicate a +ve value
# :   = insert a space before positive numbers
# :,  = comma separator like 1,000

price = 300004.543223
price2 = 123
print(f"Price is {price}")
print(f"Price is {price:.2f}")
print(f"Price is {price:}")
print(f"Price is {price:8}")
print(f"Price is {price2:>}")
print(f"Price is {price:,}")
print(f"Price is {price:^}")
print(f"Price is {price:+}")
