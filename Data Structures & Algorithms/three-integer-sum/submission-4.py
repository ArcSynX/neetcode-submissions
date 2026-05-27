class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 1st try on 2020526 after look at solution 
        
        # I think this problem is kinda like two sum
        # let say a + b + c = 0 
        # we can view this as: a + b = -c

        # so what I think is using two pointer
        # we first sort the number (because we wanna use two pointer method)
        # use for loop to fixed the first number i 
        # then the range after the number i, we use right/left pointer to find it

        nums.sort() # sort first since we wanna use two pointer method
        res = [] # make an empty list for storing answer

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # skip if 
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # we move on to check other pairs
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res






        