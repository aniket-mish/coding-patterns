# O(n) time | O(1) space
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        # Initialization: sum of the leftmost subarray
        window_sum = sum(arr[:k])

        # Instead of checking if average is greater than or equal to threshold
        # We check if sum is greater than or equal to (threshold * k)
        # This is for only the leftmost window
        if window_sum >= (threshold * k):
            count = 1
        else:
            count = 0

        # For the next sub-arrays we iterate
        for i in range(k, len(arr)):

            # Update metrics/variables
            window_sum += arr[i] # Add the rightmost number
            window_sum -= arr[i-k] # Subtract the leftmost number

            # Update global answer
            if window_sum >= (threshold * k):
                count += 1

        return count

        
