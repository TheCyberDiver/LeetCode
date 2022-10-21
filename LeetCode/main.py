
###################################################################################
#             This set encompasses LeetCodes 14 day Algorithm 1 Course            #
###################################################################################
#-------------------------------------------------------------------------------------------------------------------------------
###################################################################################
#  DAY 1:                    This is Binary Search!      Q.704                    #
###################################################################################
# USEFUL: https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

def binarySearch(arrayofnums, targetint):
    left = 0
    right = len(nums) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1
    return 'Is not in array'


nums = [-4, -1, 0, 3] #Utilized for both Binary search and Two Pointer problem
target = 90 # Used for only binary search problem
print(binarySearch(nums, target))


###################################################################################
#  DAY 2:                    This is Two Pointers!                Q.977           #
###################################################################################
# Useful https://www.youtube.com/watch?v=On03HWe2tZM || https://www.youtube.com/watch?v=-gjxg6Pln50 <-better
# Notes: This is similar to Binary search but instead of a mid point it is sum
def sortedSquares(nums):
    # TWO POINTER METHOD
    left = 0
    right = len(nums) - 1
    newArray = []

    while left <= right:
        if left == right:
            newArray.append(nums[left])
            break
        newArray.append(nums[left] ** 2)
        newArray.append(nums[right] ** 2)
        left = left + 1
        right = right - 1
    return newArray

print(sortedSquares(nums))
# BRUTE FORCE METHOD
# newList = []
# for i in nums:
#     temp = i**2
#     newList.append(temp)


# return sorted(newList)

