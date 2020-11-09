'''
1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
'''

class Solution:
    def calculateMove(self, instructions: str, currentAngle: int, currentPosition: list) -> (int, list):
        for c in instructions:
            # Handling 'Go' requests
            if c == 'G':
                if currentAngle == 90:
                    currentPosition[1] += 1
                elif currentAngle == 0:
                    currentPosition[0] += 1
                elif currentAngle == 180:
                    currentPosition[0] -= 1
                elif currentAngle == 270:
                    currentPosition[1] -= 1
                    
            # Handling 'rotations'
            elif c == 'L':
                currentAngle += 90
            elif c == 'R':
                currentAngle -= 90
                
            # Handling invalid parameters
            else:
                print("Invalid instruction set")
                return False
                
            currentAngle = (currentAngle if currentAngle < 360 and currentAngle >= 0 else abs(currentAngle % 360))
            
        return currentAngle, currentPosition
    
    def isRobotBounded(self, instructions: str) -> bool:
   
        # Four cases to check
        # 1) We are at the origin. This is a positive result.
        # 1) We have achieved a full 180 degrees rotation to 270. This should return us to the origin.
        # 2) We have achieved some form of 90 degrees rotation (180 or 0). Check if delta of all 3 possible options equals origin.
        # 3) We are facing north still. Unless we are at the origin (which we already check) this is invalid
        
        moveAngle, movePosition = self.calculateMove(instructions, 90, [0, 0])
        
        if movePosition == [0, 0]:
            return True
        
        if moveAngle == 270:
            return True
        
        elif moveAngle == 0 or moveAngle == 180:
            # Performing the move again three times.
            # This is not great from a complexity standpoint, but it still is O(n) where n = instruction count
            moveAngle, movePosition = self.calculateMove(instructions, moveAngle, movePosition)
            moveAngle, movePosition = self.calculateMove(instructions, moveAngle, movePosition)
            moveAngle, movePosition = self.calculateMove(instructions, moveAngle, movePosition)
            
            
            
            # If this does not return us to the origin, this is not a valid circle
            if movePosition == [0,0]:
                return True
            else:
                return False
            
        else:
            return False
            
            