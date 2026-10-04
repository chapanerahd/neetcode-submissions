class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return [l+1, r]

        ans = 1
        res = s[0]
        for i in range(len(s)):
            
            l, r = is_palindrome(i, i)
            if r - l + 1 >= ans:
                ans = r - l + 1
                res = s[l:r]
            l, r = is_palindrome(i, i+1)
            if r - l + 1 >= ans:
                ans = r - l + 1
                res = s[l:r]
        
        return res

            
            
        
            


            