class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def check_freq_source_in_target(source, target):
            for k, v in target.items():
                if source.get(k, 0) < v:
                    return False
            return True

        freq_t = Counter(t)
        freq_s = defaultdict(int)
        l = 0 
        ans_len = float('inf')
        min_window_start = 0

        for r in range(len(s)):
            freq_s[s[r]] += 1

            while check_freq_source_in_target(freq_s, freq_t):
                current_len = r - l + 1
                if current_len < ans_len:
                    min_window_start = l
                    ans_len = current_len
                    
                freq_s[s[l]] -= 1
                if freq_s[s[l]] == 0:
                    del freq_s[s[l]]
                    
                l += 1

        if ans_len == float('inf'):
            return ""
                
        return s[min_window_start: min_window_start + ans_len]