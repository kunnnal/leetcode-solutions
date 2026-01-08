from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**15

        dp = [NEG_INF] * (m + 1)

        for i in range(1, n + 1):
            prev = NEG_INF
            for j in range(1, m + 1):
                cur = dp[j]
                take = nums1[i-1] * nums2[j-1] + max(0, prev)
                dp[j] = max(take, dp[j], dp[j-1])
                prev = cur

        return dp[m]
