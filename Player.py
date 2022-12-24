from Board import Board
import random
import time

class Player():
    def __init__(self, token, board : Board):
        self.size = board.size
        self.paths = {}
        self.token = token
        self.board = board
        self.timeout = 0.2

    def winning_paths(self, board : Board):
        #Each game has 2x the grid size (all rows and all collumns) + 2 diagonals ways to win 
        #A winning path will be categorized by the steps away from winning. a step of 'size' 
        #means it's completely open, and -1 means it's been blocked by the other player

        self.board = board

        #Populate data for the rows
        for i, row in enumerate(self.board.rows):
            row.check_row()
            if self.token == '1':
                if row.player_2_count > 0:
                    self.paths["h%d"%i] = -1
                else:
                    self.paths["h%d"%i] = row.player_1_count

            elif self.token == '2':
                if row.player_1_count > 0:
                    self.paths["h%d"%i] = -1
                else:
                    self.paths["h%d"%i] = row.player_2_count
 
        #Populate data for the collumns
        self.board.check_collumns()
        if self.token == '1':
            for i in range(len(self.board.player_1_count_collumns)):
                if self.board.player_2_count_collumns[i] > 0:
                    self.paths["c%d"%i] = -1
                else:
                    self.paths["c%d"%i] = self.board.player_1_count_collumns[i]

        elif self.token == '2':
            for i in range(len(self.board.player_2_count_collumns)):
                if self.board.player_1_count_collumns[i] > 0:
                    self.paths["c%d"%i] = -1
                else:
                    self.paths["c%d"%i] = self.board.player_2_count_collumns[i]

        #Populate data for the diagonals
        self.board.check_diagonals()
        if self.token == '1':
            if self.board.player_2_count_diagonal_1 > 0:
                self.paths["d1"] = -1
            else:
                self.paths["d1"] = self.board.player_1_count_diagonal_1
            
            if self.board.player_2_count_diagonal_2 > 0:
                self.paths["d2"] = -1
            else:
                self.paths["d2"] = self.board.player_1_count_diagonal_2

        elif self.token == '2':
            if self.board.player_1_count_diagonal_1 > 0:
                self.paths["d1"] = -1
            else:
                self.paths["d1"] = self.board.player_2_count_diagonal_1
            
            if self.board.player_1_count_diagonal_2 > 0:
                self.paths["d2"] = -1
            else:
                self.paths["d2"] = self.board.player_2_count_diagonal_2

        #print(max(self.paths.values()))
        if max(self.paths.values()) < 0:
            return False #Return false if there are no winning paths and the game is over
        
        return True



    def offensive_move(self, board:Board, modifyToken = ''):
        if modifyToken == '': #Modify the playing token, this was Player 2 can play based on the offensive move that Player 1 would take
            token = self.token
        else:
            token = modifyToken

        #Shuffle the dictionary so the max isn't always selected in the same order
        l = list(self.paths.items())
        random.shuffle(l)
        randomized_paths = dict(l)

        #self.winning_paths(board)
        #max_path = max(self.paths, key=self.paths.get)
        max_path = max(randomized_paths, key=randomized_paths.get)
        #print(max_path)

        start_time = time.time()
        if(max_path[0]=='h'): #Horizontal (row) winning path
            while True:
                if board.assign_item(row = int(max_path[1]), item = random.randint(0, board.size-1), val=token):
                    break
                if time.time() - start_time >= self.timeout:
                    break
        
        elif(max_path[0]=='c'): #Collumn winning path
            while True:
                if board.assign_item(row = random.randint(0, board.size-1), item = int(max_path[1]), val=token):
                    break
                if time.time() - start_time >= self.timeout:
                    break

        elif(max_path=='d1'): #Diagonal Top Left to Bottom Right winning path
            while True:
                spot = random.randint(0, board.size-1)
                if board.assign_item(row = spot, item = spot, val=token):
                    break
                if time.time() - start_time >= self.timeout:
                    break
        
        elif(max_path=='d2'): #Diagonal Top Right to Bottom Left winning path
            while True:
                collumn = random.randint(0, board.size-1)
                row = board.size - collumn - 1
                if board.assign_item(row = row, item = collumn, val=token):
                    break
                if time.time() - start_time >= self.timeout:
                    break
            
