"""Insertion sort"""


def insertionsort(nums):
    length = len(nums)
    for i in range(length):
        j = i
        while j > 0:
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            else:
                break

# O(n^2)
