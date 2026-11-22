'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''

class Solution:
    # time complexity O(n)
    def plusOne(self, digits: list[int]) -> list[int]:
      # list -> value -> list
      # get value of list 
      value = 0
      power_of = len(digits) - 1 
      for i in digits:
         value = (i * 10**power_of) + value
         power_of -= 1 
      # add one 
      value += 1
      # get result and change list according 
      digits = list(str(value)) #use python type conversion to turn int to list
      for i in range(len(digits)):
         digits[i] = int(digits[i])
      return digits
    # just change the list itself 
    def plusOne2(self, digits: list[int]) -> list[int]:
      last_i = len(digits) - 1

      while last_i >= 0 and digits[last_i] == 9:
          digits[last_i] = 0
          last_i -= 1

      if last_i < 0:
          digits.insert(0, 1)
      else:
          digits[last_i] += 1

      return digits

    
solution = Solution()
digits = [1,2,3]
print(solution.plusOne(digits))
digits = [9]
print(solution.plusOne(digits))

print("plus one 2")
digits = [1,2,3]
print(solution.plusOne2(digits))
digits = [9]
print(solution.plusOne2(digits))
digits = [9,9]
print(solution.plusOne2(digits))
digits = [1,9,9]
print(solution.plusOne2(digits))
digits = [8,9,9,9]
print(solution.plusOne2(digits))
