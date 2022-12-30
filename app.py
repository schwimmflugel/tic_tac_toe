from Board import Board
from Robot import Robot
from Player import Player

class App():
    def __init__(self):
        self.board = Board(3)
        self.bot = Robot(self.board)
        self.human = Player('1',self.board)
        #self.robot = Player('2',self.board)
        self.tie = False
        self.play_count = 0

    def robot_turn(self):
        if self.bot.first_move == True:
            self.bot.random_move(self.board)
            self.bot.first_move = False
        else:
            self.bot.calculate(self.human, self.board)
  
        self.play_count += 1
        self.board.print_board()

    def human_turn(self, row, collumn):
        if self.board.assign_item(row,collumn,'1'):
            self.play_count += 1
            self.board.print_board()
            return True
        else:
            print("Space taken")
            return False

    def check_win(self):
        return self.board.check_for_win()

    def check_for_tie(self):
        if not self.bot.player.winning_paths(self.board) and not self.human.winning_paths(self.board):
            self.tie = True
            return True
        return False
        

