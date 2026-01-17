# Hash Maps in Python (Definition and Explanation)
# ------------------------------------------------
# A hash map (also known as a dictionary in Python) is a data structure that stores data in key-value pairs.
# Each value is associated with a unique identifier called a key.
# Unlike arrays (where elements are accessed by their integer index), hash maps use keys to access values.
# Internally, hash maps use an array, but instead of using the index directly, they use a hash function to convert the key into an array index.
# This allows for fast lookup, insertion, and deletion of values based on their keys.

# Hash Function Explanation
# ------------------------
# A hash function takes a key (which can be of any immutable type, like a string or number) and converts it into an integer.
# This integer is then used as an index to store the value in the underlying array.
# The hash function should distribute keys uniformly to avoid collisions (when two keys map to the same index).
# In Python, the built-in hash() function is used to generate hash values for keys.

# # Simple Example of a Hash Function
# def simple_hash(key, array_size):
#     """
#     A simple hash function that takes a string key and returns an index for an array of given size.
#     """
#     # Convert each character to its Unicode code point and sum them up
#     hash_sum = sum(ord(char) for char in key)
#     print(f"Hash sum for {key} is : {hash_sum}")
#     # Use modulo to ensure the index fits within the array size
#     return hash_sum % array_size

# # Example usage of simple_hash
# array_size = 10
# key = "apple"
# index = simple_hash(key, array_size)
# print(f"Index for key '{key}':", index)  # Output: Index for key 'apple': <some number between 0 and 9>

# # Example Code: Implementing a Simple Hash Map
# # --------------------------------------------
# # We'll create a basic hash map class using an array and our simple hash function.

# class SimpleHashMap:
#     """
#     A simple hash map implementation using an array and a basic hash function.
#     """
#     def __init__(self, size):
#         # Initialize the array with empty lists for handling collisions (chaining)
#         self.size = size
#         self.map = [[] for _ in range(size)]

#     def _hash(self, key):
#         # Use the simple_hash function to get the index
#         return simple_hash(key, self.size)

#     def set(self, key, value):
#         """
#         Store the value with the associated key.
#         """
#         index = self._hash(key)
#         # Check if the key already exists and update it
#         for pair in self.map[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         # If key does not exist, append it
#         self.map[index].append([key, value])

#     def get(self, key):
#         """
#         Retrieve the value associated with the key.
#         """
#         index = self._hash(key)
#         for pair in self.map[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return None  # Key not found

#     def remove(self, key):
#         """
#         Remove the key-value pair from the hash map.
#         """
#         index = self._hash(key)
#         for i, pair in enumerate(self.map[index]):
#             if pair[0] == key:
#                 del self.map[index][i]
#                 return True
#         return False  # Key not found

# # Example usage of SimpleHashMap
# hash_map = SimpleHashMap(10)
# hash_map.set("apple", 5)
# hash_map.set("banana", 10)
# hash_map.set("orange", 7)

# print(hash_map.get("apple"))   # Output: 5
# print(hash_map.get("banana"))  # Output: 10
# print(hash_map.get("grape"))   # Output: None

# hash_map.remove("banana")
# print(hash_map.get("banana"))  # Output: None



# Summary:
# - Hash maps store key-value pairs.
# - Keys are converted to array indices using a hash function.
# - Collisions (when two keys hash to the same index) are handled using chaining (storing multiple pairs in a list at each index).
# - Python's built-in dict type is a highly optimized hash map.


# from collections import defaultdict
# import heapq

# """
# Hash Maps, Hash Functions, Hash Tables, and Heaps in Python
# ===========================================================

# This file covers:
# - What are hash functions, hash tables, and hash maps?
# - How are they implemented in Python?
# - What are heaps and how are they used?
# - Example LeetCode problems using these data structures.
# - Extensive comments for beginners.

# -----------------------------------------------------------
# 1. HASH FUNCTIONS & HASH TABLES
# -----------------------------------------------------------

# A hash function takes an input (key) and returns an integer (hash value).
# A hash table uses this hash value to store and retrieve values efficiently.

# In Python, the built-in `dict` type is a hash map (hash table).
# """

# Example: Hash Function
def simple_hash(key):
    """
    A simple hash function for demonstration.
    Converts a string key to an integer by summing ASCII values.
    """
    return sum(ord(char) for char in key)

print("Hash for 'apple':", simple_hash('apple'))  # Example output

# Python's built-in hash function (used internally by dict)
print("Built-in hash for 'apple':", hash('apple'))

# """
# -----------------------------------------------------------
# 2. HASH MAPS (DICTIONARIES) IN PYTHON
# -----------------------------------------------------------

# A hash map (dictionary) stores key-value pairs.
# Keys must be hashable (immutable types like str, int, tuple).
# """

# # Creating a hash map (dictionary)
# my_map = {}
# my_map['apple'] = 5
# my_map['banana'] = 3

# # Accessing values
# print("Apples:", my_map['apple'])

# # Checking if a key exists
# if 'banana' in my_map:
#     print("Banana count:", my_map['banana'])

# # Iterating over keys and values
# for fruit, count in my_map.items():
#     print(f"{fruit}: {count}")

# # Removing a key
# del my_map['apple']

# """
# -----------------------------------------------------------
# 3. COLLISIONS & HANDLING
# -----------------------------------------------------------

