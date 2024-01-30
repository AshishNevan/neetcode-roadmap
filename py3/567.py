from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = Counter(s1)
        print(s1)
        for i in range(n - 1, len(s2)):
            t = Counter(s2[i - n : i])
            print(t)
            if t == s1:
                return True
        return False


sol = Solution()
# print(sol.checkInclusion("ab", "eidbaooo"))
print(sol.checkInclusion("adc", "dcda"))
