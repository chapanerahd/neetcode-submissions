class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = dict()
        
        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord('a')] += 1
            
            
            if not "_".join(map(str, key)) in anagram_groups:
                anagram_groups["_".join(map(str, key))] = []
            anagram_groups["_".join(map(str, key))].append(string)

        return list(anagram_groups.values())
            

