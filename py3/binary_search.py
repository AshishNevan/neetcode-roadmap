def driver(nums: list[int], target: int) -> int:
    return binary_search(nums, 0, len(nums) - 1, target)


def binary_search(nums: list[int], l: int, r: int, target: int) -> int:
    if l > r:
        return -1
    mid = (r + l) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        return binary_search(nums, l, mid - 1, target)
    if nums[mid] < target:
        return binary_search(nums, mid + 1, r, target)


print(driver([1, 2, 3, 4], 5))
