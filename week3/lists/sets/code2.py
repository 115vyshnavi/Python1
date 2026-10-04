from collections import Counter

class Solution:
    def getDistinctDifference(self, arr: list[int]) -> list[int]:
        # 1. Fill up the right side dictionary with everyone's counts
        right_freq = Counter(arr)

        # 2. Start with an empty left side set
        left_set = set()
        ans = []

        # 3. Walk through the array step-by-step
        for x in arr:
            # The current element 'x' is no longer on the right side
            right_freq[x] -= 1
            if right_freq[x] == 0:
                del right_freq[x]  # Remove it entirely if there are 0 left

            # Count uniques on left and right
            left_distinct = len(left_set)
            right_distinct = len(right_freq)

            # Save the difference
            ans.append(left_distinct - right_distinct)

            # Now 'x' moves to the left side for the next numbers in line
            left_set.add(x)

        return ans
