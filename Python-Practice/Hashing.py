# Frequecy Map
# Create a dictionary that represetns number (key) and it's frequecny (value) in the list
# #Method 1
# nums = [0,12,21,43,12,43,134,21,54,75,32,63,23,64,21,767,98,31]
# freq = {}
# for num in nums:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

#  Method 2
freq = {}
nums = [0,12,21,43,12,43,134,21,54,75,32,63,23,64,21,767,98,31]
for i in nums:
    freq[i] = freq.get(i,0) + 1
