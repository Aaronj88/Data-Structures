def search(nums, num_search, beg, end):
    mid = beg + end // 2

    if beg <= end:
        if nums[mid] == num_search:
            return mid

        elif nums[mid] < num_search:
            return search(nums, num_search, mid + 1, end)

        else:
            return search(nums, num_search, beg, mid - 1)

    else:
        return False


nums = list(
    map(
        int,
        input("Enter the numbers you want to add with commas in between here:"
              ).split(",")))
print(nums)
nums.sort()
print(nums)
num_search = int(
    input("Enter the number you would like to search for here:          "))
beg = 0
end = len(nums) - 1
found = True

print(search(nums, num_search, beg, end))
