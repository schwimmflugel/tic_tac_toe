from Board import Board
from Robot import Robot
from Player import Player
import random



board = Board(3)
bot = Robot()
human = Player('1',board)
robot = Player('2',board)
tie = False


play_count = 0

while play_count < board.max_plays - 1:

    if not robot.winning_paths(board) and not human.winning_paths(board):
        tie = True
        break

    if bot.first_move == True:
        bot.random_move(board)
        bot.first_move = False
    else:
        #bot.defensive_move(board)
        bot.calculate(robot, human, board)
        # bot.random_move(board)
    
    board.print_board()

    val = board.check_for_win()
    if val == '2':
        print("Robot Wins!!!!")
        break
    
    play_count += 1
  

    if not robot.winning_paths(board) and not human.winning_paths(board):
        tie = True
        break

    
    while True:
        row = int(input("Enter row: "))-1
        collumn = int(input("Enter collumn: "))-1

        if board.assign_item(row,collumn,'1'):
            break
        else:
            print("Space taken")
    
    board.print_board()

    val = board.check_for_win()
    if val == '1':
        print("You win!!!!")
        break


    play_count += 1


if play_count >= board.max_plays - 1 or tie:
    print("Tie!!!")

