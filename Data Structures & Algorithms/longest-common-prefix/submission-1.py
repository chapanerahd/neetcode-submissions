class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longest_common_prefix = []
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for j in range(1, len(strs)):
                
                if i >= len(strs[j]) or strs[j][i] != current_char:
                    return "".join(longest_common_prefix)
            longest_common_prefix.append(current_char)

        return "".join(longest_common_prefix)
        