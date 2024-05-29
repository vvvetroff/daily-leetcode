'''
2812. Find the Safest Path in a Grid

Difficulty: Medium
Topics: Array, Binary Search, Breadth-First Search, Union Find, Matrix

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

- A cell containing a thief if grid[r][c] = 1
- An empty cell if grid[r][c] = 0

You are initially positioned at cell (0, 0). 
In one move, you can move to any adjacent cell in the grid, 
including cells containing thieves.

The safeness factor of a path on the grid is defined as 
the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, 
where |val| denotes the absolute value of val.

Answer from Neetcode, submitted on 5-15-21
'''

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def bounds(r,c):
            return min(r,c) >= 0 and max(r,c) < n

        def bfs():
            q = deque()
            min_dist = {}
            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        q.append([r,c,0])
                        min_dist[(r,c)] = 0
            while q:
                r, c, dist = q.popleft()
                nei = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
                for r2, c2 in nei:
                    if bounds(r2,c2) and (r2, c2) not in min_dist:
                        min_dist[(r2,c2)] = dist + 1
                        q.append([r2,c2,dist+1])
            return min_dist
        
        min_dist = bfs()
        maxHeap = [(-min_dist[(0,0)], 0, 0)]
        visit = set()
        visit.add((0,0))
        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            dist = -dist
            if (r,c) == (n-1, n-1):
                return dist
            nei = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
            for r2, c2 in nei:
                if bounds(r2,c2) and (r2,c2) not in visit:
                    visit.add((r2,c2))
                    dist2 = min(dist, min_dist[(r2,c2)])
                    heapq.heappush(maxHeap, (-dist2,r2,c2))
