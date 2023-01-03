class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            number2 = target - nums[i]

            if number2 in nums and nums.index(number2) != i:
                a = [nums.index(number2), i]
                return a
print(Solution.twoSum(None, [2,7,11,15], 9))