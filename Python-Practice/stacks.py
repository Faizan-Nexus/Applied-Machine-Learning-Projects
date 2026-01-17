#List Inmplementation of Stacks

# stacks = []

# #Push
# stacks.append(0)
# stacks.append(5)
# stacks.append(10)
# stacks.append(15)
# for num in reversed(stacks):
#     print(num, end = " ")
# print()

# #Pop
# top = stacks.pop()
# print("Pop Element",top)

# #peek
# if stacks:
#     print(stacks[-1])

# #is_empty
# print(len(stacks) == 0)

# #size
# print(len(stacks))


#Real Implementations
# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def push(self,item):
#         self.items.append(item)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         return None
    
#     def peek(self):
#         return self.items[-1]
    
#     def is_empty(self):
#         return len(self.items) == 0
            
#     def size(self):
#         return len(self.items)

# s1 = Stack()

# s1.push(20)
# s1.push(15)
# s1.push(10)
# s1.push(5)
# s1.push(0)

# print(s1.peek())
# print(s1.pop())
# print(s1.is_empty())
# print(s1.size())


# Design a stack like data strcture instead of usual pop it should remove the most frequent element in the stack and also if their is a tie between the frequency of elements then remove the recent

# FreqStack is a special stack that removes the most frequent element first.
# If there is a tie (multiple elements with the same frequency), it removes the most recently added one.

# class FreqStack:
#     def __init__(self):
#         # cnt will keep track of how many times each value has been pushed
#         self.cnt = {}
#         # maxCnt keeps track of the current highest frequency of any element
#         self.maxCnt = 0
#         # stack is a dictionary where the key is the frequency,
#         # and the value is a list (stack) of elements with that frequency
#         self.stack = {}
    
#     def push(self, val: int) -> None:
#         # Increase the count for this value
#         valCnt = 1 + self.cnt.get(val, 0)
#         self.cnt[val] = valCnt

#         # If this value's count is now the highest, update maxCnt
#         if valCnt > self.maxCnt:
#             self.maxCnt = valCnt
#             # Create a new stack for this frequency if it doesn't exist
#             self.stack[valCnt] = []
        
#         # Add the value to the stack for its frequency
#         self.stack[valCnt].append(val)
    
#     def pop(self) -> int:
#         # Remove and return the most recent element with the highest frequency
#         res = self.stack[self.maxCnt].pop()
#         # Decrease the count for this value
#         self.cnt[res] -= 1
#         # If there are no more elements at this frequency, decrease maxCnt
#         if not self.stack[self.maxCnt]:
#             self.maxCnt -= 1
#         return res        

# # Example usage:
# obj = FreqStack()
# obj.push(10)   # 10 appears once
# obj.push(11)   # 11 appears once
# obj.push(11)   # 11 appears twice (most frequent)
# obj.push(10)   # 10 appears twice (tie with 11, but 10 is more recent)
# obj.push(12)   # 12 appears once

# # Now, pop should remove 12 (freq=1), but 10 and 11 have freq=2.
# # Since 10 was pushed after 11, pop will remove 10.
# print(obj.pop())  # Output: 10

# list = []

# #Simple Stack
# list.append(0)
# list.append(1)
# list.append(2)
# list.append(3)

# for item in reversed(list):
#     print(item,  end = " ")

# #pop
# pop = list.pop()
# print("\nPop the first element:",pop)

# #peek
# print("Top Element in our stack",list[-1])

# #is empty
# print("Is tack empty? ",len(list) == 0)

# #size
# print(len(list))


class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if not self.is_empty():
            return f"Poping the top element: {self.items.pop()}"
        return None
    
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)


s1 = Stack()

s1.push(5)
s1.push(4)
s1.push(3)
s1.push(2)
s1.push(1)

print(s1.is_empty())
print(s1.peek())
print(s1.pop())
print(s1.peek())
print(s1.size())


class FreqStack:
    def __init__(self):
        self.cnt = {}
        self.maxCnt = 0
        self.stack = {}
    
    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt

        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stack[valCnt] = []
        
        self.stack[valCnt].append(val)
    
    def pop(self) -> int:
        res = self.stack[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.maxCnt]:
            self.maxCnt -= 1
        return res