class Solution:
    def isValid(self, s: str) -> bool:
        hsh = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []

        for ch in s:
            if ch in hsh:
                if not stack or stack.pop() != hsh[ch]:
                    return False
            else:
                stack.append(ch)
        
        return not stack

        