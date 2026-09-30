class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res, subset = [], []

        def dfs(start):
            if "".join(subset) == s:
                res.append(subset[::])
                return

            for j in range(start, len(s)): # 1, 3
                choice = s[start:j+1]      # a
                if self.isPalindrome(choice):
                    subset.append(choice)  #[a]
                    dfs(j+1)
                    subset.pop()

        dfs(0)
        return res
    
    
    
    
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True