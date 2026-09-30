class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        arr = []
        res = []

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        
        for count, freq in frequency.items():
            arr.append([freq, count])
        
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res