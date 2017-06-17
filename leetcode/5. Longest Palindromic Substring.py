class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def preprocess(s):
            if not s:
                return ['^', '$']
            T = ['^']
            for c in s:
                T += ['#', c]
            T += ['#', '$']
            return T

        T = preprocess(s)
        P = [0] * len(T)
        middle, right = 0, 0
        for i in xrange(1, len(T)-1):
            mirror_i = middle*2 - i
            if right > i:
                P[i] = min(P[mirror_i], right-i)
            else:
                P[i] = 0

            while T[i-1-P[i]] == T[i+1+P[i]]:
                P[i] += 1

            if i+P[i] > right:
                middle, right = i, i+P[i]

        max_i = 0
        for i in xrange(1, len(P)-1):
            if P[i] > P[max_i]:
                max_i = i

        return s[(max_i-1-P[max_i])/2: (max_i-1+P[max_i])/2]
        # start = (max_i - 1 - P[max_i])/2
        # return s[start: start + P[max_i]]


if __name__ == "__main__":
    s = "11111"
    assert Solution().longestPalindrome(s) == "11111"
    s = "babad"
    assert Solution().longestPalindrome(s) == "bab"
    s = "cbbd"
    assert Solution().longestPalindrome(s) == "bb"