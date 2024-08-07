# O(n) time | O(n) space
def diameter_of_binary_tree(root):
      
    if root is None:
        return 0
    
    self.dia = 0
    
    def dfs(node):
        # Base case: leaf node
        if node.left is None and node.right is None:
            return 0

        # Recursive case: internal node
        my_dia = 0
        left_height = 0
        right_height = 0

        if node.left is not None:
            left_height = dfs(node.left)
            my_dia += left_height + 1

        if node.right is not None:
            right_height = dfs(node.right)
            my_dia += right_height + 1
        
        self.dia = max(my_dia, self.dia)
        
        # my own height and return it to my parent
        return max(left_height, right_height) + 1

    
    dfs(root)
    return self.dia
