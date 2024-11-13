"""
Exercise Goal:
    - The goal of this exercise is to show us how you apply software engineering 
    principles to create a maintainable software solution.

    How to approach this:

            - Don't worry about persistence. It would make sense here, but for this
            exercise only use in-memory data structures.
            - Don't worry about tricks or "gotchyas", as there aren't any.
            - Just focus on writing clean maintainable code.



Specification:

    Create a class LeaderBoard whose interface includes the following methods:

    Method Name: add_score

        - Add a new score to the player's average. If a player doesn't exist in the 
        LeaderBoard, they will be automatically added.

        Args:

                player_id (Integer): The player's ID.
                score (Integer): The score to record for the player

        Returns:

                Double: The new average score for the given player

    Method Name: top

        - Get the top player_ids on the leaderboard ordered by their average scores
        from highest to lowest

        Args:

                num_players (Integer): The maximum number of player_ids to return

        Returns:

                List<Integer>: a list of player_ids

    Method Name: reset

        - Removes any scoring information for a player, effectively 
        resetting them to 0

        Args:

                player_id (Integer): The player's ID.

Example Usage:


    // Create a new LeaderBoard Instance
    LeaderBoard leader_board = new LeaderBoard();

    // Add scores for players to the LeaderBoard
    leader_board.add_score(1, 50); // 50.0
    leader_board.add_score(2, 80); // 80.0
    leader_board.add_score(2, 70); // 75.0
    leader_board.add_score(2, 60); // 70.0
    leader_board.add_score(3, 90); // 90.0
    leader_board.add_score(3, 85); // 87.5

    // Get top positions for the leaderboard
    leader_board.top(3); // [3, 2, 1]
    leader_board.top(2); // [3, 2]
    leader_board.top(1); // [3]

    // Reset a player 3's scores
    leader_board.reset(3); // void

    // Player 3 is now at the bottom of the leaderboard
    leader_board.top(3); // [2, 1, 3]

Expected values

    - Player IDs will always be positive integers small enough to be 
    stored as a signed 32-bit integer Scores are integers ranging from 0-100


We have provided stubbed out code and tests for you below. Please note that these tests are not exhaustive and do not cover all corner cases. We recommend extending the given tests to ensure your code is correct.
"""

# Your code goes here. Feel free to make helper classes if needed
from collections import defaultdict
import operator
import unittest

class LeaderBoard:
    """This is a class to maintain the average scores of players."""
    
    def __init__(self):
        """Constructor for LeaderBoard class."""
        
        # board maintains only the averages for each player
        self.board = defaultdict(lambda:0)
        
        # history is a dictionary that maintains 
        # all of the scores for each player
        self.history = defaultdict(lambda: [])
    
    
    def add_score(self,player_id, score):
        """ 
        Add a new score to the player's average. 
        
        If a player doesn't exist in the LeaderBoard, 
        they will be automatically added.
        
        Params: 
            player_id (int): Player's ID. 
            score(int): Score to record for the player. 
                            Ranges from 0-100.
        
        Returns: 
            double: The new average score for the given player.
        
        """
        if type(player_id) != int:
            raise TypeError("player_id is not an Integer. Required Integer")
        elif type(score) != int: 
            raise TypeError("score is not an Integer. Required Integer")
        
        else: 
            if self.history[player_id] == []:
                self.history[player_id].append(score)
                self.board[player_id] = score 
            else:
                self.history[player_id].append(score)
                new_score =  sum(self.history[player_id])/len(self.history[player_id])
                self.board[player_id] = round(new_score,1)

        return self.board[player_id]

    
    def top(self, num_players):
        """
        Get the top player_ids on the leaderboard. 
        
        player_ids are ordered by their average scores from 
        highest to lowest.
        
        Params: 
            num_players (int): Maximum number of player_ids to be returned.     
        Returns: 
            list: A list of player_ids.
        
        """
        topPlayers = []
        if num_players > len(self.board):
            raise Exception ("Argument passed exceeds the total number of players on the LeaderBoard")
        else:
            sortedDict = sorted(self.board, key = lambda p: (self.board[p], len(self.history[p])), reverse = True)  
            print(sortedDict) 
            n = len(sortedDict)
            
            # for i in range(0, num_players):
            #     topPlayers.append(sortedDict[i][0])
        
            return topPlayers
        
    
    def reset(self,player_id):
        """
        Removes any scoring information for a player.
        
        Effectively resetting them to 0. 
        
        Params: 
            player_id (int): A Player's ID. 
        """
        
        for i in range(len(self.history[player_id])):
            self.history[player_id][i] = 0 
        self.board[player_id] = 0

class test_LeaderBoard(unittest.TestCase):

    # def __init__ (self):
    #     self.test_board = LeaderBoard()
    global test_board
    test_board = LeaderBoard()
    def  test_add_single_score(self):
        result = test_board.add_score(2, 80)
        self.assertEqual(result,80)

    # def test_avg(self):
    #     result = test_board.add_score(2, 63)
    #     result = test_board.add_score(2, 45)
    #     self.assertEqual(result, 62.7)

    def test_correct_type(self):
        # result = test_board.top(100) 
        with self.assertRaises(Exception):
            test_board.top(10)


    # def 




if __name__=="__main__":        
    leader_board = LeaderBoard()
    leader_board.add_score(1, 50)
    leader_board.add_score(2, 80)
    leader_board.add_score(2, 70)
    leader_board.add_score(2, 60)
    leader_board.add_score(3, 90)
    leader_board.add_score(3, 85)
    # print(leader_board.add_score(2, 80) == 80)
    # print(leader_board.add_score(2, 70) == 75)
    # print(leader_board.add_score(2, 60) == 70)
    # print(leader_board.add_score(3, 90) == 90)
    # print(leader_board.add_score(3, 85) == 87.5)

    # print(leader_board.board)
    # print(leader_board.top(3) == [3, 2, 1])
    # print(leader_board.top(2) == [3, 2])
    # leader_board.reset(3)
    # print(leader_board.top(3) == [2, 1, 3])
    
    # trying a case where two players have their averages tied
    # using in-built stable sort to break ties for now. 
    
    leader_board.add_score(5, 30)
    leader_board.add_score(4, 30)
    leader_board.add_score(5, 20)
    leader_board.add_score(4, 20)
    
    
    # print(leader_board.board)
    leader_board.top(5)
    unittest.main()
