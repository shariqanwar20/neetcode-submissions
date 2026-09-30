class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return "" 

        chars = defaultdict(int)
        for c in t:
            chars[c] += 1

        window = defaultdict(int)
        
        l = 0
        have, need = 0, len(chars)
        minLength, substrStart = math.inf, -1
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in chars and window[s[r]] == chars[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    substrStart = l
                
                window[s[l]] -= 1
                if s[l] in chars and window[s[l]] < chars[s[l]]:
                    have -= 1
                l += 1
        return s[substrStart: substrStart + minLength] if minLength != math.inf else ""

                



        