"""
Leetcode 217. Contains Duplicate
Level: Easy
Memory: O(n)
Time: O(n)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

class ContainsDuplicate(object):

    id = 'Leetcode 217. Contains Duplicate'

    def containsDuplicate(self, nums):
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False

    @staticmethod
    def test():
        print(f'===< ContainsDuplicate >===-----------------------')
        instance = ContainsDuplicate()

        nums1 = [1,2,3,1]
        result1 = instance.containsDuplicate(nums1)
        print(f'{nums1}: {result1}')

        nums2 = [1,2,3,4]
        result2 = instance.containsDuplicate(nums2)
        print(f'{nums2}: {result2}')

        nums3 = [1,1,1,3,3,4,3,2,4,2]
        result3 = instance.containsDuplicate(nums3)
        print(f'{nums3}: {result3}')
