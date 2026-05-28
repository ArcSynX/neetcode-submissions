class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map
        dic = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in dic:
                return [dic[dif],i]

            dic[nums[i]] = i

            
        return False

        