from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        Finds all pairs of elements with the minimum absolute difference.
        
        Args:
            arr:  list of distinct integers.
            
        Returns:
            A list of pairs in ascending order, where each pair [a, b] satisfies:
            - a, b are from arr
            - a < b
            - b - a equals the minimum absolute difference
        """
        # Sort the array to ensure we can easily find adjacent elements with min difference
        arr.sort()
        
        min_diff = float('inf')
        result = []
        
        # Iterate through the sorted array to find min diff and collect pairs
        for i in range(len(arr) - 1):
            current_diff = arr[i+1] - arr[i]
            
            # If we found a smaller difference, update min_diff and reset result list
            if current_diff < min_diff:
                min_diff = current_diff
                result = [[arr[i], arr[i+1]]]
            # If we found a difference equal to min_diff, add the pair to result
            elif current_diff == min_diff:
                result.append([arr[i], arr[i+1]])
                
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    arr1 = [4, 2, 1, 3]
    print(f"Input: {arr1}")
    print(f"Output: {solution.minimumAbsDifference(arr1)}")
    
    # Example 2
    arr2 = [1, 3, 6, 10, 15]
    print(f"\nInput: {arr2}")
    print(f"Output: {solution.minimumAbsDifference(arr2)}")
    
    # Example 3
    arr3 = [3, 8, -10, 23, 19, -4, -14, 27]
    print(f"\nInput: {arr3}")
    print(f"Output: {solution.minimumAbsDifference(arr3)}")
