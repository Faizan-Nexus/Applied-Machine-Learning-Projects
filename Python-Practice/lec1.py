# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
    
#     def insert_at_start(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def insert_at_end(self,data):
#         current = self.head
#         new_node = Node(data)
#         if not self.head:
#             self.head =new_node
#             return
#         while current.next:
#             current = current.next
#         current.next = new_node
        
#     def insert_after_node(self,prev_node,data):
#         current = self.head
#         while current and current.data != prev_node:
#             current = current.next
#         if not current:
#             print("Previous Node Does not exist")
#             return
#         new_node = Node(data)
#         new_node.next = current.next
#         current.next = new_node    
    
#     def traversal(self):
#         current = self.head
#         while current:
#             print(current.data, end = " -> ")
#             current = current.next
#         print("Node End")
    
#     def delete(self,value):
#         curr = self.head
#         if curr and curr.data == value:
#             self.head  = curr.next
#             return
#         prev = None
#         while curr and curr.data != value:
#             prev = curr
#             curr = curr.next
#         if not curr:
#             print("Value does not exist")
#             return
#         prev.next = curr.next
            

# L1 = LinkedList()
# L1.insert_at_start(5)
# L1.insert_at_start(0)
# L1.insert_after_node(5,7)
# # L1.insert_after_node(12,7)
# L1.delete(8)
# L1.insert_at_end(10)
# L1.traversal()


# #Stack
# stack = []

# #psuh
# stack.append(0)
# stack.append(1)
# stack.append(2)

# for num in reversed(stack):
#     print(num, end =  " ")

# #pop
# top = stack.pop()
# print(top)

# #peek
# print(stack[-1])

# #is_empty
# print(len(stack) == 0)

# #size
# print(len(stack))

# class Stack:
#     def __init__(self):
#         self.item = []
    
#     def push(self,data):
#         self.item.append(data)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.item.pop()
#         return None
        
#     def is_empty(self):
#         return len(self.item) == 0
    
#     def peek(self):
#         return self.item[-1]
    
#     def size(self):
#         return len(self.item)


# s1 = Stack()
# s1.push(0)
# s1.push(5)
# s1.push(8)

# top = s1.pop()
# print(top)

# first = s1.peek()
# print(first)

# print(s1.size())


# class FreqStack:
#     def __init__(self):
#         self.count = {} # to track the frequency of each element
#         self.max = 0    # track the maximum frequecny
#         self.stack = {} # stacks of  every frequecy
    
#     def push(self, val:int) -> None:
#         valcnt = 1 + self.count.get(val,0)
#         self.count[val] = valcnt
        
#         if valcnt > self.max:
#             self.max = valcnt
            
#             self.stack[valcnt] = []
#         self.stack[valcnt].append(val)
    
#     def pop(self) -> int:
#         res = self.stack[self.max].pop()
        
#         self.count[res] -= 1
        
#         if not self.stack[self.max]:
#             self.max -= 1
#         return res
        
# Queue with list

    


# FS = FreqStack()
# FS.push(0)
# FS.push(2)
# FS.push(2)
# FS.push(4)
# res = FS.pop()
# print(res)
# res = FS.pop()
# print(res)

# from collections import deque

# que = deque()
# que.append(0)
# que.append(5)
# que.appendleft(10)
# print(que)
# # que.pop()
# que.popleft()
# print(que)
# print(len(que))

#Dyanamic Programming

# # fibanoci
# def fibo(n:int):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)

# print(fibo(3))

# def fibo(n:int):
#     list= [0,1]
#     for i in range(2,n+1):
#         list.append(list[i-1] + list[i-2])
#     print(list[n])
# fibo(5)
    
# list = [0,1]
# list[2] = list[1]+list[0]

# print(list[1])


