# O(n) time | O(1) space
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        Instead of focusing on choosing the k cards(two separate subarrays)
        we can focus on choosing a single subarray with n-k cards
        whose combined score is minimized.

        So we reverse the problem.

        Choose the subarray of size n-k with minimum total score
        In end we can compute the score that was taken away and can be the output

        This is a problem reduction technique
        """

        # Initialize the metrics for the leftmost window
        L = len(cardPoints)-k # n-k
        window_sum = sum(cardPoints[:L])
        global_min = window_sum

        for i in range(L, len(cardPoints)):
            # Use template for fixed length sliding window pattern
            # Work to be done to calc min score of the subarray ending at index i

            # Add new element in the window
            window_sum += cardPoints[i]

            # Remove the element of last subarray from the window
            window_sum -= cardPoints[i-L]

            # Update the global minimum using local minimum
            global_min = min(global_min, window_sum)

        # Return the maximum sum which is asked in the question 
        return sum(cardPoints) - global_min
