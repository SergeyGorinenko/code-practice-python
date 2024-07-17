"""
Leetcode 53. Maximum Subarray
Level: Medium
Memory: O(1)
Time: O(n)

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class MaximumSubarray(object):

    id = 'Leetcode 238. Product of Array Except Self'

    def maxSubArray(self, nums):
        maxSum = float('-inf')
        currSum = 0

        for num in nums:
            currSum += num
            if currSum > maxSum:
                maxSum = currSum

            if currSum < 0:
                currSum = 0

        return maxSum

    @staticmethod
    def test():
        print(f'===< MaximumSubarray >===-----------------------')
        instance = MaximumSubarray()

        nums1 = [-2,1,-3,4,-1,2,1,-5,4]
        result1 = instance.maxSubArray(nums1)
        print(f'{nums1}: {result1}')

        nums2 = [1]
        result2 = instance.maxSubArray(nums2)
        print(f'{nums2}: {result2}')

        nums3 = [5,4,-1,7,8]
        result3 = instance.maxSubArray(nums3)
        print(f'{nums3}: {result3}')
