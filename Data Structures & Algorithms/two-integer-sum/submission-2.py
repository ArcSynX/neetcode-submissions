class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        # key: nums, value: index 

        for i in range(len(nums)):

            difference = target - nums[i] # we want find: differnce = nums[j]

            # first search and then store the key-value in the dict to avoid refer to itself
            if difference in table:

                return [table[difference],i]


            else:
                table[nums[i]] = i 
 
        
# better solution using hash table