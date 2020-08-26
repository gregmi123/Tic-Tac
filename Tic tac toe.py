start=1
#To restart the game 
while True:
    if start!=1:
        play=input("Do you want to play again Yes or No")
        if play=="Yes":
            pass
        elif play=="No":
            print("Thank You!!!!!!")
            break
        else:
            print("Invalid input")
            continue
    
    #For board of the game
    board=["-","-","-",
        "-","-","-",
        "-","-","-"]
      
    game_is_still_going=True

    winner=None

    current_player="X"

    #For displaying board of tic tac
    def display_board():
        print(board[0]+"|"+board[1]+"|"+board[2])
        print(board[3]+"|"+board[4]+"|"+board[5])
        print(board[6]+"|"+board[7]+"|"+board[8])  

    #For player turn
    def handle_turn():
        print(current_player ," turn")
        position=input("Choose position between 0 to 9:")
        valid=False
        while not valid:
            while position not in ["1","2","3","4","5","6","7","8","9"]:
                position=input("Choose position between 0 to 9:")
            position=int(position)-1
            if board[position]=="-":
                valid=True
            else:
                print("Position is occupied. Enter a new position")
        board[position]=current_player

    #For playing game
    def play_game():
        while game_is_still_going:
            display_board()
            handle_turn()
            check_if_game_over()
            flip_turn()
        
        if winner=="X" or winner=="0":
            display_board()
            print(winner , "won")
        elif winner==None:
            display_board()
            print("Tie")
        return
        
        

    #For checking the game 
    def check_if_game_over():
        check_winner()
        check_tie()

    #to check the winner    
    def check_winner():
        global winner

        #Winner from row evaluation
        row_winner=check_rows()

        #Winner from column evaluation
        column_winner=check_columns()
        
        #Winner from diagonal evaluation
        diagonal_winner=check_diagonals()

        #Confirming the winner "X" or "0"
        if row_winner:
            winner=row_winner
        elif column_winner:
            winner=column_winner
        elif diagonal_winner:
            winner=diagonal_winner
        return

    #Checking rows equality 
    def check_rows():
        global game_is_still_going
        row_1=board[0]==board[1]==board[2] !="-"
        row_2=board[3]==board[4]==board[5] !="-"
        row_3=board[6]==board[7]==board[8] !="-"

        if row_1 or row_2 or row_3:
            game_is_still_going=False
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
        return

    #Checking columns equality
    def check_columns():
        global game_is_still_going
        column_1=board[0]==board[3]==board[6] !="-"
        column_2=board[1]==board[4]==board[7] !="-"
        column_3=board[2]==board[5]==board[8] !="-"

        if column_1 or column_2 or column_3:
            game_is_still_going=False
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]
        return

    #Checking diagonals equality
    def check_diagonals():
        global game_is_still_going
        diagonal_1=board[0]==board[4]==board[8] !="-"
        diagonal_2=board[2]==board[4]==board[6] !="-"

        if diagonal_1 or diagonal_2:
            game_is_still_going=False

        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[2]
        return

    #Checking tie
    def check_tie():
        global game_is_still_going
        if "-" not in board:
            game_is_still_going=False

    #To flip the turn of players
    def flip_turn():
        global current_player
        if current_player=="X":
            current_player="0"
        elif current_player=="0":
            current_player="X"
        return
    
    play_game()

    if start==1:
        start=0


