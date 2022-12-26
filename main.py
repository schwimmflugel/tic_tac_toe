from App import App

app = App()

while app.play_count < app.board.max_plays - 1:
    if app.check_for_tie():
        break

    app.robot_turn()
    
    if app.check_win() == '2':
        print("Robot Wins!!!")
        break

    if app.check_for_tie():
        break

    while True:
        row = int(input("Enter row: "))-1
        collumn = int(input("Enter collumn: "))-1

        if app.human_turn(row, collumn):
            break

    if app.check_win() == '1':
        print("You Win!!!")
        break

    if app.check_for_tie():
        break

app.check_for_tie()
if app.play_count >= app.board.max_plays or app.tie:
    print("Tie!!!")

