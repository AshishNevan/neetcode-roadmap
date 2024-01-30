class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        front, back = 0, 0
        longest_substr = s[front]
        front += 1
        longest = 1
        while front < len(s):
            if s[front] not in longest_substr:
                longest_substr += s[front]
                front += 1
                longest = max(longest, len(longest_substr))
            else:
                while back < front and s[front] in longest_substr:
                    back += 1
                    longest_substr = longest_substr[1:]
        return longest


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring(" "))
