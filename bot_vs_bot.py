from Board import Board
from Robot import Robot
from Player import Player

import time



robot1_wins = 0
robot2_wins = 0
ties = 0

for i in range(0,10):
    board = Board(3)
    bot1 = Robot('1')
    bot2 = Robot('2')
    robot1 = Player('1',board)
    robot2 = Player('2',board)
    tie = False

    play_count = 0

    while play_count < board.max_plays:

        if not robot1.winning_paths(board) and not robot2.winning_paths(board):
            tie = True
            break

        if bot1.first_move == True:
            bot1.random_move(board)
            bot1.first_move = False
        else:
            #bot.defensive_move(board)
            bot1.calculate(robot1, robot2, board)
            # bot.random_move(board)
        
        board.print_board()

        val = board.check_for_win()
        if val == '1':
            print("Robot 1 Wins!!!!")
            robot1_wins += 1
            break
        

        time.sleep(1)
        play_count += 1
    

        if not robot1.winning_paths(board) and not robot2.winning_paths(board):
            tie = True
            break

        bot2.calculate(robot2, robot1, board)
        
        board.print_board()

        val = board.check_for_win()
        if val == '2':
            print("Robot 2 Wins!!!!")
            robot2_wins += 1
            break

        #player2.winning_paths(board)
        #print(player2.paths)

        time.sleep(1)
        play_count += 1


    if tie == True:
        print("Tie!!!")
        ties += 1

print("Robot1 wins: %d times"%robot1_wins)
print("Robot2 wins: %d times"%robot2_wins)
print("Ties: %d"%ties)

