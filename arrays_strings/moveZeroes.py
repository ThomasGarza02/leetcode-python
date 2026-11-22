'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

class Solution:
    # goes through list and using python methods to move 0 to the end 
    # use temp list to keep track
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums==[]:
            return None
        for a in nums: # since it loops it O(n^2)
            if a == 0:
                nums.remove(0)# this takes O(n)time 
                nums.append(0)# this takes O(n)time 
        return nums
    
    
    # other solution avoid using the python methods
    # two pointer technique overwrite elements in place instead of removing elements
    def moveZeroes2(self, nums: list[int]) -> None:
        insert_pos = 0 # tracks the number of numbers 
        #moves all numbers forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        print(nums)
        #use insert_pos to add zeros at end of list
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        return nums





solution = Solution()
nums = [0,1,0,3,12]
print(solution.moveZeroes2(nums))