# When two keys have the same hash, it's called a collision.
# Python handles collisions internally using open addressing.
# You don't need to worry about this when using dict.
# """

# Example: Two different keys with same hash (rare, but possible)
class AlwaysHash42:
    def __hash__(self):
        return 42

a = AlwaysHash42()
b = AlwaysHash42()
collision_map = {a: "first", b: "second"}
print("Collision map:", collision_map)

# """
# -----------------------------------------------------------
# 4. HASH TABLE IMPLEMENTATION (BASIC)
# -----------------------------------------------------------

# Let's implement a simple hash table for educational purposes.
# """

# class SimpleHashTable:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [[] for _ in range(size)]  # List of buckets

#     def _hash(self, key):
#         return hash(key) % self.size

#     def set(self, key, value):
#         idx = self._hash(key)
#         # Check if key exists and update
#         for i, (k, v) in enumerate(self.table[idx]):
#             if k == key:
#                 self.table[idx][i] = (key, value)
#                 return
#         # Otherwise, append new key-value pair
#         self.table[idx].append((key, value))

#     def get(self, key):
#         idx = self._hash(key)
#         for k, v in self.table[idx]:
#             if k == key:
#                 return v
#         raise KeyError(key)

#     def remove(self, key):
#         idx = self._hash(key)
#         for i, (k, v) in enumerate(self.table[idx]):
#             if k == key:
#                 del self.table[idx][i]
#                 return
#         raise KeyError(key)

# # Usage
# ht = SimpleHashTable()
# ht.set('apple', 10)
# ht.set('banana', 20)
# print("SimpleHashTable get apple:", ht.get('apple'))

# """
# -----------------------------------------------------------
# 5. LEETCODE HASH MAP PROBLEMS
# -----------------------------------------------------------

# Example 1: Two Sum (LeetCode #1)
# --------------------------------
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# """

# def two_sum(nums, target):
#     """
#     Uses a hash map to store previously seen numbers.
#     Time: O(n), Space: O(n)
#     """
#     num_to_index = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_to_index:
#             return [num_to_index[complement], i]
#         num_to_index[num] = i
#     return []

# print("Two Sum:", two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

# """
# Example 2: Group Anagrams (LeetCode #49)
# ----------------------------------------
# Group strings that are anagrams.
# """


# def group_anagrams(strs):
#     """
#     Uses a hash map with sorted tuple of characters as key.
#     """
#     anagrams = defaultdict(list)
#     for s in strs:
#         key = tuple(sorted(s))
#         anagrams[key].append(s)
#     return list(anagrams.values())

# print("Group Anagrams:", group_anagrams(["eat","tea","tan","ate","nat","bat"]))

# """
# -----------------------------------------------------------
# 6. HEAPS IN PYTHON
# -----------------------------------------------------------

# A heap is a special tree-based data structure.
# - Min-heap: Parent is less than children (smallest at root)
# - Max-heap: Parent is greater than children (largest at root)

# Python's `heapq` module implements a min-heap.
# """


# # Min-heap example
# min_heap = []
# heapq.heappush(min_heap, 5)
# heapq.heappush(min_heap, 2)
# heapq.heappush(min_heap, 8)
# print("Min-heap:", min_heap)
# print("Pop min:", heapq.heappop(min_heap))

# # Max-heap example (invert values)
# max_heap = []
# heapq.heappush(max_heap, -5)
# heapq.heappush(max_heap, -2)
# heapq.heappush(max_heap, -8)
# print("Max-heap (inverted):", max_heap)
# print("Pop max:", -heapq.heappop(max_heap))

# """
# -----------------------------------------------------------
# 7. LEETCODE HEAP PROBLEMS
# -----------------------------------------------------------

# Example 1: Kth Largest Element in an Array (LeetCode #215)
# """

# def find_kth_largest(nums, k):
#     """
#     Uses a min-heap of size k.
#     """
#     heap = nums[:k]
#     heapq.heapify(heap)
#     for num in nums[k:]:
#         if num > heap[0]:
#             heapq.heappushpop(heap, num)
#     return heap[0]

# print("Kth largest:", find_kth_largest([3,2,1,5,6,4], 2))  # Output: 5

# """
# Example 2: Merge K Sorted Lists (LeetCode #23)
# """

# def merge_k_lists(lists):
#     """
#     Uses a heap to merge k sorted lists.
#     """
#     heap = []
#     for i, l in enumerate(lists):
#         if l:
#             heapq.heappush(heap, (l[0], i, 0))  # (value, list index, element index)
#     result = []
#     while heap:
#         val, list_idx, elem_idx = heapq.heappop(heap)
#         result.append(val)
#         if elem_idx + 1 < len(lists[list_idx]):
#             next_tuple = (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1)
#             heapq.heappush(heap, next_tuple)
#     return result

# print("Merge K Lists:", merge_k_lists([[1,4,5],[1,3,4],[2,6]]))

# """
# -----------------------------------------------------------
# 8. SUMMARY
# -----------------------------------------------------------

# - Hash maps (dict) are fast for key-value storage and lookup.
# - Hash tables use hash functions to map keys to indices.
# - Heaps are used for priority queues, finding min/max efficiently.
# - Python provides built-in dict and heapq modules for these structures.
# - Practice LeetCode problems to master these concepts!
# """

