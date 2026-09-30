class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digits = list(digits)
        digits_to_letters = {
            '2': ["a", "b", "c"],
            '3': ["d", 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res, permut = [], []
        digits_to_used = defaultdict(set)
        used = set()
        def backtrack(start):

            if len(permut) == len(digits):
                res.append("".join(permut))
                return

            for i in range(start, len(digits)):

                    for j in range(len(digits_to_letters[digits[i]])):
                        # if digits_to_letters[digits[i]][j] not in digits_to_used[digits[i]]:
                           
                            # digits_to_used[digits[i]].add(digits_to_letters[digits[i]][j])
                            permut.append(digits_to_letters[digits[i]][j])
                        
                            backtrack(i + 1)

                            permut.pop()
                            # digits_to_used[digits[i]].remove(digits_to_letters[digits[i]][j])

        backtrack(0)
        return res
