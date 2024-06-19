nums = list(map(int, input("Enter the numbers you want to add with commas in between here:            ").split(",")))
print(nums)
nums = nums.sort()
num_search = int(input("Enter the number you would like to search for here:          "))

beg = 0
end = len(nums)-1
found = True

while beg <= end:
    mid = (beg + end)/2
    if num_search > nums[mid]:
        beg = mid + 1

    elif num_search < nums[mid]:
        end = mid - 1

    elif num_search == nums[mid]:
        print("Your number was in the list!")
        break

    else:
        found = False


if found == False:
    print("Your number was not in the list.")
