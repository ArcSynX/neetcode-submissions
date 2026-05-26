class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result += str(length) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s): # exceed the str length then we stop
             
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j]) # index i to j -1 

            word = s[j+1 : j+1+length]

            result.append(word)

            i = j+1+length
        return result 
        
