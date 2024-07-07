# O(n) time | O(1) space - hash table stores at max 3 elements
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Variable length sliding window.
        """

        hmap = {}
        left = 0
        global_max = 0

        for i in range(len(fruits)):

            # Work to be done to calculate max number of fruit to be gathered ending at index i

            # If the fruit is same with increase the count else we add it to the hash map
            if fruits[i] in hmap:
                hmap[fruits[i]] += 1
            else:
                hmap[fruits[i]] = 1

            while left <= i and len(hmap) > 2:
                hmap[fruits[left]] -= 1

                if hmap[fruits[left]] == 0:
                    del hmap[fruits[left]]

                left += 1

            global_max = max(global_max, i-left+1)

        return global_max
