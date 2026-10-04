class Solution:
    def countSubstrings(self, s: str) -> int:

        def is_palindrome(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            return res

        
        count = 0
        for i in range(len(s)):
            count += is_palindrome(i, i)
            count += is_palindrome(i, i + 1)
        return count


        