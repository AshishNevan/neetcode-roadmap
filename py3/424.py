from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charmap = Counter(s)
        char = sorted(charmap, key=charmap.get, reverse=True)[0]
        l, r = 0, 1
        while r < len(s):
            c = r - l - s[l:r].count(char)
            if c <= k:
                r += 1
            else:
                l += 1
                r += 1
        return r - l


sol = Solution()
print(sol.characterReplacement("ABAB", 2))
print(sol.characterReplacement("AABABBA", 1))
print(sol.characterReplacement("ABBB", 1))
print(sol.characterReplacement("ABAA", 0))
print(sol.characterReplacement("AAAA", 0))
