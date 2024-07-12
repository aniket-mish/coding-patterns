# O(nlogn) time
def quick_sort(arr):

  def helper(arr, start, end):

    # Base case: subproblem size is 0 or 1 we do nothing
    if start >= end:
      return

    # Recursive case: subproblem size is atleast 2 we cut the array into two halves and give them to subordinate for sorting
    
    # Pick a random interger
    pindex = random.randint(start, end)

    # Move the pivot to the first place in the array
    arr[pindex], arr[start] = arr[start], arr[pindex]

    orange = start
    
    for green in range(start + 1, end + 1):

      if arr[green] < arr[start]:
        orange += 1
        arr[orange], arr[green] = arr[green], arr[orange]

    # Move pivot on the boundary of orange and green regions
    arr[start], arr[orange] = arr[orange], arr[start]

    # Now we have two partitions and pivot is at boundary and now we can delegate the work to our subordinates
    helper(arr, start, orange - 1)
    helper(arr, orange + 1, end)

  helper(arr, 0, len(arr) - 1)
  return arr
    
