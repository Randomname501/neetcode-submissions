class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            sortedS = "".join(sorted(word))
            if sortedS not in seen:
                seen[sortedS] = []
            seen[sortedS].append(word)
        return(list(seen.values()))