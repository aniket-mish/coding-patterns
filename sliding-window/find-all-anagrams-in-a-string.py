# O(m + n) time | O(1) space

def permutation_in_string(s1, s2):
  """
  Use decrease and conquer approach and see how its a fixed length sliding window problem.
  Use the coding pattern discussed.

  The understanding is that if the frquency dict is the same then the permutation exists.

  Similar code to permutation-in-string problem.
  """
  out = []

  # Initialization
  hmap_s1 = {}
  for i in range(len(s1)):
    if s1[i] in hmap_s1:
      hmap_s1[s1[i]] += 1
    else:
      hmap[s1[i]] = 1


  # Leftmost window
  k = len(s1)
  hmap = {}
  for i in range(len(s2)):
    if len(s2) >= k:
      if s2[i] in hmap:
        hmap[s2[i]] += 1
      else:
        hmap[s2[i]] = 1

  # Compare the dicts
  if hmap_s1 == hmap:
    return out.append(i-k+1) # as substring begins at i-k+1

  # Iterate over next subarrays
  for i in range(k, len(s2)):

    # Add the element at ith place
    if s2[i] in hmap:
      hmap[s2[i]] += 1
    else:
      hmap[s2[i]] = 1

    # Remove the element at i-kth place
    # First decrease the frequency
    hmap[s2[i-k]] -= 1

    if hmap[s2[i-k]] == 0:
      del hmap[s2[i-k]]

    # Compare the dicts
    if hmap_s1 == hmap:
      return out.append(i-k+1)

  return out
