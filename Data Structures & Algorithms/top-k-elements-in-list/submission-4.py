class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store frequency in dict
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        # then we move data from dict to list for sorting, since dict cant sort
        # sort() 是先比 list 的第一個元素，所以你想按什麼排，就把那個東西放第一位。

        pairs = []
        for num in count:
            freq = count[num]
            pairs.append([freq, num])
        
        pairs.sort()
        pairs.reverse()

        # Now let's get top k
        # for each small list we have [freq, num]
        # pair[i][0] refer to freq
        # pair[i][1] refer to num
        result = []
        for i in range(k):
            result.append(pairs[i][1])

        return result
        





        

        