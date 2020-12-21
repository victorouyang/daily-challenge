def is_positive_list(nums) -> bool:
    for i in nums:
        if i >= 0:
            return True
    return False


def maxSubArray(nums: list[int]) -> int:
    max_so_far = 0
    max_ending_here = 0

    if not is_positive_list(nums):
        return max(nums)

    for i in nums:
        max_ending_here = max_ending_here + i
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if (max_ending_here < 0):
            max_ending_here = 0
    return max_so_far

l = [-2,1,-3,4,-1,2,1,-5,4]
assert 6 == maxSubArray(l)

l=[-1]
assert -1 == maxSubArray(l)

l = [-5,-6,-7,-2]
assert -2 == maxSubArray(l)

l=[0]
assert 0 == maxSubArray(l)


