"""
Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers
have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5],
which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each,
his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if citations[i] > i:
                h = i + 1
            else:
                break
        return h


if __name__ == "__main__":
    assert Solution().hIndex([0]) == 0
    assert Solution().hIndex([100]) == 1
    assert Solution().hIndex([1]) == 1
    assert Solution().hIndex([3, 0, 6, 1, 5]) == 3
