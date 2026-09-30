class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}
        def dfs(s):
            if s in memo: return memo[s]

            if not s: return 1

            sub = ""
            res = 0
            for i in range(len(s)):
                sub += s[i]

                if not sub.startswith("0") and int(sub) in range(1, 27):
                    res = res + dfs(s[i+1:])

            memo[s] = res
            return res
        return dfs(s)



    def ascii_to_char(self, val):
        return chr((val - 1) + ord('A'))