class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedKey = "".join(sorted(s))
            res[sortedKey].append(s)
        return list((res.values()))
        