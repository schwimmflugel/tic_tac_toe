from Board import Board
from Player import Player
import random

class Robot():
    def __init__(self, token = '2'):
        self.board : Board = None
        self.robotToken = token
        self.first_move = True
        pass

    def random_move(self, board : Board):
        self.board = board

        while True:
            row = random.randint(0,self.board.size-1)
            collumn = random.randint(0,self.board.size-1)
            val = self.board.rows[row].items[collumn]

            if self.board.assign_item(row, collumn, self.robotToken):
                break

    def calculate(self, robot:Player, opponent:Player, board : Board):
        robot.winning_paths(board)
        opponent.winning_paths(board)
        
        if max(robot.paths.values()) == board.size - 1: #If the bot is one away from winning, make the final winning move
            self.offensive_move(robot, board)
        elif max(opponent.paths.values()) == board.size - 1: #If the opponent is one away from winning, stop them
            self.defensive_move(opponent, board)
        else:
            self.offensive_move(robot, board) #otherwise make an offensive move

    def defensive_move(self, opponent:Player, board : Board):
        #A defensive move looks at the most offensive move the opponent could take, and takes that spot
        opponent.offensive_move(board, modifyToken=self.robotToken)
        #print("Made a defensive move")

    def offensive_move(self, robot:Player, board:Board):
        #Look where wins are not possible and go for the closest winning path
        robot.offensive_move(board)
        #print("Made an offensive move")