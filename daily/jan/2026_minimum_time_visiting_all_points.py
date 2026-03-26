class Solution:
    def minTimeToVisitAllPoints(self, points):
        total_time = 0

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            dx = abs(x1 - x2)
            dy = abs(y1 - y2)

            total_time += max(dx, dy)

        return total_time
