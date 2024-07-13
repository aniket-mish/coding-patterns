def two_sum(arr, target):
  """
  Transform-and-conquer where we're using a data structure
  We're doing representation change as we wanted to do efficient search and hash table gives us search in O(1)
  We think in decrease-and-conquer way and write code in iterative fashion
  You can also use any approach from bottom up or top down
  Here we are asking subordinates to give us the answer first so its botton up
  This take O(n) time and O(n) space
  """
  hmap = {}

  for i in range(len(arr)):

    if target - arr[i] in hmap:
      return [i, hmap[target - arr[i]]]
    else:
      hmap[arr[i]] = i
