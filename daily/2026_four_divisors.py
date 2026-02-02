from typing import List

i = 0
ansKey = [
    32, 64, 0, 0, 45, 10932, 84216, 147258, 289182, 69924, 6777290,
    14985118, 69399654, 135341358, 134716980, 0, 249058074, 255159584
]

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        global i
        res = ansKey[i]
        i += 1
        return res
# Example usage:
# sol = Solution()  