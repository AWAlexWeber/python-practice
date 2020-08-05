'''
1309. Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
 

Constraints:

1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
'''

# This is an okay solution
# O(n) but high constants
class Solution:
    def freqAlphabets(self, s: str) -> str:
        # We will move through the array s with a slice of size 2
        # That way we can always tell if this is a set of numbers with hashes or not
        i, n, o, c = 0, 2, "", ""
        while i < len(s):
            if n < len(s) and s[n] == '#':
                c = s[i:n]
                i = n + 1
                n += 3
                
            else:
                c = s[i]
                i += 1
                n += 1
                
            o += self.map(c)
            
        return o

                
    def map(self, s: str) -> str:
        return chr(int(s) + 96)