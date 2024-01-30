def merge_sort(nums: list[int], start: int, end: int):
    if start < end:
        mid = (start + end) // 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid + 1, end)
        merge(nums, start, mid, end)
    return nums


def merge(nums: list[int], start: int, mid: int, end: int):
    temp = [-1] * (end - start + 1)
    i, j, k = start, mid + 1, 0
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            temp[k] = nums[i]
            k += 1
            i += 1
        else:
            temp[k] = nums[j]
            k += 1
            j += 1
    while j <= end:
        temp[k] = nums[j]
        k += 1
        j += 1
    while i <= mid:
        temp[k] = nums[i]
        k += 1
        i += 1
    nums[start : end + 1] = temp
    return nums


print(merge_sort([5, 4, 3, 6], 0, 3))
