from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False
        
        freq_s, freq_t = Counter(s), Counter(t)
        for char_s, freq_s in freq_s.items():
            if freq_t.get(char_s, 0) != freq_s:
                return False
        return True
            

        