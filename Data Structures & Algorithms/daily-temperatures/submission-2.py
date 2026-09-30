class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stack = [0 for _ in range(len(temperatures))], [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                _, index = stack.pop()
                res[index] = (i - index)
            stack.append((temperatures[i], i))

        return res

        # (40, 5)

        

            
