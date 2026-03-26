class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        highest_y = 0
        total_square_area = 0

        
        for x, y, side in squares:
            total_square_area += side * side
            highest_y = max(highest_y, y + side)

        
        def is_half_area_reached(cut_y):
            area_below = 0

            for x, y, side in squares:
                if y < cut_y:
                    covered_height = min(cut_y - y, side)
                    area_below += side * covered_height

            return area_below >= total_square_area / 2

        low = 0.0
        high = highest_y
        precision = 1e-5

        
        while abs(high - low) > precision:
            mid_y = (low + high) / 2

            if is_half_area_reached(mid_y):
                high = mid_y
            else:
                low = mid_y

        return high
