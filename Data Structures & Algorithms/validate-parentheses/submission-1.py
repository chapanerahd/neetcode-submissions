class Solution:
    def isValid(self, s: str) -> bool:
        close_open_pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for idx in range(len(s)):
            if s[idx] not in close_open_pairs:
                stack.append(s[idx])
            else:
                if not stack or close_open_pairs[s[idx]] != stack.pop():
                    return False
                    
        return False if stack else True
        


        