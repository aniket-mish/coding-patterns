
# O(n) time | O(1) space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        [Optimization] We can further optimize the solution by having a hash table that stores a character
        and the index it appears in s most recently.
        Then we can directly jump to the index where we have already seen the repeated character instead of going one place.

        left = 0
        hmap = {}
        global_max = 0

        for i in range(len(s)):
          if s[i] in hmap:
            left = max(left, 1+hmap[s[i]])

          global_max = max(global_max, i-left+1)

          hmap[s[i]] = i

        return global_max
        """

        left = 0
        hmap = {}
        global_max = 0

        for i in range(len(s)):
            # Work to be done to find the longest substring ending at index i
            # with no repeating characters

            # Add a new element
            if s[i] in hmap:
                hmap[s[i]] += 1
            else:
                hmap[s[i]] = 1

            while left <= i and hmap[s[i]] > 1:
                
                hmap[s[left]] -= 1

                if hmap[s[left]] == 0:
                    del hmap[s[left]]

                left += 1

            global_max = max(global_max, i-left+1)

        return global_max
