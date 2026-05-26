class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters
        regex = r"[^a-zA-Z0-9]"
        filtered_str = re.sub(regex, "", s).lower()
        print(filtered_str)



 
        return filtered_str[::-1] == filtered_str