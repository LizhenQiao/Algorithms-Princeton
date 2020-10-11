"""Selection sort"""


def selectionsort(nums):
    length = len(nums)
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

# O(n^2)

