class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stack = [0 for i in range(len(temperatures))], []
        stack.append((0, temperatures[0]))
        i = 1
        # (1, 38), (2, 30)
        while stack:
            if i >= len(temperatures):
                break
            while stack and temperatures[i] > stack[-1][1]:
                pos, temp = stack.pop()
                res[pos] = i - pos
            
            stack.append((i, temperatures[i]))
            i += 1
        return res
            
