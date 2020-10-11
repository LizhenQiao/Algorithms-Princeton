"""Merge sort"""

import numpy as np


def mergesort(nums):
    length = len(nums)
    if length <= 1:
        return nums

    list0 = np.zeros(shape=length)
    mid = length // 2
    nums[:mid] = mergesort(nums[:mid])
    nums[mid:] = mergesort(nums[mid:])
    i = 0
    j = mid
    k = 0
    while k < length:
        if i == mid:
            list0[k:] = nums[j:]
            break
        elif j == length:
            list0[k:] = nums[i:mid]
            break
        else:
            if nums[i] <= nums[j]:
                list0[k] = nums[i]
                i += 1
                k += 1
            else:
                list0[k] = nums[j]
                j += 1
                k += 1
    return list0


# O(NlgN) ; Extra storage N

# Ways to improve: 1.list0-nums exchange each time. Save time of copy data.
#                  2.compare a[mid-1] and a[mid] each time. if a[mid-1]<a[mid]: merge directly : a[:mid-1] + a[mid:]
#                  3.When come to small list, use easier sorting algorithms instead of merge sort.
# plus: bottom-up also works.
