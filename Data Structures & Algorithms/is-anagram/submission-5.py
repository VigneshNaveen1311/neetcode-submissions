class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs,ct = {},{}
        for i in s:
            cs[i] = cs.get(i,0) + 1
        for i in t:
            ct[i] = ct.get(i,0) + 1
        return cs == ct