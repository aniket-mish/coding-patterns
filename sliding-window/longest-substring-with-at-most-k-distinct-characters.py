# O(n) time | O(k) space - can be at the max k
def longest_substring_with_at_most_k_distinct_characters(s: str, k: int):
  
  left = 0
  hmap = {}
  global_max = 0

  for i in range(len(s)):
    # Max length substring ending at index i
    # and containing at most k distinct characters

    if s[i] in hmap:
      hmap[s[i]] += 1
    else:
      hmap[s[i]] = 1

    while left <= i and len(hmap) > k:
      hmap[s[left]] -= 1

      if hmap[s[left]] == 0:
        del hmap[s[left]]

      left += 1

    global_max = max(global_max, i-left+1)

  return global_max
