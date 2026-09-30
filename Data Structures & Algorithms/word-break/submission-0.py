class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # one variable: i 
        # recurrence: (0..i) + [i:]
        # base case: i out of bounds.
        # if s empty: return True
        # if s[:i] in wordDict: dfs(s[i:])
        # else: you add one more char
        
        memo = {}
        wordSet = set(wordDict)
        # s = neetcode   code  ""
        # sub = 
        #
        #
        #
        def dfs(s):
            print(s)
            if s in memo: return memo[s]

            if not s: return True

            sub = ""
            res = False
            for i in range(len(s)):
                sub += s[i]
                if sub in wordSet:
                    res = res or dfs(s[i + 1:])
            memo[s] = res
            return res

        return dfs(s)