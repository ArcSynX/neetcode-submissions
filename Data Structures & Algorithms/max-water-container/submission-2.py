class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2025-05-27

        # area = (right index - left index) * min (height[left], height[right])

        # brute force - try every combination and get the biggest
        # two for loop O(n^2)
        res = []
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                area = (j - i) * min(heights[j], heights[i])
                res.append(area)

        return max(res)



        