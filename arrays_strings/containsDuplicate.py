""" 
Given an integer array nums, return true if any value appears at least twice in the array,

and return false if every element is distinct.
"""
nums = [1,2,3,14,24,34,341,323,234,23,242,2423423423,23423423423]
class Solution:
    # go through the list starting at the first index
    # check if any number other then the first is the same
    # keep doing this until all index are checked
    def containsDuplicate_1(self, nums: list[int]) -> bool:
      for index_a, a in enumerate(nums): # loop that goes through the index for the first index a
          for index_b, b in enumerate(nums[index_a+1:],start=index_a+1): #loop for the second index b
              if a == b:
                  return True
      return False
            
    # use a hash map to find another number that is the same
    # idea keep track of the number of occurs that the number appears
    def containsDuplicate_2(self, nums: list[int]) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
            if hashmap[num] > 1:
                return True
        return False
    

solution = Solution()
print(solution.containsDuplicate_1(nums))
print(solution.containsDuplicate_2(nums))