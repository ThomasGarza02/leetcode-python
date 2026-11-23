'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def prefixList(lst,word):
           for index,char in enumerate(word):
                    if lst == []:
                      lst.append(char)
                    else:
                       lst.append(lst[index-1]+char)        
        lst = []
        #creates list of prefixes
        prefixList(lst,strs[0])
        #compares prefixes and removes ones that dont occur in next word
        for word in strs[1:]:
           next_lst = []
           prefixList(next_lst,word)
           for i,prefix in enumerate(lst[:]):
              if i >= len(next_lst) or prefix != next_lst[i]:
                  lst.remove(prefix)
        if lst == []:
           return ""
        return lst[-1]
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        prefix = ""
        matching = True
        ind = 0
        while matching == True:
            if ind >= len(strs[0]):
                return prefix
            letter = strs[0][ind]
            for i in strs:
                if ind >= len(i):
                    return prefix
                if i[ind] != letter:
                    matching = False
            if matching == True:
                prefix += strs[0][ind]
                ind += 1
        return prefix
            


solution = Solution()
strs = ["flower","flow","flight"]
print(solution.longestCommonPrefix(strs))
strs = ["flower","fkow"]
print(solution.longestCommonPrefix(strs))