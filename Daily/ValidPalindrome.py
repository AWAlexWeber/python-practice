class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, b = 0, len(s) - 1
        while i < b:
            # Skipping if its non alphanumeric
            while (not s[b].isnumeric() and not s[b].isalpha()) and b > 0:
                b -= 1

            while (not s[i].isnumeric() and not s[i].isalpha()) and i < b:
                i += 1
            
            if s[b].lower() != s[i].lower() and i < b:
                return False

            b -= 1
            i += 1
        return True

s = Solution()
print(s.isPalindrome(""))
print(s.isPalindrome("1"))
print(s.isPalindrome("11"))
print(s.isPalindrome("121"))
print(s.isPalindrome("0P"))
print(s.isPalindrome("A man, a plan, a canal:                                    !!! ! !!! ! ! ! ! ! ! ! !  Panama"))
print(s.isPalindrome("\"Sue,\" Tom smiles, \"Selim smote us.\""))