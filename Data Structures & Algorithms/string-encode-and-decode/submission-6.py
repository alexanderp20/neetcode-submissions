class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + '#' + string
        print(encoded)
        return encoded
    
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            num = ""
            while s[j] != '#':
                num += s[j]
                j+=1
            start = i + len(num) + 1
            num = int(num)
            end = start + num
            strs.append(s[start:end])
            i = end

        return strs