class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        l = 0
        max_length = 0
        most_common = 0

        for r in range(len(s)):
            charDict[s[r]] = charDict.get(s[r], 0) + 1
            most_common = max(most_common, charDict[s[r]])

            while len(s[l:r+1]) - most_common > k:
                charDict[s[l]] -= 1
                l += 1

            max_length = max(max_length, len(s[l:r+1]))
            
        return max_length