# O(nlogn) time | O(n) space
def merge_sort(arr):

  def helper(arr, start, end):
    # Base case: subproblem size is 0 or 1 which means nothing to do
    if start >= end:
      return

    # Recursive case: subproblem size is atleast 2 so cut the array into two halves and delegate the work to two subordinates hired under you
    mid = (start + end) / 2

    # Sort left half
    helper(arr, start, mid)

    # Sort right half
    helper(arr, mid + 1, end)

    # Now merge the two sorted halves using two pointer pass
    i = start
    j = mid + 1
    aux = []

    while i <= mid and j <= end:

      if arr[i] > arr[j]:
        aux.append(arr[j])
        j = j + 1
      elif arr[i] <= arr[j]: # "=" is for stablitity
        aux.append(arr[i])
        i = i + 1

    # Gather up remaining elements from the arrays
    while i <= mid:
      aux.append(arr[i])
      i = i + 1

    while j <= end:
      aux.append(arr[j])
      j = j + 1

    # Copy the elements back to the original array
    arr[start:end+1] = aux

  # Call the helper function with original array
  helper(arr, 0, len(arr)-1)
  return arr
    
