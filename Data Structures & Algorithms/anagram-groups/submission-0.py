class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1    
            anagram_map[tuple(key)].append(s)
        
        res = []
        for val in anagram_map.values():
            res.append(val)
        
        return res
        
