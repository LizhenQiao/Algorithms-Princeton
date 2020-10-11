"""Shell sort"""


def shellsort(nums):
    # initialize h
    length = len(nums)
    h = 1
    while h < length/3:
        h = 3*h + 1
    while h >= 1:
        for i in range(h, length):
            j = i
            while j > h-1:
                if nums[j] < nums[j-h]:
                    nums[j], nums[j-h] = nums[j-h], nums[j]
                    j -= h
                else:
                    break
        h //= 3

# O(n^k), k =4/3; 5/4 ...
