class Solution:
    def minWindow(self, s: str, t: str) -> str:


        freq_t = Counter(t)
        freq_s = defaultdict(int)
        l = 0 
        ans_len = float('inf')
        min_window_start = 0
        required = len(freq_t)
        matches = 0

        for r in range(len(s)):
            freq_s[s[r]] += 1

            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                matches += 1


            while matches == required:
                current_len = r - l + 1
                if current_len < ans_len:
                    min_window_start = l
                    ans_len = current_len
                    
                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
                    matches -= 1
                    
                l += 1

        if ans_len == float('inf'):
            return ""
                
        return s[min_window_start: min_window_start + ans_len]