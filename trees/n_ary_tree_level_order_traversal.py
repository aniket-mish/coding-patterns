# O(n) time | O(n) space
def n_ary_tree_level_order_traversal(root):

  if root is None:
    return []

  q = deque()
  q.append(root)
  result = []
  
  while len(q) != 0:
      temp = []
      numnodes = len(q)
    
      for _ in range(numnodes):
          node = q.popleft()
          temp.append(node.val)
        
          for child in node.children:
              q.append(child)
            
      result.append(temp)

  return result
    
