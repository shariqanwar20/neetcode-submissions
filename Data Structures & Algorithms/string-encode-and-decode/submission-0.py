class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, ""

        while i < len(s):
            j = ""
            while s[i] != "#":
                j += s[i]
                i += 1
            i += 1
            res.append(s[i: i + int(j)])

            i += int(j)
        return res

