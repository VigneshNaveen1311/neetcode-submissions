class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums))]
        count = Counter(nums)
        res = []
        for i,j in count.items():
            bucket[j-1].append(i)
        print(bucket)
        for b in reversed(bucket):
            if b:
                for j in b:
                    res.append(j)
                    k-=1
            if k==0:
                break
        return res 
