from queue import Queue

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ''' Number of islands problem. We will solve through iterative BFS using queue'''
        ''' We will also track visited nodes using a set where the key is the x-y as a tuple. '''
        visit = set()
        
        ''' While we haven't reached the end or the node is visted, explore the node '''
        islandCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) in visit:
                    continue
                elif grid[r][c] == '0':
                    continue
                    
                else:
                    self.explore(r, c, visit, grid)
                    islandCount += 1
                    
        return islandCount
                    
    def explore(self, r: int, c: int, visit: set, grid: List[List[str]]) -> None:
        frontier = Queue()
        frontier.put((r,c))
        visit.add((r,c))
        
        while not frontier.empty():
            r, c = frontier.get()
            print(r,c)
            ''' Attempting to add north, south, east, west'''
            if self.isValidPosition(r + 1, c, grid, visit):
                visit.add((r + 1, c))
                frontier.put((r + 1, c))
                
            if self.isValidPosition(r - 1, c, grid, visit):
                visit.add((r - 1, c))
                frontier.put((r - 1, c))
                
            if self.isValidPosition(r, c + 1, grid, visit):
                visit.add((r, c + 1))
                frontier.put((r, c + 1))
                
            if self.isValidPosition(r, c - 1, grid, visit):
                visit.add((r, c - 1))
                frontier.put((r, c - 1))
        
    def isValidPosition(self, r: int, c: int, grid: List[List[str]], visit) -> bool:
        if (r,c) in visit:
            return False
        if r < 0 or c < 0:
            return False
        if r >= len(grid) or c >= len(grid[0]):
            return False
        if grid[r][c] == "0":
            return False
        return True