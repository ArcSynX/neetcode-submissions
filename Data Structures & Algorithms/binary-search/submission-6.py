class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 # index
        right = len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            mid = (right + left) // 2

        return -1
            

            
        

# iterate