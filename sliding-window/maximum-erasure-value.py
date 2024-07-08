# O(n) time | O(n) space - as hash table can now have n numbers
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        left = 0
        hmap = {}
        window_sum = 0
        global_max = 0

        for i in range(len(nums)):
            # Work to be done to find the maximum subarray sum ending at index i
            # with no repeating elements

            # Add a new element to the window
            window_sum += nums[i]

            # Add the element in the hmap with its frequency
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
  
            while left <= i and hmap[nums[i]] > 1:
                
                window_sum -= nums[left]
                
                hmap[nums[left]] -= 1

                if hmap[nums[left]] == 0:
                    del hmap[nums[left]]

                left += 1

            # Update the global answer
            global_max = max(global_max, window_sum)

        return global_max
