# O(n) time | O(1) space
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        We look at this problem in a different way.
        If we reduce the array elements so that their sum is x,
        We need to find the sum of elements that are preserved and
        thier sum is sum(nums) - x.

        Find the longest subarray of nums such that sum of 
        all elements in the subarray = K
        here k is sum(nums) - x
        """

        # Initialize
        window_sum = 0
        global_max = -1
        left = 0
        k = sum(nums)-x

        # Iterate over every subarray
        for i in range(len(nums)):

            # Work to be done by subarray ending at index i

            # Add new element in the window
            window_sum += nums[i]

            # Start shrinking the subarray
            while left <= i and window_sum > k:
                window_sum -= nums[left]
                left += 1

            # Update the global answer with the local answer
            if window_sum == k:
                global_max = max(global_max, i-left+1)

        if global_max == -1:
            return -1
        else:
            return len(nums)-global_max
        
