class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return "" 

        chars = defaultdict(int)
        for c in t:
            chars[c] += 1

        window = defaultdict(int)
        
        l = 0
        size = math.inf
        res = ""
        have, need = 0, len(chars)
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in chars and window[s[r]] == chars[s[r]]:
                have += 1

            while l <= r and window[s[l]] > chars[s[l]]:
                window[s[l]] -= 1
                l += 1
            
            if have == need:
                if (r - l + 1) < size:
                    size = r - l + 1
                    res = s[l:(r+1)]
        return res