# O(n) time | O(n) space
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Variable length sliding window.

        We find the min subarray thats >= target but then when this problem is assigned to subordinate,
        he adds his number into the window and the shrinks the subarray till he gets the optimal one.
        """
        global_answer = float("inf")
        left = 0
        window_sum = 0

        # Iterate over the array
        for i in range(len(nums)):

            # Work to be done by subarrays ending at index i

            # Add the number at index i
            window_sum += nums[i]

            while left <= i and window_sum >= target:
                window_sum -= nums[left]
                global_answer = min(global_answer, i-left+1) # Length of min subarray with target as sum. All the subarrays are contributing to the global answer.
                left += 1

        if global_answer == float("inf"):
            return 0

        return global_answer



