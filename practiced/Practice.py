from collections import Counter
import collections

import random

arr = [random.randrange(-10, 10) for i in range(8)]
########################## Three sum
arr = [-1, 0, 1, 2, -1, -4]
arr.sort()
print("Given Array: ", arr)


def threeSum(nums):
    res = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            target = a + nums[l] + nums[r]
            if target < 0:
                l += 1
            elif target > 0:
                r -= 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res


x = threeSum(arr)
print(x)
#########################binary seargch
def bs(arr, l, r, t):
    if r >= l:
        mid = l + (r - l) // 2
        print(mid, arr[mid])
        if t == arr[mid]:
            return "Found"
        elif t < arr[mid]:
            r = mid - 1
            return bs(arr, l, r, t)
        else:
            l = mid + 1
            return bs(arr, l, r, t)
    else:
        return -1


############################Egg droping problem
def eggDrop(k, n):  # n means floors and k means eggs
    # code here
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for floor in range(1, n + 1):
        for egg in range(1, k + 1):
            dp[floor][egg] = 1 + dp[floor - 1][egg - 1] + dp[floor - 1][egg]
            print(floor, egg, dp[floor][egg])
            if dp[floor][egg] >= n:
                return floor
    return -1


##################### Two sum Problem -> Hasmap and diff of target and elements
def twosum(arr, target):
    hasMap = {}
    for i, n in enumerate(arr):
        diff = target - n
        if diff in hasMap:
            return [hasMap[diff], i]
        hasMap[n] = i


print(twosum(arr, 18))
######################### two sum ll -> two Pointer
left = 0
right = len(arr) - 1
for _ in arr:
    if (arr[left] + arr[right]) < 9:
        left += 1
    if (arr[left] + arr[right]) > 9:
        right -= 1
    if (arr[left] + arr[right]) == 9:
        print([left, right])
        break
    else:
        print("Trying ...")
