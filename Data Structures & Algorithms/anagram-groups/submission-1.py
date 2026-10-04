from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        for val in strs:
            count = [0] * 26
            for char in val:
                count[ord(char) - ord('a')] += 1
            mapper['_'.join(map(str, count))].append(val)
        return list(mapper.values())
