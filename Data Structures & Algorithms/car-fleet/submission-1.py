class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = list(zip(position, speed))
        s_pair = sorted(pair, key= lambda pair: pair[0])

        for p,s in s_pair[::-1]:
            reach = (target - p) / s
            if stack and reach > stack[-1]:
                stack.append(reach)

            elif not stack:
                stack.append(reach)

        return len(stack)
