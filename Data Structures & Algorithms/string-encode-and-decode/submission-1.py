class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love3#you
        res = []
        i = 0

        while i < len(s):
            size = ""
            while s[i] != "#":
                size += s[i]
                i += 1
            i += 1
            
            count = int(size)
            res.append(s[i:i+count])
            i += count
        return res
