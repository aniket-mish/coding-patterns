# time - leaf workers O(n!.n) + internal workers O(n!.n)

# space - input O(n) + aux space O(n) + output O(n!.n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        global_result = []

        def helper(s, i, slate):
        
            # Base case: leaf worker
            if i == len(s):
                global_result.append(slate[:]) # slicing creates a copy/clone of the slate
                return
        
            # Recursive case: intermediate worker
            for pick in range(i, len(nums)):
                # picking s[pick] for the leftmost blank

                # swap s[pick] and s[i]
                s[pick], s[i] = s[i], s[pick]

                slate.append(s[i])
                helper(s, i+1, slate)
                slate.pop()

                # swap them back to their original place
                s[pick], s[i] = s[i], s[pick]

        helper(nums, 0, [])
        return global_result
