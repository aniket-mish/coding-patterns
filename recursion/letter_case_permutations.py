
def letter_case_permutations(s: str):
  global_result = []

  # s, i - subproblem
  # slate - partial solution
  def helper(s, i, slate):
    # if `i` exists then there is a blank available
    
    # Base case: leaf worker
    if i == len(s): # empty subproblem
      global_result.append(slate)
      return

    # Recursive case: internal worker
    if s[i].isdigit():
      helper(s, i+1, slate+s[i])
    else: # is a character
      helper(s, i+1, slate+s[i].lower())
      helper(s, i+1, slate+s[i].upper())


  helper(s, 0, "")
  return global_result
    
