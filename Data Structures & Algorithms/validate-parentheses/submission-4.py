class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_map = {
            '}': '{',
            ']': '[', 
            ')': '('
        }

        for c in s:
            if c not in parenthesis_map:
                stack.append(c)
            
            else:
                if len(stack) > 0 and parenthesis_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0