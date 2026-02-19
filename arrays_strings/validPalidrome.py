""" 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
"""

s = "A man, a plan, a canal: Panama"
class Solution:
    def isPalindrome(self, s: str) ->bool:
       
        #first remove all characters other then letters/numbers and make lower case
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        #second create new string that is revers of first
        #go through the string and see if there is any differences  
        if len(s) <= 1:
            return True
        return s == s[::-1]

solution = Solution()
print(solution.isPalindrome(s))
