class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        
        resLen = 1001
        res = ""

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if len(s[l:r+1]) < resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        return res