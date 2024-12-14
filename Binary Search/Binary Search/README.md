# Binary Search Algorithm

This repository contains a Python implementation of the Binary Search algorithm, which is a faster method of searching for an element in a sorted list. Instead of checking each item one by one, binary search divides the list into two parts and repeatedly checks the middle element, narrowing down the search range.

## How Binary Search Works

- We start with two pointers: `low` and `high`, which represent the range of the list to search within. Initially, `low` is set to the first index (0) and `high` is set to the last index of the list.
  
- We calculate the middle element using the formula `mid = (low + high) // 2`.

- If the middle element matches the target element, the search ends and returns the index of the element.

- If the target element is smaller than the middle element, we narrow the search to the left half by setting `high = mid - 1`.

- If the target element is larger than the middle element, we narrow the search to the right half by setting `low = mid + 1`.

- This process repeats until the element is found or the search range is exhausted.

## Advantages of Binary Search

- **Efficiency**: Binary Search is much faster than linear search because it divides the search range in half at each step.
- **Logarithmic Time**: In the worst case, the number of steps required to find an element is proportional to `log2(n)`, where `n` is the size of the list. For example, a list with 1000 elements requires only about 10 steps to search for an element.

## Important Notes

- Binary Search requires the list to be **sorted**. It will not work on unsorted lists.
- Compared to linear search, where every element is checked, binary search significantly reduces the number of comparisons needed.
`

## LeetCode Problem

You can view and solve the [LeetCode Binary Search problem here](https://leetcode.com/problems/binary-search/description/?envType=study-plan-v2&envId=binary-search) for more details and practice.

This problem provides a practical way to apply the Binary Search algorithm to a real coding challenge. Try solving it directly on LeetCode to test and improve your understanding.
