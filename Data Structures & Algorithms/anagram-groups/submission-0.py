class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings_dict = {}
        for i in range(len(strs)):
            string_array = [0]*26
            for m in range(len(strs[i])):
                string_array[ord(strs[i][m]) - ord('a')] += 1
            if tuple(string_array) in strings_dict:
                strings_dict[tuple(string_array)].append(strs[i])
            else:
                strings_dict[tuple(string_array)] = [strs[i]]

        return list(strings_dict.values())