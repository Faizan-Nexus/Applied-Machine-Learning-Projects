#Linked list implementation in Python
# Node (contains data and a pointer to the next node)
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None    

# LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Head points to the first node in the list

    def traversal(self):
        current = self.head  # Start from the head node
        while current:
            print(current.data, end="->")  # Print the data of the current node
            current = current.next  # Move to the next node
        print("None")  # Indicate the end of the list

    def insert_at_start(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Point new node's next to current head
        self.head = new_node  # Update head to the new node

    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set head to new node
            return
        current = self.head  # Start from the head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Link last node to new node

    def insert_after_node(self, prev_node, data):
        current = self.head  # Start from the head
        while current and current.data != prev_node:  # Find the node with prev_node data
            current = current.next
        if not current:  # If previous node not found
            print("Previous Node not found")
            return
        new_node = Node(data)  # Create a new node
        new_node.next = current.next  # Point new node's next to current's next
        current.next = new_node  # Link current node to new node

    def delete(self, key):
        current = self.head  # Start from the head
        if current and current.data == key:  # If head node holds the key
            self.head = current.next  # Move head to next node
            return
        prev = None  # To keep track of previous node
        while current and current.data != key:  # Search for the key
            prev = current
            current = current.next
        if not current:  # If key not found
            print("Key not found")
            return
        prev.next = current.next  # Remove node by linking previous to next

# Doubly Linked List Node
class DNode:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head points to first node

    def insert_at_end(self, data):
        new_node = DNode(data)  # Create new node
        if not self.head:  # If list is empty
            self.head = new_node  # Set head to new node
            return
        current = self.head
        while current.next:  # Traverse to last node
            current = current.next
        current.next = new_node  # Link last node to new node
        new_node.prev = current  # Link new node back to last node

    def traversal(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")  # Print data
            current = current.next
        print("None")  # End of list

# Circular Linked List Node (same as Node)
# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None  # Head points to first node

    def insert_at_end(self, data):
        new_node = Node(data)  # Create new node
        if not self.head:  # If list is empty
            self.head = new_node
            new_node.next = self.head  # Point to itself
            return
        current = self.head
        while current.next != self.head:  # Traverse to last node
            current = current.next
        current.next = new_node  # Link last node to new node
        new_node.next = self.head  # Link new node to head

    def traversal(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:  # Stop when back at head
                break
        print("HEAD")
        
        #delete in circular linkedlist
        
# Leetcode Problem 1: Add Two Numbers (Medium)
# https://leetcode.com/problems/add-two-numbers/
# Each node contains a single digit. The digits are stored in reverse order.
# Add the two numbers and return the sum as a linked list.
class Solution:
    def addTwoNumbers(self, l1, l2) :
        dummy = Node()  # Dummy node to start the result list
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

# Leetcode Problem 2: Remove Nth Node From End of List (Medium)
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution2:
    def removeNthFromEnd(self, head, n):
        dummy = Node(0)  # Dummy node before head
        dummy.next = head
        fast = slow = dummy  # Two pointers
        for _ in range(n):  # Move fast n steps ahead
            fast = fast.next
        while fast.next:  # Move both pointers until fast reaches end
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next  # Remove nth node
        return dummy.next  # Return new head


l1 = LinkedList()
l1.insert_at_start(1)
l1.insert_at_end(6)
l1.insert_at_start(5)
l1.insert_after_node(5,2)
l1.traversal()

# l2 = LinkedList()
# l2.insert_at_start(0)
# l2.insert_at_end(5)
# l2.insert_at_start(8)
# l2.insert_after_node(1,2)
# l2.traversal()

# Sol = Solution()
# result  = Sol.addTwoNumbers(l1.head,l2.head)

Sol2 = Solution2()
result = Sol2.removeNthFromEnd(l1.head, 2)
# l1 = Node(2)
# l1.next = Node(4)
# l1.next.next = Node(6)

# l2 = Node(2)
# l2.next = Node(4)
# l2.next.next = Node(6)

# sol = Solution()

# result = sol.addTwoNumbers(l1,l2)

while result:
    print(result.data, end = "->" if result.next else "\n")
    result = result.next

#__init is a constructor method it automatically runs when you create an object from the class.Used to intialize or set u settings
#Self refers to current object. Each allows each object to have theri own variables

    
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = None

# def traversal(node1):
#     current_node = node1
#     while current_node is not None:
#         print(current_node.data, end=" -> ")
#         current_node = current_node.next
#     print("None")  # Indicating the end of the linked list


# def insert_after(node, new_data):
#     new_node = Node(new_data)
#     new_node.next = node.next
#     node.next = new_node
# # Example usage of insert_after
# insert_after(node2, 2.5)
# current_node = node1
# while current_node is not None:
#     print(current_node.data, end=" -> ")
#     current_node = current_node.next
# print("None")  # Indicating the end of the linked list

# def delete_node(node):
#     if node is None or node.next is None:
#         return None  # Cannot delete the last node or a non-existent node
#     node.data = node.next.data  # Copy data from the next node
#     node.next = node.next.next  # Bypass the next node

# # Example usage of delete_node
# delete_node(node2)
# current_node = node1
# while current_node is not None:
#     print(current_node.data, end=" -> ")
#     current_node = current_node.next
# print("None")  # Indicating the end of the linked list

# def find_node(head, target_data):
#     current_node = head
#     while current_node is not None:
#         if current_node.data == target_data:
#             return current_node
#         current_node = current_node.next
#     return None  # Node with target_data not found
# # Example usage of find_node
# found_node = find_node(node1, 3)
# if found_node:
#     print(f"Node with data {found_node.data} found.")
    
