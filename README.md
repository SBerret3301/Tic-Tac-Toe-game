Certainly! Let's go through each function in the code and explain what happens in each one:

1. **Main Window Setup:**
   ```python
   main = Tk()
   main.title("Tic-Tac-Toe Game")
   main.resizable(False, False)
   main.iconbitmap("C:\\Users\\salah\\Downloads\\POO\\json\\icontic.ico")
   ```
   - This code creates the main window (`main`) using `Tk()`.
   - Sets the title of the main window to "Tic-Tac-Toe Game".
   - Disables resizing of the main window.
   - Sets the window icon using the provided path.

2. **Background Image Setup:**
   ```python
   img = PhotoImage(file='C:\\Users\\salah\\Downloads\\POO\\json\\back.png')
   image_width = img.width()
   image_height = img.height()
   main.geometry(f"{image_width}x{image_height}")
   background_label = Label(main, image=img)
   background_label.place(relwidth=1, relheight=1)
   ```
   - Loads a background image (`back.png`) using the `PhotoImage` class.
   - Gets the width and height of the image.
   - Sets the size of the main window to match the image dimensions.
   - Creates a label (`background_label`) with the background image and places it to cover the entire window.

3. **Start Function:**
   ```python
   def Start():
       window = Tk()
       window.title("Tic Tac Toe")
       board = [' ' for i in range(9)]
   ```
   - This function is called when the "Start" button is pressed.
   - Creates a new game window (`window`) using `Tk()`.
   - Sets the title of the game window to "Tic Tac Toe".
   - Initializes the game board as a list of nine empty spaces.

4. **Check Win Function:**
   ```python
   def check_win(player_mark, board):
       win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
       for condition in win_conditions:
           if board[condition[0]] == board[condition[1]] == board[condition[2]] == player_mark:
               return True
       return False
   ```
   - Takes a player's mark and the current state of the game board as input.
   - Checks if the player has won based on the win conditions (combinations of indices) on the board.
   - Returns `True` if the player has won, otherwise returns `False`.

5. **Mark Spot Function:**
   ```python
   def mark_spot(player, row, col):
       index = 3 * row + col

       if board[index] == ' ':
           board[index] = player
           button = Button(window, text=player, width=20, height=10)
           button.grid(row=row, column=col)

           if check_win(player, board):
               messagebox.showinfo("Tic Tac Toe", f"Player '{player}' has won!")
               window.destroy()
           else:
               c = 0
               for condition in board:
                   if condition != " ":
                       c += 1
               if c == 9:
                   messagebox.showinfo("Tic Tac Toe", "Draw")
                   window.destroy()
   ```
   - Marks a spot on the game board when a player makes a move.
   - Checks if the spot is empty before marking.
   - Creates a button with the player's mark and places it on the game window.
   - Checks if the move results in a win using `check_win`.
   - Displays a message if the player has won or if the game is a draw.
   - Destroys the game window (`window`) after the game ends.

6. **Game Board Setup:**
   ```python
   for i in range(3):
       for j in range(3):
           button = Button(window, text=' ', command=lambda row=i, col=j: mark_spot('X' if sum(cell == ' ' for cell in board) % 2 == 1 else 'O', row, col), width=20, height=10)
           button.grid(row=i, column=j)
   ```
   - Sets up the 3x3 grid of buttons for the game board.
   - Each button is associated with the `mark_spot` function using the `command` parameter.
   - Uses a lambda function to pass the current row and column to the `mark_spot` function.
   - Buttons initially have empty text and a size of 20x10.

7. **Main Window Widgets (Labels and Buttons):**
   ```python
   lab = Label(main, text="Tic-Tac-Toe", font=('Consolas', 40, 'bold'), bg='black', fg='white')
   lab.pack()

   btn = Button(main, text='Start', font=100, command=Start, bg='black', fg='white')
   btn.place(x=95, y=120)
   btn.config(width=15, height=2)

   exit_button = Button(main, text="Exit", bg='black', fg='white', font=100, command=lambda: exit())
   exit_button.place(x=95, y=184)
   exit_button.config(width=15, height=2)
   ```
   - Creates a label (`lab`) with the text "Tic-Tac-Toe", a font, and background/foreground colors.
   - Packs the label into the main window.
   - Creates a "Start" button (`btn`) with a specific font, command (`Start` function), and colors.
   - Places the "Start" button at coordinates (95, 120) and sets its size.
   - Creates an "Exit" button (`exit_button`) with a specific font, command (closes the program), and colors.
   - Places the "Exit" button at coordinates (95, 184) and sets its size.

8. **Main Loop:**
   ```python
   main.mainloop()
   ```
   - Runs the main event loop, allowing the GUI to respond to user actions.
   - Keeps the main window open until it is closed by the user.

This code creates a graphical Tic-Tac-Toe game using Tkinter, with a main menu that includes a title label, a "Start" button to begin the game, and an "Exit" button to close the program. When the "Start" button is pressed, a new game window opens, and players can make moves by clicking on the buttons in the 3x3 grid. The game checks for a win or draw after each move and displays a message accordingly. The main window has a background image and is styled with different fonts and colors.
