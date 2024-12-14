# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums.
#  If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

def search_binary(item, my_list):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        
        if item == guess:
            return mid  # Item found
        elif item < guess:
            high = mid - 1  # Search in the left half
        else:
            low = mid + 1  # Search in the right half
    return None  # Item not found

