'''

Problem:

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

'''


def permute(nums):
    if (len(nums) == 1):
            return [nums]

    output = []
    for l in permute(nums[1:]):
        for idx in range(len(nums)):
            output.append(l[:idx] + [nums[0]] + l[idx:])
    return output



# Recursive function

def permute(nums):
    def helper(nums, index, output):
        if index == len(nums) - 1:
            output.append(nums.copy())
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            helper(nums, index + 1, output)
            nums[index], nums[i] = nums[i], nums[index]

    output = []
    helper(nums, 0, output)
    return output