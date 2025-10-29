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
    pass


# Test cases
def run_tests():
    assert count_vowels("Hello World") == 3
    assert count_vowels("Python") == 1
    assert count_vowels("aEiOu") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0
    print("✅ All test cases passed!")

run_tests()
