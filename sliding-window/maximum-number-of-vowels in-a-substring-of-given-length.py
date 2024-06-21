# O(n) time | O(1) space
def maxVowels(self, s: str, k: int) -> int:

    VOWELS = {"a", "e", "i", "o", "u"}

    # Initialization for the leftmost window
    num_vowels = 0
    for i in range(k):
        if s[i] in VOWELS:
            num_vowels += 1

    global_max = num_vowels

    # Iterate over next subarrays
    for i in range(k, len(s)):

        # If the rightmost ele is a vowel, update the metric by adding it in the window
        if s[i] in VOWELS:
            num_vowels += 1

        # If the leftmost ele is a vowel, update the metric by removing it from the window
        if s[i - k] in VOWELS:
            num_vowels -= 1

        # Update the global answer using the local answer 
        global_max = max(global_max, num_vowels)

    return global_max
