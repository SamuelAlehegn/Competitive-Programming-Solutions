class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        new_s = []
        for i in range(len(s)//2):
            if '()' in s:
                s = s.replace('()', '')
            elif '{}' in s:
                s = s.replace('{}', '')
            elif '[]' in s:
                s = s.replace('[]', '')
        return s == ""
