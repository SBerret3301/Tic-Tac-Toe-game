from tkinter import *
from tkinter import messagebox

# Create the main window
main = Tk()
main.title("Tic-Tac-Toe Game")
main.resizable(False, False)
main.iconbitmap("C:\\Users\\salah\\Downloads\\POO\\json\\icontic.ico")

# Load background image
img = PhotoImage(file='C:\\Users\\salah\\Downloads\\POO\\json\\back.png')
image_width = img.width()
image_height = img.height()
main.geometry(f"{image_width}x{image_height}")
background_label = Label(main, image=img)
background_label.place(relwidth=1, relheight=1)

# Function to start the game
def Start():
    # Create the game window
    window = Tk()
    window.title("Tic Tac Toe")

    # Define the game board
    board = [' ' for i in range(9)]

    # Function to check if a player has won
    def check_win(player_mark, board):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == player_mark:
                return True
        return False

    # Function to mark a spot on the board
    def mark_spot(player, row, col):
        index = 3 * row + col

        # Check if the spot is empty
        if board[index] == ' ':
            board[index] = player
            button = Button(window, text=player, width=20, height=10)
            button.grid(row=row, column=col)

            # Check if the current move results in a win
            if check_win(player, board):
                messagebox.showinfo("Tic Tac Toe", f"Player '{player}' has won!")
                window.destroy()

            # Check for a draw
            else:
                c = 0
                for condition in board:
                    if condition != " ":
                        c += 1
                if c == 9:
                    messagebox.showinfo("Tic Tac Toe", "Draw")
                    window.destroy()

    # Set up the game board
    for i in range(3):
        for j in range(3):
            button = Button(window, text=' ', command=lambda row=i, col=j: mark_spot('X' if sum(cell == ' ' for cell in board) % 2 == 1 else 'O', row, col), width=20, height=10)
            button.grid(row=i, column=j)

    window.mainloop()

# Create labels and buttons for the main window
lab = Label(main, text="Tic-Tac-Toe", font=('Consolas', 40, 'bold'), bg='black', fg='white')
lab.pack()

btn = Button(main, text='Start', font=100, command=Start, bg='black', fg='white')
btn.place(x=95, y=120)
btn.config(width=15, height=2)

exit_button = Button(main, text="Exit", bg='black', fg='white', font=100, command=lambda: exit())
exit_button.place(x=95, y=184)
exit_button.config(width=15, height=2)

main.mainloop()
