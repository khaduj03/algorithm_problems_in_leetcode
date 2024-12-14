class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1

        while low <= high:
            mid=(low+high)//2
            guess=nums[mid]

            if guess==target:
                return mid #found Item
            elif target<guess:
                high=mid-1   # Search in the left half
            else:
                low=mid+1   # Search in the right half
        return -1 #item not found

        