class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - 1 + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - 1 + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - 1 + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - 1 + 1
                l -= 1
                r += 1
        return res

z = Solution()
y = z.longestPalindrome(
    s="babad")
print(y)