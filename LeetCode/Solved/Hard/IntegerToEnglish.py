'''
273. Integer to English Words

Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 231 - 1
'''

class Solution:
    
    def numberToWords(self, num: int) -> str:
        
        if int(num) == 0:
            return "Zero"
        
        # Initializing our helper variables for mapping purposes.
        self.digits = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        self.teens = ["","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.dist = ["Hundred", "Thousand", "Million", "Billion"]
        
        
        # Using a list as it keeps our string concatenation simpler. Will be combined into a string at the end.
        output = list()
        
        # Converting num into a string
        s = str(num)
        
        # Perform this by splitting each segment into 3 digit chunks.
        # As long as we have a 3 digit chunk left, we will continue to make a 3 digit chunk
        o, i = 0, len(s) - 1
        while i >= 0:
            # Grabbing the next 3 digit chunk
            j, n = 0, ""
            while i >= 0 and j < 3:
                n += s[i]
                j += 1
                i -= 1
            
            # Flipping it
            n = n[::-1]
            intN = int(n)
            
            nextString = (self.getString(n, o))
            if len(nextString) != 0:
                output.append(nextString)
            
            # Incrementing our 'depth' counter
            o += 1
            
        final = ' '.join(output[::-1])
        return final.strip()
            
    # Helper function for converting a multiple digit value into a string
    def getString(self, n: str, depth: int) -> str:
        
        if int(n) == 0:
            return ""
        
        f = ""
        
        if len(n) == 1:
            # Returning the digit plus the depth
            f = self.digits[int(n)]
            if depth == 0:
                return f
        elif len(n) == 2:
            # Checking for teens
            if int(n) > 10 and int(n) < 20:
                f = self.teens[int(n) - 10]
            else:
                # Have to do some actual work here
                f = self.tens[(int(n) // 10) - 1]
                if int(n) % 10 != 0:
                    f = f + " " + self.digits[int(n) % 10]
            if depth == 0:
                return f
        elif len(n) == 3:
            if depth == 0:
                # Building the full set
                firstDigit = self.digits[int(n[0])]

                if int(n[0]) != 0:
                    f = firstDigit + " " + "Hundred"

                # Getting the second
                secondDigit = self.getString(str(int(n[1:])), 0)

                if int(n[1:]) != 0 and int(n[0]) != 0:
                    f = f + " " + secondDigit
                elif int(n[1:]) != 0:
                    f = secondDigit

                return f
            else:
                # We need to build the depth level 0 and then add our current depth
                f = self.getString(n, 0)
            
        
        f = f + " " + self.dist[depth]
        return f
        
        