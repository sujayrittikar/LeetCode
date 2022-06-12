class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        globalInversionPairs = 0
        for cur_idx, cur_num in enumerate(nums):
            if cur_num > cur_idx:
                globalInversionPairs += cur_num - cur_idx                
            elif cur_num < cur_idx:
                globalInversionPairs += cur_idx - cur_num - 1
                
        localInversionPairs = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                localInversionPairs += 1

        return localInversionPairs==globalInversionPairs