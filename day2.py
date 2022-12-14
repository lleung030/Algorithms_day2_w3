""" 
Reformat the String
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.
Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:
Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:
Input: s = "ab123"
Output: "1a2b3
"""

def reformat(str_1):
    digits = []
    letters = []
    str_2 = []
    for characters in str_1:
        if characters.isdigit():
            digits.append(characters)
        else:
            letters.append(characters)
    '''letters go first'''
    '''digit go second'''

    current = 'digit'
    if len(digits) > len(letters):
        current = 'digit'
    else:
        current = 'letter'
        
    str_2 = []
    
    for i in range(len(str_1)):
        if current == 'digit':
            digit = digits.pop
            str_2.append(digit)
            current = 'letter'
        else:
            letter = letters.pop
            str_2.append(letter)
            current = 'digit'
    print(str_2)
            
    
    
print(reformat("a0b1c2"))
# print(reformat("leetcode"))
# print(reformat("1229857369"))
# print(reformat("covid2019"))
# print(reformat("ab123"))

