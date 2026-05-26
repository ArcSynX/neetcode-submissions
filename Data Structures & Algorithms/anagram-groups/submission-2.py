class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for i in strs:
            
            c = "".join(sorted(i))
            if c in table:
                table[c].append(i)
            else:
                table[c] = [i]

        return list(table.values())
        



        