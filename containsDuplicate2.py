# Worst case
def containsNearbyDuplicate(nums, k):
    for num in nums:
        if nums.count(num)>1:
            indices = [i for i in range(len(nums)) if nums[i]==num]
            indices = sorted(indices)
            for index in indices:
                for index1 in indices:
                    if index1!=index and abs(index1-index)<=k:
                        return True
    return False

# Best Case:
def containsNearbyDuplicate(nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False

print(containsNearbyDuplicate([1,2,3,1,2,3], 2))