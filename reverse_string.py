class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, int(len(s) / 2)):
            to = i
            from_ = len(s) - i - 1
            if (from_ - to >= 1):
                s[from_], s[to] = s[to], s[from_]
