# O(n) time | O(n) space
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Variable length sliding window.

        We need to use concepts from fixed length sliding window pattern like
        the max and min. So we can use 2 double ended queues to keep track of min and max
        elements.
        """

        # Initialize empty queues
        max_d = deque([])
        min_d = deque([])
        global_max = 0
        left = 0

        for i in range(len(nums)):

            # Work to be done for calculating size of longest subarray
            # ending at index i such that the diff between any two numbers
            # is less then `limit`

            # Include nums[i] in the window
            # O(n) as in each either we delete something or insert something
            while len(max_d) != 0 and max_d[-1] < nums[i]:
                max_d.pop() # delete the back of the queue

            # Insert the nums[i] in the max deque
            max_d.append(nums[i])

            while len(min_d) != 0 and min_d[-1] > nums[i]:
                min_d.pop() # delete the back of the queue

            # Insert the nums[i] becaus either the min queue is empty or
            # we saw a number that is smaller than nums[i]
            min_d.append(nums[i])

            # Combined work does not exceed O(n)
            while left <= i and abs(max_d[0] - min_d[0]) > limit:
                # We are still in the left zone
                if nums[left] == max_d[0]:
                    max_d.popleft() # delete the front of the queue

                if nums[left] == min_d[0]:
                    min_d.popleft()

                left += 1

            global_max = max(global_max, i-left+1)

        return global_max
