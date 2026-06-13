class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
         frequency[num] = 1 + frequency.get(num, 0)

        count = []
        for num, freq in frequency.items():
            count.append([freq, num])
        count.sort()

        result = []
        while len(result) < k:
            result.append(count.pop()[1])
        return result    
            