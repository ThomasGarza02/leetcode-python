""" 
Given a string s consisting of words and spaces, return the length of the last word in the string.
"""

s = "Hello World"
class Solution:
    # start at the end of the string of words
    # if its a space move to the left until there is a letter
    # when there is letter keep going until there is a space 
    # keep track of how many time you moved left after the first letter
    def lengthOfLastWord(self, s: str) ->int:
        count = 0
        if len(s) == 0:
            return 0
        for letter in s[::-1]:
            # when its a space
            if letter == " ":
                #if last char was a space ignore and keep looking for letter
                #when hitting a space that separates last word from others
                if count !=0:
                    return count
            # when letter
            else:
                count +=1
        return count

solution = Solution()
print(solution.lengthOfLastWord(s))
