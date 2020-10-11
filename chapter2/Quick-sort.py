"""Quick sort"""

def quicksort(nums):
    if not nums:
        return False
    length = len(nums)
    if length == 1:
        return nums
    if length == 2:
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        return nums
    # Need shuffle first in practice
    flag = nums[0]
    l = 1
    r = length-1
    while l < r:
        if nums[l] <= flag:
            l += 1
            if l >= length:
                break
        if nums[r] > flag:
            r -= 1
            if r <= 0:
                break
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
    nums[r], nums[0] = nums[0], nums[r]
    nums[:r] = quicksort(nums[:r])
    nums[r:] = quicksort(nums[r:])
    return nums


if __name__ == "__main__":
    list0 = [23, 3, 1, 4, 6, 70, 90213, 24, 1, 7, 15, 89, 213]
    list0 = quicksort(list0)
    print(list0)