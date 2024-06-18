# Sliding Window Coding Pattern

## Fixed window problem pattern

```
# Initialization metrics/variables for the leftmost window

# This will be same in every fixed window problem
for i in range k to n-1:

  # Update the window and its metrics
  # Add the rightmost number
  # Subtract the leftmost number

  # Update the global answer based on the local answer

  return global answer (e.g. counting(sum of local answers) or optimization(min, max, avg, etc))
```
