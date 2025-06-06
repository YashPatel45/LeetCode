class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}
        for i in strs:
            sortedStr = tuple(sorted(i))
            if sortedStr not in result:
                result[sortedStr] = [i]
            else:
                result[sortedStr].append(i)
        
        print(result)
        return list(result.values())

