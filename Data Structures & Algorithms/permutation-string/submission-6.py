class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_list = [0] * 26

        for i in range(len(s1)):
            s1_list[ord(s1[i]) - 97] += 1

        for r in range(len(s2)):
            if s1_list[ord(s2[r]) - 97] == 0:
                l += 1
            elif len(s2[l:r+1]) == len(s1):
                substring = [0] * 26
                for i in range(len(s1)):
                    substring[ord(s2[l:r+1][i]) - 97] += 1
                if substring == s1_list:
                    return True
                l += 1
                
        return False