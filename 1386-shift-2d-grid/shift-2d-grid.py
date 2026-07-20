class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        # Flatten the grid
        arr = []
        for row in grid:
            for val in row:
                arr.append(val)

        total = rows * cols
        k %= total

        # Rotate to the right by k
        arr = arr[-k:] + arr[:-k]

        # Convert back to 2D grid
        result = [arr[i:i+cols] for i in range(0, total, cols)]

        return result
        
        