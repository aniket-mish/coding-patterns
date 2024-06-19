def dietPlanPerformance(calories, k, lower, upper):

  # Initialization
  # metrics/variables for the leftmost window
  window_sum = sum(calories[:k])
  if window_sum > upper:
    points = 1
  elif window_sum < lower:
    points = -1
  else:
    points = 0

  # Iterate over next windows
  for i in range(k, len(calories)):

    # Update variables
    window_sum += calories[i]
    window_sum -= calories[i-k]

    if window_sum > upper:
      points += 1
    elif window_sum < lower:
      points -= 1

  return points
