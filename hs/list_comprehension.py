class Solution:
    def twoSum(self, *nums, target):
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], i]
            else:
                dict[num] = i

    num = [n for n in range(9999999)]
    target = 1
    print(twoSum(num, target=10))
