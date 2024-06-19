# Fixed window problem

# O(n) time | O(1) space
def findMaxAverage(self, nums: List[int], k: int) -> float:

  # initialization metrics/variables for the leftmost window
  window_sum = sum(nums[:k])
  max_window_sum = window_sum

  # this will be same in every fixed window problem
  for i in range(k, len(nums)):
    
    # work to be done on the subproblem ending at i

    # update the window and its metrics
    window_sum += nums[i] # add the rightmost number
    window_sum -= nums[i-k] # subtract the leftmost number

    # update the global answer based on the local answer
    max_window_sum = max(max_window_sum, window_sum)

  return max_window_sum/k
            

        
