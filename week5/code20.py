from collections import defaultdict


class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        for s in strs:
            # Sorting the characters produces the same key for all anagrams
            key = tuple(sorted(s))
            groups[key].append(s)

        return list(groups.values())
