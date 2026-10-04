class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = ans = 0
        freq = defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(freq.values())
            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
            ans = max(ans, r - l + 1)
        return ans
       
