class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        index = ""
        while i<len(s):
            l = s[i]
            if l != '#':
                index+=l
            print(index)
            if l == "#":
                res.append(s[i+1:i+1+int(index)])
                i+=int(index)
                index = ""
            i+=1
            print(i)
        return res