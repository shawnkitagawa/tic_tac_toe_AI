# Tic Tac Toe with Computer 
import random

class tic_tac_toe():
    def __init__(self):
        self.board = []
        self.symbol = " O "
        for i in range(3):
            board_x = []
            for j in range(3):
                board_x.append("__")
            self.board.append(board_x)


    def display(self):
        for i in range(3):
            print(self.board[i])

    def turn(self):
        if self.symbol == " O ":
            self.symbol = " X "
        else:
            self.symbol = " O "

    def computer(self):
        position = ["00", "01" , "02" , "10" , "11", "12", "20", "21", "22"]
        while True:
            computer_input = random.choice(position)
            y , x =  self.position(computer_input)
            if self.board[y][x] == "__":
                return y, x
        
        

    def position(self, input):
        if int(input) < 10:
            y = 0 
            x = int(input)
        elif int(input) < 20:
            y = 1
            x = int(input) - 10

        else:
            y = 2 
            x = int(input) - 20  

        return (y,x) 


    def user_input(self):
        x =  -1
        y =  -1 
        while True:
            try: 
                user = input("Input a valid cordinate 00 , 01 , 02 , 10 , 11, 12, 20, 21, 22:   ")

                y, x = self.position(user)

                if user not in ["00", "01", "02", "10", "11", "12", "20", "21", "22"] or self.board[y][x] != "__":
                    raise ValueError("You have inserted an invalid input. Please choose from the valid option.")
                
                return y,x 
            
            except ValueError as e :
                print(e)


    def update_board(self, cordinate):
        y = cordinate[0]
        x = cordinate[1]
        self.board[y][x] = self.symbol

    def judge(self):
        # Check if one of the user won
        left_diagnol = True 
        right_diagnol = True 

        for i in range(3):
            # horizontal 
            if all(self.board[i][j] == self.symbol for j in range(3)):
                print(f"{self.symbol} horizontal win ")
                return True
            elif all(self.board[j][i] == self.symbol for j in range(3)):
                print(f"{self.symbol} Vertical Win ")
                return True 
            

            if self.board[i][i] != self.symbol:
                left_diagnol = False
            if self.board[i][2- i] != self.symbol:
                right_diagnol = False
            
        if left_diagnol == True or right_diagnol == True:
            print(f"{self.symbol} diagnol win")
            return True
        
        return False

        





play = tic_tac_toe()
play.display()
count = 0

while play.judge() == False:
    if count % 2 == 0 :
        cordinate = play.user_input()
    else:
        play.turn()
        cordinate = play.computer()
    count += 1 

    play.update_board(cordinate)
    play.display()


