class Solution:
    def reverseWords(self, s: str) -> str:
        lst = list(s.split())
        lst = lst[::-1]
        res = " ".join(lst)
        return res
