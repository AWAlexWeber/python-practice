'''
Given a string file path that has ../ and ./, return the absolute path.
'''

class Solution:
    def absolutePath(self, path: str) -> str:
        stack = list()
        for s in path.split('/'):
            if len(s) == 0:
                continue
            if s == '.':
                continue
            elif s == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(s)
                
        output = '/'
        for idx, p in enumerate(stack):
            output += p
            if idx < len(stack) - 1:
                output += '/'
        return output

s = Solution()
print(s.absolutePath("/users/tech/docs/.././desk/../"))