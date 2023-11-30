class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_container = []
        for value in range(len(nums)):
            for value2 in range(value):
                if nums[value] + nums[value2] == target:
                    new_container.append(value2)
                    new_container.append(value)
        return new_container


