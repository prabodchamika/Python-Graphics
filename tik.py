import tkinter as tk
from tkinter import messagebox

PLAYER = "X"
AI = "O"
EMPTY = " "
WIN_COLOR = "#76ff03"  
BG_COLOR = "#2E2E2E" 
FG_COLOR = "#F5F5F5" 
BUTTON_COLOR = "#3A3A3A"  
BUTTON_HOVER = "#505050"  
HIGHLIGHT_COLOR = "#757575"  

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg=BG_COLOR)
        self.board = [EMPTY] * 9
        self.buttons = []
        self.current_player = PLAYER
        self.create_widgets()

    def create_widgets(self):
        
        for i in range(9):
            button = tk.Button(
                self.root, text=EMPTY, font=("Helvetica", 32, "bold"), width=5, height=2,
                bg=BUTTON_COLOR, fg=FG_COLOR, 
                command=lambda i=i: self.on_button_click(i),
                activebackground=HIGHLIGHT_COLOR,
                relief="flat",  
                bd=0  
            )
            button.grid(row=i//3, column=i%3, sticky="nsew") 
            button.bind("<Enter>", lambda e, b=button: b.config(bg=BUTTON_HOVER)) 
            button.bind("<Leave>", lambda e, b=button: b.config(bg=BUTTON_COLOR))  
            self.buttons.append(button)
        
       
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)
        
      
        reset_button = tk.Button(
            self.root, text="Reset", font=("Helvetica", 16, "bold"), width=10,
            bg=BUTTON_COLOR, fg=FG_COLOR, command=self.reset_game,
            activebackground=HIGHLIGHT_COLOR,
            relief="flat", bd=0
        )
        reset_button.grid(row=3, column=0, columnspan=3, pady=(10, 0))

    def on_button_click(self, index):
        if self.board[index] == EMPTY and self.current_player == PLAYER:
            self.make_move(index, PLAYER)
            if not self.check_winner():
                self.ai_move()

    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index].config(text=player)
        if player == PLAYER:
            self.buttons[index].config(state="disabled")
        self.check_winner()

    def ai_move(self):
        best_move = self.get_best_move()
        if best_move is not None:
            self.make_move(best_move, AI)

    def get_best_move(self):
        
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == EMPTY:
                self.board[i] = AI
                score = self.minimax(self.board, 0, False)
                self.board[i] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def minimax(self, board, depth, is_maximizing):
        if self.is_winner(board, AI):
            return 1
        if self.is_winner(board, PLAYER):
            return -1
        if EMPTY not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == EMPTY:
                    board[i] = AI
                    score = self.minimax(board, depth + 1, False)
                    board[i] = EMPTY
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == EMPTY:
                    board[i] = PLAYER
                    score = self.minimax(board, depth + 1, True)
                    board[i] = EMPTY
                    best_score = min(score, best_score)
            return best_score

    def is_winner(self, board, player):
    
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]              
        ]
        for combo in win_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True
        return False

    def check_winner(self):
       
        if self.is_winner(self.board, PLAYER):
            self.highlight_winner(PLAYER)
            messagebox.showinfo("Game Over", "You win!")
            return True
        elif self.is_winner(self.board, AI):
            self.highlight_winner(AI)
            messagebox.showinfo("Game Over", "You Lost!")
            return True
        elif EMPTY not in self.board:
            messagebox.showinfo("Game Over", "Draw!")
            return True
        return False

    def highlight_winner(self, player):
       
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]             
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                for index in combo:
                    self.buttons[index].config(bg=WIN_COLOR)

    def reset_game(self):
       
        self.board = [EMPTY] * 9
        for button in self.buttons:
            button.config(text=EMPTY, state="normal", bg=BUTTON_COLOR)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.geometry("400x450")  
    root.mainloop()
