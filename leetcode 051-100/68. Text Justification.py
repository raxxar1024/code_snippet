"""
Given an array of words and a length L,
format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach;
that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        words_line = []
        tmp_line = []
        tmp_len = 0
        for word in words:
            if len(word) + tmp_len + 1 < maxWidth:
                tmp_line.append(word)
                tmp_len += (len(word) + 1)
            elif len(word) + tmp_len + 1 == maxWidth:
                tmp_line.append(word)
                tmp_len += (len(word) + 1)
            elif len(word) + tmp_len == maxWidth:
                tmp_line.append(word)
                tmp_len += (len(word))
            elif len(word) + tmp_len > maxWidth:
                words_line.append(tmp_line)
                tmp_line = list()
                tmp_line.append(word)
                tmp_len = len(word) + 1
        words_line.append(tmp_line)

        result = []
        for words in words_line:
            words_string = ""
            count = len(words)
            if count == 1:
                words_string = words[0] + " " * (maxWidth - len(words[0]))
            elif count == 2:
                words_string = words[0] + " " * (maxWidth - len(words[0]) - len(words[1])) + words[1]
            else:
                all_len = 0
                for word in words:
                    all_len += len(word)
                all_space_len = maxWidth - all_len
                space_len = all_space_len / (count - 1)
                tmp_count = count
                for i in xrange(count):
                    words_string += words[i]
                    if i == (count - 1):
                        break
                    if all_space_len % (tmp_count - 1) > 0:
                        words_string += " " * (space_len + 1)
                        all_space_len -= (space_len + 1)
                        tmp_count -= 1
                    else:
                        words_string += " " * space_len
            result.append(words_string)

        words_string = ""
        for i in xrange(len(words_line[-1])):
            if i == 0:
                words_string += words_line[-1][i]
            else:
                words_string += " " + words_line[-1][i]
        words_string += " " * (maxWidth - len(words_string))
        result[-1] = words_string

        return result


if __name__ == "__main__":
    assert Solution().fullJustify(["Don't", "go", "around", "saying", "the", "world", "owes", "you", "a", "living;",
                                   "the", "world", "owes", "you", "nothing;", "it", "was", "here", "first."], 30) == [
               "Don't  go  around  saying  the",
               "world  owes  you a living; the",
               "world owes you nothing; it was",
               "here first.                   "
           ]

    assert Solution().fullJustify([""], 0) == [""]
    assert Solution().fullJustify(["What", "must", "be", "shall", "be."], 12) == [
        "What must be",
        "shall be.   "
    ]
    assert Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
