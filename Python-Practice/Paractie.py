class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        current = self.head
        while current:
            print(current.data, end= "->")
            current= current.next
        print("None")
    
    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_after_node(self,node,data):
        new_node = Node(data)
        current = self.head
        while current and current.data != node:
            current = current.next
        if not current:
            print("Previous Node does not exist")
            return
        new_node.next = current.next
        current.next = new_node
    
    def delete(self,value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if not current:
            print("Key not found!")
            return
        prev.next = current.next
                    
        

# L1= LinkedList()
# L1.insert_at_end(15)
# L1.insert_at_start(10)
# L1.insert_at_start(5)
# L1.insert_after_node(15,20)
# L1.insert_after_node(20,32)
# L1.insert_after_node(32,62)
# L1.delete(32)
# L1.delete(62)
# L1.traversal()


# class DoubleNode:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class Doubly:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_start(self, data):
#         new_node = DoubleNode(data)  # Create a new node with the given data
#         new_node.next = self.head  # Point new node's next to current head
#         self.head = new_node  # Update head to the new node
    
#     def insert_at_end(self,data):
#         new_node = DoubleNode(data)
#         current = self.head
        
#         if not self.head:
#             self.head = new_node
        
#         while current.next:
#             current = current.next
#         current.next = new_node
#         new_node.prev = current.next
        
    
#     def insert_after_node(self,data,node):
#         new_node = DoubleNode(data)
#         current = self.head
#         while current and current.data != node:
#             current = current.next
        
#         if not current:
#             print("Previous node does not exist")
#             return
#         new_node.next = current.next
#         new_node.prev = current
#         if current.next is not None:
#             current.next.prev = new_node
#         current.next = new_node
#     def traversal(self):
#         current = self.head
#         while current:
#             print(current.data, end=" <-> ")  # Print data
#             current = current.next
#         print("None")  # End of list
    
#     def delete(self, key):
#         current = self.head  # Start from the head
#         if current and current.data == key:  # If head node holds the key
#             self.head = current.next  # Move head to next node
#             return
#         prev = None  # To keep track of previous node
#         while current and current.data != key:  # Search for the key
#             prev = current
#             current = current.next
#         if not current:  # If key not found
#             print("Key not found")
#             return
#         prev.next = current.next  # Remove node by linking previous to next

        

    
    
# D1 =Doubly()
# D1.insert_at_start(5)
# D1.insert_at_end(10)
# D1.insert_after_node(15,10)
# D1.insert_after_node(12,10)
# D1.insert_at_end(20)
# D1.delete(12)
# D1.traversal()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next  = self.head
        self.head = new_node
    
    def traversal(self):
        current = self.head
        while current:
            print(current.data, end = " -> " if current.data else "\n")
            current = current.next
        print("End")
    
    def insert_at_end(self,data):
        new_node = Node(data)
        current = self.head
        if not self.head:
            new_node.next  = self.head
            self.head = new_node
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_after_node(self,node,data):
        curr = self.head
        while curr and curr.data != node:
            curr = curr.next
        if not curr:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node
     
    def delete(self,key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            return
        prev = None
        
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if not curr:
            print("Key not found")
            return
        prev.next = curr.next
    
    def insert_list(self,list):
        for num in reversed(list):
            self.insert_at_start(num)
        

class DoublyNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        

class Doubly:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        current = self.head
        while current:
            print(current.data, end = " -> " if current.data else "\n")
            current = current.next 
        print("End")

    def insert_at_start(self,data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = DoublyNode(data)
        current = self.head
        if not self.head:
            new_node.next  = self.head
            self.head = new_node
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    
    def insert_after_node(self,node,data):
        curr = self.head
        while curr and curr.data != node:
            curr = curr.next
        if not curr:
            print("Previous node does not exist")
            return
        new_node = DoublyNode(data)
        new_node.next = curr.next
        curr.next = new_node
        new_node.prev = curr
    
    def delete(self,key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            return
        last = None
        
        while curr and curr.data != key:
            last = curr
            curr = curr.next
        if not curr:
            print("Key not found")
            return
        last.next = curr.next
        curr.prev =  last
    
    def insert_list(self,list):
        for num in reversed(list):
            self.insert_at_start(num)
        

list = [1,2,3,4]
    
D1 = Doubly()
D1.insert_list([7,8,9])
# D1.insert_at_start(5)
# D1.insert_after_node(5,6)
# D1.insert_at_start(7)
# D1.insert_after_node(7,5)
# D1.insert_at_end(7)
# D1.delete(5)
# D1.delete(7)
D1.traversal()
 
        
# L1 = LinkedList()
# L1.insert_list(list)
# # L1.insert_at_start(5)
# # L1.insert_after_node(5,6.5)
# # L1.insert_at_end(8)
# # L1.delete(8)
# # L1.insert_at_start(10)
# # L1.insert_at_start(15)
# L1.traversal()



class Solution:
    def addTwoNumbers(self, l1, l2) :
        dummy = Node(0)  # Dummy node to start the result list
        current = dummy  # Pointer to build the result list
        carry = 0  # Carry for sum > 9
        while l1 or l2 or carry:
            val1 = l1.data if l1 else 0  # Get value from l1 or 0
            val2 = l2.data if l2 else 0  # Get value from l2 or 0
            total = val1 + val2 + carry  # Add values and carry
            carry = total // 10  # Update carry
            current.next = Node(total % 10)  # Create new node with digit
            current = current.next  # Move to next node
            if l1: l1 = l1.next  # Move l1 pointer
            if l2: l2 = l2.next  # Move l2 pointer
        return dummy.next  # Return result list (skip dummy)

L1 = LinkedList()
L1.insert_at_start(5)
L1.insert_at_start(0)
L1.insert_at_end(10)

L2 = LinkedList()
L2.insert_at_start(0)
L2.insert_at_end(5)
L2.insert_at_start(8)
L2.traversal()


sol = Solution()

result = sol.addTwoNumbers(L1.head, L2.head)
while result:
    print(result.data, end=" -> " if result.next else "\n")
    result = result.next