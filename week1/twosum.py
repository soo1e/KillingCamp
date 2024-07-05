nums = [4,9,7,5,1]
target = 14
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == 14:
           print([i,j])