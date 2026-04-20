# Problem: 567. Permutation in String
# Link: https://leetcode.com/problems/permutation-in-string/description/
# Difficulty: Medium
# Pattern: Fixed Size Sliding Window
# Trick: Frequency Matching

# Intuition:
# we don’t actually try all permutations, that would be too slow
# we just check if any part of s2 looks like s1 in terms of characters
# so we fix a window of size len(s1) and slide it over s2
# for every window we check if both have same characters with same count
# if yes → that window is a permutation → return True
# while moving forward we just add one new char and remove one old char
# so we don’t rebuild everything again and again

# Approach:
# make count array for s1
# make count array for first window of s2
# then start sliding window
# every step:
# add new char
# remove old char
# compare both arrays
# if match found → return True

# Time Complexity:
# O(n) because we go through s2 once and compare small arrays (size 26)

# Space Complexity:
# O(1) because arrays are always size 26, no extra space grows

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1_count=[0]*26
        s2_count=[0]*26

        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]+=1
            s2_count[ord(s2[i])-ord('a')]+=1

        for i in range(len(s1),len(s2)):
            s2_count[ord(s2[i])-ord('a')]+=1
            s2_count[ord(s2[i-len(s1)])-ord('a')] -=1

            if s1_count==s2_count:
                return True
        
        return False

sol=Solution()
print(sol.checkInclusion("ab","eidbaooo"))