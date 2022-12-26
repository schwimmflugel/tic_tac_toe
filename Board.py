from Row import Row
import os

#from numpy import unravel_index
#import array

class Board():
    def __init__(self, size = 3):
        self.size = size
        self.max_plays = self.size * self.size
        self.rows : Row = []
        self.collumns = []
        self.diagonals = []
        self.player_1_count_rows = []
        self.player_1_count_collumns = []
        self.player_1_count_diagonal_1 = 0
        self.player_1_count_diagonal_2 = 0
        self.player_2_count_rows = []
        self.player_2_count_collumns = []
        self.player_2_count_diagonal_1 = 0
        self.player_2_count_diagonal_2 = 0
        self.max_route = 0
        self.max_index = 0
       
        for count in range(0,self.size):
            row = Row(self.size)
            self.rows.append(row)
            self.player_1_count_rows.append(0)
            self.player_1_count_collumns.append(0)
            self.player_2_count_rows.append(0)
            self.player_2_count_collumns.append(0)



        self.print_board()

        
    def print_board(self):
        #os.system('cls')
        print('\n\n')
        print('    ',end='')
        for x in range(1,self.size+1):
            print('%d     '%x,end='')
        print('\n')
        for x, row  in enumerate(self.rows):
            print('%d  '%(x+1), end='')
            row.print_row()
            if x < row.item_count - 1:
                print('   ',end='')
                for i in range(0,self.size):
                    print('-----',end='')
                    if i == self.size - 1:
                        print('')
            else:
                print('\n\n')

    def assign_item(self, row, item, val):
        current_item = self.rows[row].items[item]
        if current_item == '#':
            self.rows[row].items[item] = val
            return True
        return False


    def build_collumns(self):
        for i in range(0,self.size):
            items = []
            for row in self.rows:
                items.append(row.items[i])
            if len(self.collumns) != self.size:
                self.collumns.append(items)
            else:
                self.collumns[i] = items
        #print(self.collumns)


    def check_collumns(self):
        self.build_collumns()
        for i, collumn in enumerate(self.collumns):
            self.player_1_count_collumns[i] = collumn.count('1')
            self.player_2_count_collumns[i] = collumn.count('2')  

            if self.player_1_count_collumns[i] == self.size:
                return '1'  
            elif self.player_2_count_collumns[i] == self.size:
                return '2' 

        return ""

    def build_diagonals(self):
        items_1 = []
        items_2 = []
        for i, row in enumerate(self.rows):
            items_1.append(row.items[i])
            items_2.append(row.items[row.item_count - 1 - i])
        
        if len(self.diagonals) != 2:
            self.diagonals.append(items_1)
            self.diagonals.append(items_2)
        else:
            self.diagonals[0] = items_1
            self.diagonals[1] = items_2

        #print(self.diagonals)



    def check_diagonals(self):
        self.build_diagonals()
        self.player_1_count_diagonal_1 = self.diagonals[0].count('1')
        self.player_1_count_diagonal_2 = self.diagonals[1].count('1')
        self.player_2_count_diagonal_1 = self.diagonals[0].count('2')
        self.player_2_count_diagonal_2 = self.diagonals[1].count('2')

        if self.player_1_count_diagonal_1 == self.size or self.player_1_count_diagonal_2 == self.size:
            return '1'  
        elif self.player_2_count_diagonal_1 == self.size or self.player_2_count_diagonal_2 == self.size:
            return '2' 
        
        return ""

    def closest_to_win(self, player):
        player_1_options = []
        player_2_options = []

        player_1_options.append(self.player_1_count_rows)
        player_1_options.append(self.player_1_count_collumns)
        player_1_options.append(self.player_1_count_diagonal_1)
        player_1_options.append(self.player_1_count_diagonal_2)
      
        player_2_options.append(self.player_2_count_rows)
        player_2_options.append(self.player_2_count_collumns)
        player_2_options.append(self.player_2_count_diagonal_1)
        player_2_options.append(self.player_2_count_diagonal_2)

        if player == '1':
            player_options = player_1_options
        elif player == '2':
            player_options = player_2_options

        self.max_route = 0 #Track if best option is in rows, collumns, diagonal 1, or diagonal 2
        self.max_index = 0 #Track index of best option (ex. best option is in rows and in row 1 (0,2))
        for route in player_options:
            print(route)
            if type(route) == list:
                for index in route:
                    if index > self.max_index:
                        self.max_index = index
                        self.max_route = route
            else:
                if index > self.max_index:
                    self.max_index = index
                    self.max_route = route

        if(self.max_route == 0):
            print("Best move in Row: %d"(self.max_index+1))
        elif(self.max_route == 1):
            print("Best move in Column: %d"(self.max_index+1))
        elif(self.max_route == 2):
            print("Best move in Diagonal 1")
        elif(self.max_route == 3):
            print("Best move in Diagonal 2")


    def check_for_win(self):
        #Check if there is a winner in the rows
        for i, row in enumerate(self.rows):
            response = row.check_row()
            self.player_1_count_rows[i] = row.player_1_count
            self.player_2_count_rows[i] = row.player_2_count
            if response != "":
                return response
        #Check for a winner in the collumns
        response = self.check_collumns()
        if response != "":
            return response

        #Check for a winner in the diagonals
        response = self.check_diagonals()
        if response != "":
            return response


        

    

