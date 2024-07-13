"""
Leetcode 238. Product of Array Except Self
Level: Medium
Memory: O(1)
Time: O(n)

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class ProductOfArrayExceptSelf(object):

    id = 'Leetcode 238. Product of Array Except Self'

    def productExceptSelf(self, nums):
        nums_count = len(nums)
        result_nums = [1] * nums_count

        product = 1
        for index in range(0, nums_count - 1, 1):
            product = product * nums[index]
            result_nums[index + 1] = product

        product = 1
        for index in range(nums_count - 1, 0, -1):
            product = product * nums[index]
            result_nums[index - 1] = product * result_nums[index - 1]

        return result_nums

    @staticmethod
    def test():
        print(f'===< ProductOfArrayExceptSelf >===-----------------------')
        instance = ProductOfArrayExceptSelf()

        nums1 = [1,2,3,4]
        result1 = instance.productExceptSelf(nums1)
        print(f'{nums1}: {result1}')

        nums2 = [-1,1,0,-3,3]
        result2 = instance.productExceptSelf(nums2)
        print(f'{nums2}: {result2}')
