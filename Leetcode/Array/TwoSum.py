"""
Leetcode 1. Two Sum
Level: Easy
Memory: O(n)
Time: O(n)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
• 2 < nums. length <= 10^4
• -10^9 ≤ nums[i] ≤ 10^9
• -10^9 ≤ target ≤ 10^9
• Only one valid answer exists.

"""

from typing import List

class TwoSum(object):

    id = 'Leetcode 1. Two Sum'

    def twoSum(self, nums: List[int], target: int):
        prevMap = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in prevMap:
                return [prevMap[diff], index]

            prevMap[num] = index

    @staticmethod
    def test():
        print(f'===< TwoSum >===-----------------------')
        instance = TwoSum()

        nums1 = [2,7,11,15]
        target1 = 9
        result1 = instance.twoSum(nums1, target1)
        print(f'{nums1}: {sorted(result1)}')

        nums2 = [3,2,4]
        target2 = 6
        result2 = instance.twoSum(nums2, target2)
        print(f'{nums2}: {sorted(result2)}')

        nums3 = [3,3]
        target3 = 6
        result3 = instance.twoSum(nums3, target3)
        print(f'{nums3}: {sorted(result3)}')
