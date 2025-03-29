# Tic Tac Toe using minmax 

import copy 

class Node():
    def __init__(self,board,cordinates, empty_space,current_symbol,score, prev = None):
        self.empty_space = empty_space
        self.current_symbol = current_symbol
        self.score = score
        self.children = []
        self.prev = prev
        self.board = board
        self.cordinates = cordinates





class tic_tac_toe():
    def __init__(self):
        self.head = Node(None, None,None, None, None)
        self.board = []
        self.current_symbol = " O "
        for i in range(3):
            board_x = []
            for j in range(3):
                board_x.append("__")

            self.board.append(board_x)



    def append_level(self):
        empty_list = []
        score = 0 
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "__":
                    empty_list.append((i,j))

        empty_children = False

        print(f"head is address {self.head}")
        
        #i represents Possibility in that level 
        for i in range(len(empty_list)):
            row = int(empty_list[i][0])
            column = int(empty_list[i][1])
            board_temp = copy.deepcopy(self.board)
            board_temp[row][column] = self.current_symbol


            new_node = Node(board_temp,empty_list[i],len(empty_list) - 1,self.current_symbol,score)
            current = self.head
            current_prev = None 
            if len(current.children) == 0 or empty_children == True:
                current.children.append(new_node)
                empty_children = True
            else:
                while current.children[i] != None:
                    current_prev = current
                    current = current.children
                current.children = new_node
            if current_prev == None:
                current.prev = self.head
            else:
                current.prev = current_prev


            print("_________________________________")
            print(f"previous address{current.prev}")
            print(f"children address{current.children[i]}")
            print(f"case{i}")
            self.display(board_temp)

    def display(self, board):
        for i in range(3):
            print(board[i])
            

    def change_turn(self):
        if self.current_symbol == " O ":
            self.current_symbol = " X "


play = tic_tac_toe()
play.append_level()



        
    

