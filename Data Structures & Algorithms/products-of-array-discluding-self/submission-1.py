class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1]*len(nums), [1]*len(nums)
        for i in range(1,len(nums)):
            prefix[i] *= nums[i-1]*prefix[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] *= nums[i+1]*suffix[i+1]
        print(prefix,suffix)
        for i in range(len(nums)):
            nums[i] = prefix[i]*suffix[i]
        return nums
