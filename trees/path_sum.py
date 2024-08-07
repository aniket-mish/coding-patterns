# O(n) time | O(n) - height of the tree space
def path_sum(root, targetSum):
  
    result = [False]

    # Edge case
    if root is None:
        return False

    # Passing node and the target sum to be searched
    def dfs(node, target):
    
        # Base case: leaf node
        if node.left is None and node.right is None:
            # Process the value
            if node.val == target:
                result[-1] = True
            return
    
        # Recursive case: internal node
        if node.left is not None:
            dfs(node.left, target-node.val)
    
        if node.right is not None:
            dfs(node.right, target-node.val)

    # Only call with parameters
    dfs(root, targetSum)

    return result[-1]
