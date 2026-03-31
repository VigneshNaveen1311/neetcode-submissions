class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs,ct = {},{}
        for i in s:
            print(i)
            cs[i] = cs.get(i,0) + 1
        for i in t:
            print(i)
            ct[i] = ct.get(i,0) + 1
        print(cs,ct)
        return cs == ct