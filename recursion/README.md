# Recursion

Order matters - permutation

Order does not matter - combination

## General template for permutation


![image](https://github.com/user-attachments/assets/77810959-4e95-4a80-88e9-17c552df4c69)


```python
def main problem(problem_of_size_n):
    Initialize the global_result = []

    def helper(subproblem_definition, partial_solution):
    
        # Base case: lead worker
        if subproblem size == 0:
            # Treat the partial solution as a complete permutation/combination
            # print/process/add it to the global result/whatever the problem wants you to do
            add it to the global_result
            return
    
        # Recursive case: intermediate worker
        # Atleast one blank to be filled
        for each choice from c1, c2, ..., ck for filling in the leftmost blank:
            # Make that choice
            # Write that choice into that blank

            # Delegate to the subordinate
            helper(slightly_smaller_subproblem_definition, slightly_larger_partial_solution)

    helper(full_problem_definition_of_size_n, blank_slate)
    return global_result
  
```

> [!NOTE]
> a top-down recursion - quick sort - you do some work and then delegate and go away
> 
> a bottom-up recursion - merge sort - once those are sorted by your subordinates you need to combine those subarrays


- For immutable slates, time complexity is dominated by the penultimate layer (not the leaf workers)

- For mutable slates, time complexity is dominated by the leaf workers


## Why mutable slate solution? We want to decrease auxilary space complexity

> Always use mutable solution

```python

# time - leaf worker O(2^n.n) + internal worker O(2^n.1)

# space - input O(n) + aux space O(n) + output O(2^n.n)

def letter_case_permutation(s: str):
    global_result = []

    def helper(s, i, slate):
    
        # Base case: leaf worker
        if i == len(s):
            global_result.append("".join(slate)) # string version of slate contents (just copying contents to global result)
            return
    
        # Recursive case: intermediate worker
        if s[i].isdigit():

            slate.append(s[i])
            helper(s, i+1, slate)
            slate.pop()

        else:

            slate.append(s[i].lower())
            helper(s, i+1, slate)
            slate.pop()

            slate.append(s[i].upper())
            helper(s, i+1, slate)
            slate.pop()

    helper(s, 0, "")
    return global_result
```

## General template for combination


<img width="960" alt="Screenshot 2024-08-01 at 3 54 40 PM" src="https://github.com/user-attachments/assets/8cff8159-0239-4a2c-a3e3-11d6733cb186">


```python

# space - input O(n) + aux space O(n) (height of the call stack + max size of the slate) + output O(2^n. n)

# time - leaf workers O(2^n.n) + internal workers O(2^n.1)

def subsets(nums):
    global_result = []

    def helper(s, i, slate):
    
        # Base case: leaf worker
        if i == len(s):
            global_result.append(slate[:]) # slicing creates a copy/clone of the slate
            return
    
        # Recursive case: intermediate worker
        # Exclude case

        helper(s, i+1, slate)

        # Include case
        slate.append(s[i])
        helper(s, i+1, slate)
        slate.pop()

    helper(nums, 0, [])
    return global_result
```

## Backtracking


<img width="822" alt="Screenshot 2024-08-02 at 4 48 44 PM" src="https://github.com/user-attachments/assets/e1d23864-2863-4f67-a43a-f72e774e30b6">



