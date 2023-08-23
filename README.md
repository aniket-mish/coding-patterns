# coding-patterns

## Sorting

## Recursion
```

```

## Trees
```
handle an empty tree as a special edge case
initialize an empty result array
create an empty queue and push the root of the tree into it

while the queue is not empty:
  count how many nodes are there in the queue

  repaeat that many times:
    pop the next node from the front of the queue
    append it to the result
    if the node has a left child, push it to the back of the queue
    if the node has a right child, push it to the back of the queue
```
