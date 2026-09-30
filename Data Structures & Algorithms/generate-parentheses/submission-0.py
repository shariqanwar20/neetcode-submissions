class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        candidates = []
        for i in range(n):
            candidates.append("(")
            candidates.append(")")

        # generate all possible permutations and add if valid

        res, permut = [], []
        used = {}
        used["("] = n
        used[")"] = n

        def backtrack(start):
            if len(permut) == 2 * n:
                res.append("".join(permut))
                return
            
            for i in range(start, 2*n):
                if used["("] > 0:
                    used["("] -= 1
                    permut.append("(")

                    backtrack(i + 1)

                    permut.pop()
                    used["("] += 1

                if used[")"] > used["("]:
                    used[")"] -= 1
                    permut.append(")")

                    backtrack(i + 1)

                    permut.pop()
                    used[")"] += 1
        
        backtrack(0)
        print(res)
        return res
        


        def isValidParantheses(input_str):

            return True