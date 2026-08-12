class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        lst = sorted(set(nums))
        current = 1
        longest = 1

        for i in range(1, len(lst)):
            if lst[i] == lst[i-1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        return max(longest, current)