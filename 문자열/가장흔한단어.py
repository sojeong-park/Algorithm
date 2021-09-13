# https://leetcode.com/problems/most-common-word/

import collections
from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

s = Solution()
print(s.mostCommonWord("a, a, a, a, b,b,b,c, c", banned=["a"]))
print(s.mostCommonWord("a.", banned = []))
print(s.mostCommonWord("Bob. hIt, baLl", banned = ["bob", "hit"]))
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was tt.", banned = ["hit"]))
