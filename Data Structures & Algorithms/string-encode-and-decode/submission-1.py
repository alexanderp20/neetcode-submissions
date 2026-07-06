class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += string + '.'

        return encoded
    
    def decode(self, s: str) -> List[str]:
        strings = s.split(".")
        strings.pop()

        return strings