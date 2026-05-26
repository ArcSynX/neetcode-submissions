class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, left, right):
            if left > right:
                return -1
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(nums, target, left,   mid - 1)
            elif nums[mid] < target:
                return binary_search(nums, target,  mid + 1, right)
        left = 0
        right = len(nums) - 1
        return binary_search(nums, target, left, right)
        

# recursive method