class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hash:
                return [hash[pair], i]
            hash[nums[i]] = i