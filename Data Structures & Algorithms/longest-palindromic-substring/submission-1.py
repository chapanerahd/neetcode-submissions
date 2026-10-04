class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return [l+1, r]

        best_start = 0
        best_length = 1
        for i in range(len(s)):
            
            l, r = is_palindrome(i, i)
            if r - l > best_length:
                best_start = l
                best_length = r - l
            l, r = is_palindrome(i, i+1)
            if r - l > best_length:
                best_start = l
                best_length = r - l
        
        return s[best_start: best_start+best_length]

            
            
        
            


            