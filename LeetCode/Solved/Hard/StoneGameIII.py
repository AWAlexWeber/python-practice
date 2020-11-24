'''
1406. Stone Game III

Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.

 

Example 1:

Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
Example 2:

Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.
Example 3:

Input: values = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
Example 4:

Input: values = [1,2,3,-1,-2,-3,7]
Output: "Alice"
Example 5:

Input: values = [-1,-2,-3]
Output: "Tie"
'''

from typing import List

class StoneGameNode:
    def __init__(self, stones, turn, depth, scores, parent, prevMove: dict, turnCount=1):
        
        self.stones = stones
        self.turn = turn
        self.depth = depth
        
        # Tuple indicating the scores. 0 = Alice, 1 = Bob
        self.scores = scores
        
        self.moves = list()
        self.parent = parent
        
        self.winner = None
        
        # Going deeper.
        nextTurn = "Alice" if self.turn == "Bob" else "Bob"
        
        # Calculating the new score.
        newScore = 0
        
        # Trying all future possible moves
        maxMoves = min(depth + 3, len(stones))
        for i in range(depth, maxMoves):
            newScore += stones[i]
            
            newScores = None
            
            if turn == 'Alice':
                newScores = (self.scores[0] + newScore, self.scores[1])
            else:
                newScores = (self.scores[0], self.scores[1] + newScore)
                
            # Calculating score difference
            scoreDiff = (self.scores[0] - self.scores[1])
            h = str(self.turn) + str(self.depth) + str(scoreDiff)
            if h in prevMove:
                gameNode = prevMove[str(self.turn) + str(self.depth) + str(scoreDiff)]
                #print("Using prev")
            else:
                # Creating the new game node
                gameNode = StoneGameNode(stones, nextTurn, i + 1, newScores, self, prevMove, turnCount = turnCount + 1)

                # Appending it to our prev move dictionary
                prevMove[str(gameNode)] = gameNode
            
            # Adding it to the list
            self.moves.append(gameNode)
            
    def winningMove(self):
        
        if self.winner:
            return self.winner
        
        # Okay now calculating our winning move
        if len(self.moves) <= 0:
            # Okay we just return who wins here
            if self.scores[0] > self.scores[1]:
                self.winner = 'Alice'
                
            elif self.scores[1] > self.scores[0]:
                self.winner = 'Bob'
                
            else:
                self.winner = 'Tie'
                
            return self.winner
        
        else:
            # Okay now we will see who wins here.
            # Alice will select Alice, otherwise Tie, otherwise Bob
            
            winningMovesInChildren = list()
            for m in self.moves:
                m.winningMove()
                winningMovesInChildren.append(m.winner)
                
            if self.turn in winningMovesInChildren:
                self.winner = self.turn
            elif 'Tie' in winningMovesInChildren:
                self.winner = 'Tie'
            else:
                if self.turn == 'Alice':
                    self.winner = 'Bob'
                else:
                    self.winner = 'Alice'
        
        return self.winner
            
        
    def __str__(self):
        scoreDiff = (self.scores[0] - self.scores[1])
        return str(self.turn) + str(self.depth) + str(scoreDiff)

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
        n = len(stoneValue)
        dp = [[0 for _ in range(4)] for _ in range(n)]
        
        def solve(s, M):
            if M > 3:
                return 0
            if s >= n:
                return 0
            if dp[s][M]:
                return dp[s][M]
            
            curr = 0
            best = float('-inf')
            for x in range(1, M+1):
                if s+x-1 < n:
                    curr += stoneValue[s+x-1]
                    best = max(best, curr - solve(s+x, M))
            dp[s][M] = best
            return dp[s][M]
        
        alice_score = (sum(stoneValue) + solve(0, 3)) / 2
        average = sum(stoneValue) / 2
        
        if alice_score > average:
            return 'Alice'
        elif alice_score == average:
            return 'Tie'
        else:
            return 'Bob'
        """
        
        # Building our root stone node
        root = StoneGameNode(stoneValue, 'Alice', 0, (0,0), None, {})
        
        # We've built it, now to calculate the winning moves
        return root.winningMove()