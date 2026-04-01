class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cdict = defaultdict(list)
        for i,s in enumerate(strs):
            ss=''.join(sorted(s))
            cdict[ss].append(s)
        return list(cdict.values())