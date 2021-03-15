''' Given a number, return the number of consecutive 1s in the binary representation of the number '''
import math

class Solution:
    def consecutiveOnes(self, k: int) -> int:
        # Basically while this is divisible by our power of 2 we continue
        # We need to calculate our starting position by doing a log2 and rounding down
        startingPower = math.floor(math.log(k, 2))
        maximumConsecutive, currentConsecutive = 0, 0
        while k > 0:
            if 2**startingPower > k:
                maximumConsecutive = max(maximumConsecutive, currentConsecutive)
                currentConsecutive = 0
            else:
                k -= (2**startingPower)
                currentConsecutive += 1
            startingPower -= 1
        maximumConsecutive = max(maximumConsecutive, currentConsecutive)
        return maximumConsecutive

#242 - 2^7, 128 = 114
#114 - 2^6, 64 = 50
#50 - 2^5, 32 = 18
#18 - 2^4, 16 = 2
#2 - 2^3, 8 !=
#2- - 2^2, 4 !=
#2 - 2^2, 2 = 0
# consecutive = 4

s = Solution()
print(s.consecutiveOnes(4096))