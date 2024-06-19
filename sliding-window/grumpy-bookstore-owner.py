# O(n) time | O(1) space
def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
  # Start thinking with a decrease and conquer method and you realize its a fixed sliding window pattern
  
  # Initialization phase
  # k is the meditation mins (window size)
  k = minutes

  # numhappy for the satisfied customers (leftmost window)
  numhappy = 0
  for i in range(len(customers)):
    if grumpy[i] == 0:
      numhappy += customers[i]

  # numangry for the unsatisfied customers
  numangry = 0
  for i in range(k):
    if grumpy[i] == 1:
      numangry += customers[i]

  # global result
  globalmax = numangry

  for i in range(k, len(customers)):
    # Compute angry customers in each windows ending at i
            
    # Update window and the metrics
    if grumpy[i] == 1:
      # Add the rightmost number
      numangry += customers[i]
            
    if grumpy[i-k] == 1:
      # Subtract the leftmost number
      numangry -= customers[i-k]

      # Update the global answer using the local answer
      globalmax = max(globalmax, numangry)
  
  # customers that are satisfied from the start + customers that are converted because of owners meditation time
  return numhappy + globalmax
