nums = [0,6,1,2]

for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]



print(nums)

nums.sort() #Sorts the list in ascending order
print(nums)
nums.sort(reverse = True) #Reverses it and sorts the list in descending order
print(nums)
