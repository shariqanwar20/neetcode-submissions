class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (target - position) / speed -> 3 seconds
        # (4, 2) -> 3
        # (1, 2) -> 4.5
        # (0, 1) -> 10
        # (7, 1) -> 3
        # (10, 4.5, 3, 3)

        # (1, 1, 12, 7, 3)
        
        pairs = [(pos, sp) for pos, sp in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []

        # we only append to the stack if the new car will reach after the already present car in stack
        # otherwise it will have merged with that car
        for pos, sp in pairs:
            time_to_target = (target - pos) / sp
            print(time_to_target)
            if stack and time_to_target <= stack[-1]:
                continue

            stack.append(time_to_target)
        
        return len(stack)

        
