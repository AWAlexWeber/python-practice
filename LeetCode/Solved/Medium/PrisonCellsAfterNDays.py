'''
957. Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 

Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
'''

from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # We need to continue to calculate this until we've reached a steady-state
        # Then we calculate the number of iterations to hit N
        # We multiple the steady state cycle up to N, and then add the remainder, selecting that as our output
        depth = 0
        stateMap = {}
        depthMap = {}
        
        while str(cells) not in stateMap:
            stateMap[str(cells)] = depth
            depthMap[depth] = cells
            cells = self.processPrison(cells)
            depth += 1
            
        # We've completed our steady-state
        cycleSize = depth - stateMap[str(cells)]
        
        if cycleSize > N:
            return depthMap[N]
        
        else:
            # We must calculate the cycle period
            N -= stateMap[str(cells)]
            #print(stateMap)
            return depthMap[stateMap[str(cells)] + N % cycleSize]
        
    def processPrison(self, cells: List[int]):
        # Performs a single process
        newCells = list()
        for i, n in enumerate(cells):
            if i == 0 or i == len(cells) - 1:
                newCells.append(0)
                
            else:
                if cells[i - 1] == cells[i + 1]:
                    newCells.append(1)
                else:
                    newCells.append(0)
                    
        return newCells