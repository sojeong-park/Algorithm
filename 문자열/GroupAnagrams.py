# https://leetcode.com/problems/group-anagrams/

from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])