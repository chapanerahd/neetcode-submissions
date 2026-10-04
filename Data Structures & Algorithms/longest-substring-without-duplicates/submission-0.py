class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_to_idx = dict()
        ans = 0
        left = right = 0
        while right < len(s):
            if s[right] in char_to_idx:
                left = max(left, char_to_idx[s[right]] + 1)
            
            char_to_idx[s[right]] = right
            ans = max(ans, right - left + 1) 
            right += 1
        
        return ans


