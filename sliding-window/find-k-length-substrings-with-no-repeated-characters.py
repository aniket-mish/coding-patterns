# O(n) time | O(n) space : dictionary can grow to n
def find_k_length_substrings_with_no_repeated_characters(s, k):
  # Edge case: if given k is a higher number than the length of s
  if len(s) < k:
    return 0

  # Initialiazation phase for the leftmost window

  # dictionary to keep track of frequencies of the characters
  hmap = {}

  # Initialize frquencies of the leftmost window
  for i in range(k):
    if s[i] in hmap:
      hmap[s[i]] += 1
    else:
      hmap[s[i]] = 1

  # As dictionary now only has characters with frequency 1, update the variable
  if len(hmap) == k:
    global_count = 1
  else:
    global_count = 0

  # Iterate over next subarrays
  for i in range(k, len(s)):

    # If the ele is in dictionary, increment the frequency
    if s[i] in hmap:
      hmap[s[i]] += 1
    else:
      hmap[s[i]] = 1

    # Decrease the frequency by 1 as it must have been added in the hmap by subordinate and so we don't need a check
    hmap[s[i-k]] -= 1

    # Delete the ele from hmap
    if hmap[s[i-k]] == 0:
      del hmap[s[i-k]]

    if len(hmap) == k:
      global_count += 1

  return global_count
    
