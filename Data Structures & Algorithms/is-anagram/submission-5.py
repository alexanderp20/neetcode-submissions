class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s_dict.get(s[i], 0) > 0:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t_dict.get(t[i], 0) > 0:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
        
        for i in range(len(s)):
            if s_dict.get(s[i]) != t_dict.get(s[i]):
                return False
        
        return True