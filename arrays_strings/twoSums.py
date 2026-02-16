""" 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
nums = [3,2,4]
target = 6
class Solution:
    # first idea start at the first on the left of the list 
    # and add it with every other index 
    # if, it fails find the target by the end move 
    # the first index to the right of the list
    def twoSum_1(self, nums: list[int], target: int) -> list[int]:  
      for index_a, a in enumerate(nums): # loop that goes through the index for the first index a
          for index_b, b in enumerate(nums[index_a+1:],start=index_a+1): #loop for the second index b
              if a + b == target:
                  return[index_a,index_b]
      return[]
    # second solution using hashmap
    # load a hash map with all numbers in the list with indices
    # next look go through list num and find the complement 
    # complement = target - number at current index
    # if complement is in the hash map return current index and complement index
    def twoSum_2(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)): # create hashmap
            hashmap[nums[i]] = i
        for i in range(len(nums)): #looking for complement
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i: #checks if not the same index
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []
solution = Solution()
print(solution.twoSum_1(nums,target))
print(solution.twoSum_2(nums,target))
