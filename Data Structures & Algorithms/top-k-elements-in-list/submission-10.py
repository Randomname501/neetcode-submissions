class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        count = []
        res = []

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        for num, freq in frequency.items():
             count.append([freq, num])
        count.sort()

        while len(res) < k:
            res.append(count.pop()[1])

        return res