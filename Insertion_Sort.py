nums = [2,110000,5,4,9,8,7,1]
for i in range(len(nums)):
    min_element = 9999999
    min_loc = -1
    for j in range(i,len(nums)):
        if min_element > nums[j]:
            min_element = nums[j]
            min_loc = j
            nums[i],nums[j] = nums[j],nums[i]

print(nums)


