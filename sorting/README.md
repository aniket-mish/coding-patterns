# Sorting

1. Pre-sorting + binary search/linear scan/two-pointer pass or hash tables (space vs time tradeoff)
2. Extension of merge phase in merge sort - Union or intersection of two arrays
3. Extension of quicksort - quick select and 3-way partitioning
4. Extension of heapsort


> [!TIP]
> to get the mid of a python list and to avoid overflow use
> `mid = start + (end - start) / 2`


## Divide-and-conquer

work to be done upfront e.g. quick sort

work to be done at the end e.g. merge sort

## Transform-and-conquer

_Pre-sorting_

- Searching
- Closest pair
- Check for duplicates
- Frequency distribution
- Select k-th largest/smallest/median

_Common patterns_

- Pre-sorting and binary search
- Pre-sorting and one pass
- Pre-sorting and two-pointer pass

## Two-pointer pass

- Should have sorted lists
- Code is similar to merge sort's merge phase [merge_sort]()
- Whichever element is smaller, that pointer is incremented

*This is a very important coding pattern similar to merge sort's merge phase and pointer increments are just tweeks*

```python
# initialization
i = 0
j = 0
res = []

# while loop
for i < len(nums1) and j < len(nums2):

  # if both are same
  if nums1[i] == nums2[j]:
    res.append(nums1[i])
    i += 1
    j += 1

  # if one of them is smaller
  elif nums1[i] < nums2[j]:
    i += 1

  else:
    j += 1

# potentially a gather phase

# return result
return res
```

## Decrease-and-conquer

1. Binary search

a type of decrease-and-conquer but instead of decreasing the size of the list by 1, we're decreasing it by a factor of 2 (n --> n/2)

2. Randomized quick select [always use randomized form of quick sort]

we decrease the size of list by a variable number and end up with O(n) time complexity

> [!NOTE]
> quick select is best when entire data is given

[problem] k-th largest element

*using quick sort*

```python
def helper(array, start, end):

  # base case: leaf node
  # subproblem of size 0 or 1
  if start >= end: 
    return

  # recursive case: intermediate node

  # LOMUTO'S PARTITIONING
  pivot_index = a random number in range start...end
  swap array[pivot_index], array[start]

  orange_ptr = start

  for green_ptr in start + 1 to end:
    if array[green_ptr] <= array[pivot_index]:
      orange_ptr ++
      swap array[green_ptr], array[orange_ptr]

  swap array[start], array[orange_ptr]

  helper(nums, start, orange_ptr - 1)
  helper(nums, orange_ptr + 1, end)

def quick_sort(nums):
  helper(nums, 0, len(nums) - 1)
```

*using quick select*

```python
def helper(array, start, end, index):

  # base case: leaf node
  if start == end:      # runs into error on leetcode: should be start >= end
    return

  # recursive case: intermediate node

  call LOMUTO'S PARTITIONING code

  if orange_ptr == index:
    return

  elif index < orange_ptr:
    helper(array, start, orange_ptr - 1, index)

  else:
    helper(array, orange_ptr + 1, end, index)


def quick_select(nums, k):
  helper(nums, 0, len(nums) - 1, len(nums) - k)
  return nums[len(nums) - k]
```

## Extensions of heap operation

[problem] k-th largest element in a stream

> [!NOTE]
> In streaming, quick select is not the best solution
> If k is constant, a single heap would do
> If k is function of n like the median, we need a maxheap and minheap

space - O(k)
time - O(log k)

```python

arr = initialize an array
minheap = heapq.heapify(arr) # build a minheap on arr

for each number in the stream:
  heapq.heappush(minheap, number) # insert the number in the minheap
  heapq.heappop(minheap) # extract mininum number
  return minheap[0] # root element kth element
```

similarly, to find the kth smallest element, use maxheap

[problem] median in a stream

space - O(n)
time - O(log n)

```python
initialize minheap and maxheap to empty collections
median = 0.0

for each number in the stream:
  if number > median:
    insert the number in the minheap

    if (size of minheap - size of maxheap) == 2:
      # rebalance
      extract root of the minheap and insert it into the maxheap

  else:
    insert the number in the maxheap

    if (size of maxheap - size of minheap) == 2:
      # rebalance
      extract root of the maxheap and insert it into the minheap
  

  # median computation

  if size of minheap == size of maxheap:
    median = average of the two roots

  elif size of minheap > size of maxheap:
    median = root of the minheap

  elif size of maxheap > size of minheap:
    median = root of the maxheap
```
