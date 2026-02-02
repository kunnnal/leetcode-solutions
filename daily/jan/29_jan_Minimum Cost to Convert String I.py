    from collections import defaultdict
    from heapq import heappush, heappop
    from math import inf
    from typing import List

    class Solution:
        def minimumCostFrom(self, sourceChar):
            bests = {}
            seenCost = defaultdict(lambda: inf)
            seenCost[sourceChar] = 0
            frontier = [(0, sourceChar)]
            while frontier:
                reachCost, current = heappop(frontier)
                if current in bests:
                    continue
                bests[current] = reachCost
                for d, edgeCost in self.edges[current].items():
                    totalCost = reachCost + edgeCost
                    if totalCost < seenCost[d]:
                        heappush(frontier, (totalCost, d))
                        seenCost[d] = totalCost
            return bests
        
        def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
            self.edges = defaultdict(dict)
            for i in range(len(original)):
                s = original[i]
                d = changed[i]
                c = cost[i]
                if d not in self.edges[s] or c < self.edges[s][d]:
                    self.edges[s][d] = c

            bests = {}
            totalCost = 0
            for s, t in zip(source, target):
                if s != t:
                    if s not in bests:
                        bests[s] = self.minimumCostFrom(s)
                    if t in bests[s]:
                        totalCost += bests[s][t]
                    else:
                        return -1
            return totalCost
