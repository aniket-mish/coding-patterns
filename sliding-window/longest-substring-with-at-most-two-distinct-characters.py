# O(n) time | O(1) space
def longest_substring_with_at_most_two_distinct_characters(s: str):
  
  left = 0
  hmap = {}
  global_max = 0

  for i in range(len(s)):
    # Max length substring ending at index i
    # and containing at most 2 distinct characters

    if s[i] in hmap:
      hmap[s[i]] += 1
    else:
      hmap[s[i]] = 1

    while left <= i and len(hmap) > 2:
      hmap[s[left]] -= 1

      if hmap[s[left]] == 0:
        del hmap[s[left]]

      left += 1

    global_max = max(global_max, i-left+1)

  return global_max
