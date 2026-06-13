class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        pair = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                index = seen.get(complement)
                pair.append(index)
                pair.append(i)
                return pair
            seen[nums[i]] = i
