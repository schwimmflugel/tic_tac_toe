class Row():
    def __init__(self, item_count):
        self.items = []
        self.item_count = item_count
        self.default_char = '#'
        self.player_1_char = '1'
        self.player_2_char = '2'
        self.default_count = self.item_count
        self.player_1_count = 0
        self.player_2_count = 0

        for count in range(0,item_count):
            self.items.append(self.default_char)

    def print_row(self):
        for count, item in enumerate(self.items):
            print(" %s "%item,end='')
            if count < self.item_count - 1:
                print(' | ',end='')
        print('')

    def check_row(self):
        self.default_count = self.items.count(self.default_char)
        self.player_1_count = self.items.count(self.player_1_char)
        self.player_2_count = self.items.count(self.player_2_char)

        if self.player_1_count == self.item_count:
            return self.player_1_char
        elif self.player_2_count == self.item_count:
            return self.player_2_char
        else:
            return ""



