class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def helper(stk):
            a, op, b = stk
            if op == "&":
                if a[0] ^ b[0]:
                    return (0, 1)
                elif a[0]:
                    return (1, min(a[1], b[1]))
                else:
                    return (0, 1 + min(a[1], b[1]))
            else:
                if a[0] ^ b[0]:
                    return (1, 1)
                elif a[0]:
                    return (1, 1 + min(a[1], b[1]))
                else:
                    return (0, min(a[1], b[1])) 
        stack = [[]]
        for ch in expression:
            if ch in "01":
                stack[-1].append((int(ch), 1))
            elif ch in "&|":
                stack[-1].append(ch)
            elif ch == "(":
                stack.append([])
            elif ch == ")":
                tmp = stack.pop()
                stack[-1].append(tmp[-1])
            if len(stack[-1]) == 3:
                a = helper(stack[-1])
                stack[-1] = [a]
        return stack[-1][-1][-1]
