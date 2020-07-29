'''
535. Encode and Decode TinyURL

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''

# Note that this is a system design question
# There is no 'right' answer
class Codec:
    
    def __init__(self):
        self.url = "http://tinyurl.com/"
        self.map = {}
        self.tiny = "a"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # We are simply going to map to a dictionary
        # Encoding to our map
        fullUrl = self.url + self.tiny

        # Incrementing our url
        self.incrementUrl()

        self.map[fullUrl] = longUrl
        
        return fullUrl
    
    def incrementUrl(self):
        a, i = [char for char in self.tiny], len(self.tiny) - 1
        for c in a[::-1]:
            # If we are at z in our tiny, we need increment our left
            if c == 'z':
                a[i] = 'a'
                i -= 1
                continue

            # Otherwise we just increment our tiny
            else:
                # Increments our url
                nc = chr(ord(c[0]) + 1)
                a[i] = nc
                break

        if i == -1 and c =='z':
            self.tiny = 'a' + ''.join(a)
        else:
            self.tiny = ''.join(a)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
for i in range(0,1500000):
    tinyUrl = codec.encode("https://www.leetcode.com/problems/design-tinyurl")

tinyUrl = codec.encode("https://www.leetcode.com/problems/design-tinyurl")
print(tinyUrl)
print(codec.decode(tinyUrl))