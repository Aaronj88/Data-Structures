def merge_sort(nums, beg, mid, end):
    c = []
    start1 = beg
    start2 = mid + 1

    while start1 <= mid and start2 <= end:
        if nums[start1] < nums[start2]:
            c.append(nums[start1])
            start1 += 1

        else:
            c.append(nums[start2])
            start2 += 1

    while start1 <= mid:
        c.append(nums[start1])
        start1 += 1

    while start2 <= end:
        c.append(nums[start2])
        start2 += 1

    k = 0
    for i in range(beg, end + 1):
        nums[i] = c[k]
        k += 1


def merge_sort2(nums, beg, end):
    if beg < end:
        mid = (beg + end) // 2
        merge_sort2(nums, beg, mid)
        merge_sort2(nums, mid + 1, end)
        merge_sort(nums, beg, mid, end)


nums = [79, 64, 347, 949, 1151, 9, 12, 8]
print(nums)
n = len(nums)
merge_sort2(nums, 0, n - 1)
print(nums)
