class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = list(zip(position, speed))

        for p,s in sorted(pair)[::-1]:
            reach = (target - p) / s
            if stack and reach > stack[-1]:
                stack.append(reach)

            elif not stack:
                stack.append(reach)

        return len(stack)
