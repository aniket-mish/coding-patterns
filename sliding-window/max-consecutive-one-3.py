# O(n) time | O(1) space
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Variable length sliding window.
        """
        
        left = 0
        window_zeros = 0
        global_max = 0

        for i in range(len(nums)):
            # Work to be done to solve local problem ending at index i

            # Add nums[i] to the window
            if nums[i] == 0:
                window_zeros += 1

            while left <= i and window_zeros > k:
                if nums[left] == 0:
                    window_zeros -= 1
                left += 1

            if i-left+1 > global_max:
                global_max = i-left+1

        return global_max
