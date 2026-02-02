class Solution:
    def get_all_distances(self, fences, total_length):
        # Add the two borders: start (1) and end (total_length)
        all_points = [1] + fences + [total_length]
        all_points.sort()

        distances = set()

        # Find distance between every pair of points
        for i in range(len(all_points)):
            for j in range(i + 1, len(all_points)):
                distance = all_points[j] - all_points[i]
                distances.add(distance)

        return distances

    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        # All possible vertical lengths from horizontal fences
        horizontal_lengths = self.get_all_distances(hFences, m)

        # All possible horizontal lengths from vertical fences
        vertical_lengths = self.get_all_distances(vFences, n)

        # Common lengths that can form a square
        possible_square_edges = horizontal_lengths & vertical_lengths

        if not possible_square_edges:
            return -1

        max_edge = max(possible_square_edges)

        return (max_edge * max_edge) % MOD
