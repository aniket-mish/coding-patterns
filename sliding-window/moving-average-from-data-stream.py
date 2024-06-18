from collections import deque

# O(1) time | O(k) space
class MovingAverage(object):

  # Initialization Phase
  def __init__(self, size):

    self.k = size
    self.total_so_far = 0.0
    self.q = deque([])

  def next(self, val):

    # Add the number in the total
    self.total_so_far += val
    q = self.q

    # Add the number in the queue
    q.append(val)

    # Check if the length of the queue is greater than k
    if len(q) > self.k:

      # Remove the top left number from the queue 
      # and subtract the number from the total as well
      self.total_so_far -= data.popleft()

    # Return the average
    return self.total_so_far / len(q)
