def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def sub(*nums):
    total = 0
    for num in nums:
        total-= num
    return total

def mul(*nums):
    total = 0
    for num in nums:
        total*= num
    return total

def div(*nums):
    total = 0
    for num in nums:
        total/= num
    return total