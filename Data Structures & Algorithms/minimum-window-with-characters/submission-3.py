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
        """
            chars = { X: 1, Y: 1, Z: 1}
            window = { Z: 1, Y: 1, X: 1, A: 1 }
        
        """

        def isSame(s_window, t_window, s, t):
            for c in t:
                if t_window[c] > s_window[c]:
                    return False
            return True

        for r in range(len(s)):
            window[s[r]] += 1

            while l <= r and window[s[l]] > chars[s[l]]:
                window[s[l]] -= 1
                l += 1
            
            if isSame(window, chars, s, t):
                if (r - l + 1) < size:
                    size = r - l + 1
                    res = s[l:(r+1)]
        return res