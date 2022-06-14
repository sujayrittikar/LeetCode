class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        for num in nums:
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 1
        c = 0
        if 0 in d.keys():
            for j in range(d[0]):
                nums[c] = 0
                c+=1
        if 1 in d.keys():
            for j in range(d[1]):
                nums[c] = 1
                c+=1
        if 2 in d.keys():
            for j in range(d[2]):
                nums[c] = 2
                c+=1