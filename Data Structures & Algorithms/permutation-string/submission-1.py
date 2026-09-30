class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        chars = [0] * 26
        for c in s1:
            chars[ord(c) - ord('a')] += 1

        n = len(s1)

        chars2 = [0] * 26
        i = 0
        size = 0
        for j in range(len(s2)):
            if size < n:
                chars2[ord(s2[j]) - ord('a')] += 1
                size += 1
            else:
                
                print(chars2)

                if chars2 == chars:
                    return True
                chars2[ord(s2[j]) - ord('a')] += 1
                chars2[ord(s2[i]) - ord('a')] -= 1
                i += 1
        if chars2 == chars:
            return True
        return False
                
