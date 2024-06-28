# O(n) time | O(n) space
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Variable length sliding window.
        """
        
        global_count = 0
        left = 0
        window_product = 1

        for i in range(len(nums)):

            window_product *= nums[i]

            while left <= i and window_product >= k:

                # To remove the product we need to divide
                window_product /= nums[left]
                left += 1

            global_count += i-left+1 # Final subarray contributes to the global count

        return global_count
