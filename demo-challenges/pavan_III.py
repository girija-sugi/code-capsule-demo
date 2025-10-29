"""
Problem Title: Count Vowels in a String

Problem Description:
Write a function that counts the number of vowels (a, e, i, o, u) in a given string.
The function should be case-insensitive, meaning both uppercase and lowercase vowels
should be counted.

Example:
Input: "Hello World"
Output: 3
Explanation: The vowels are 'e', 'o', 'o'

Input: "Python"
Output: 1
Explanation: The vowel is 'o'

Function Signature:
def count_vowels(s: str) -> int:
    pass

Constraints:
- 0 <= len(s) <= 10^4
- String may contain letters, numbers, spaces, and special characters
"""

# Write your function here
def count_vowels(s: str) -> int:
    vowel_count = 0
    vowels_list = ['a', 'e', 'i', 'o', 'u']

    for letter in s:
        if letter.lower() in vowels_list:
            vowel_count += 1
    
    return vowel_count

# Test cases
def run_tests():
    assert count_vowels("Hello World") == 3
    assert count_vowels("Python") == 1
    assert count_vowels("aEiOu") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0
    print("✅ All test cases passed!")

run_tests()

# Checklist
"""
1. How to count the vowels - X
2. How to identify vowels - X
3. How to convert letters to lowercase - X


Solution Approach:

1. initiate the count variable - X
2. Loop through the string - X
3. Check if the lowercase of current value in vowels list - X
4. if a vowel increase the count, if not move to the next value - X
5. Return cnt - X
"""