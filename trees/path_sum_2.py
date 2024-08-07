# Shallow and wide balanced tree

# O(nlogn) as each leaf worker could make a copy of the slate - time
# O(nlogn) again as above - space
def path_sum_2(root, targetSum):        
    result = []

    # Edge case
    if root is None:
        return []

    # Passing node and the target sum to be searched
    def dfs(node, target, slate):
    
        # Base case: leaf node
        if node.left is None and node.right is None:
            # Process the value
            if node.val == target:
                slate.append(node.val)
                result.append(slate[:]) # mutable slate as seen in recursion
                slate.pop()
            return
    
        # Recursive case: internal node
        slate.append(node.val)

        if node.left is not None:
            dfs(node.left, target-node.val, slate)
    
        if node.right is not None:
            dfs(node.right, target-node.val, slate)
        
        slate.pop()

    # Only call with parameters
    dfs(root, targetSum, [])

    return result
