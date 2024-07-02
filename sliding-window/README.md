# Sliding Window Coding Pattern

## Fixed length sliding window pattern

_Easy to figure out as problems have `size=k`_

> [!NOTE]
> Brute force: exhaustively search for all the sub-arrays of size k
> time complexity: O(nk) as O(k) time per sub-array

```python
# Initialization metrics/variables for the leftmost window

# This will be same in every fixed window problem
for i in range k to n-1:

  # Update the window and its metrics
  # Add the rightmost number
  # Subtract the leftmost number

  # Update the global answer based on the local answer

return global answer (e.g. counting(sum of local answers) or optimization(min, max, avg, etc))
```

## Variable length sliding window pattern

```python
# Initialization metrics/variables

# Decrease and conquer
for i in range 0 to n-1:

  # Work to be done to compute local answer for subarray ending at index i
  # Incoporate nums[i] to the window

  while left <= i and left has not reach the "boundary":
      # Update window metrics
      left += 1

  # Local answer would be available here and we can use that to update global answer

return global answer

  # Update the global answer based on the local answer

  return global answer (e.g. counting(sum of local answers) or optimization(min, max, avg, etc))
```
