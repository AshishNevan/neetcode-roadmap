from collections import Counter


class Solution:
    def maxLength(self, arr: list[str]) -> int:
        charset = set()

        def overlap(charset, s):
            c = Counter(charset) + Counter(s)
            return max(c.values()) > 1

        def backtrack(i):
            if i == len(arr[i]):
                return len(charset)
            if not overlap(charset, arr[i]):
                for c in arr[i]:
                    charset.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charset.remove(c)
                return max(backtrack(i + 1), res)

        return backtrack(0)


sol = Solution()
print(sol.maxLength(["un", "iq", "ue"]))
