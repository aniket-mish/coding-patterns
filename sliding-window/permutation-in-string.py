# O(m + n) time | O(1) space

def permutation_in_string(s1, s2):

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
    return True

  # Iterate over next subarrays
  for i in range(k, len(s2)):

    # Remove the element at i-kth place
    # First decrease the frequency
    hmap[s2[i-k]] -= 1

    if hmap[s2[i-k]] == 0:
      del hmap[s2[i-k]]

    # Add the element at ith place
    if s2[i] in hmap:
      hmap[s2[i]] += 1
    else:
      hmap[s2[i]] = 1

    # Compare the dicts
    if hmap_s1 == hmap:
      return True

  return False
