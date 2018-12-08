import tkinter as tk
from tkinter import *

X = "X"
O = "O"
EMPTY = " "
TIE = "Нічия"
NUM_SQUARES = 9

def pos0():
    step(0)
def pos1():
    step(1)
def pos2():
    step(2)
def pos3():
    step(3)
def pos4():
    step(4)
def pos5():
    step(5)
def pos6():
    step(6)
def pos7():
    step(7)
def pos8():
    step(8)


def step(pos):
    computer, human = O, X
    if (getWinner(board) == TIE) and legal_moves(board) != []:
        if pos in legal_moves(board):
            board[pos] = human
            if (getWinner(board) == TIE) and legal_moves(board) != []:
                move = computer_move(board, human, computer)
                board[move] = computer
        display_board(board)
    if not((getWinner(board) == TIE) and legal_moves(board) != []):
        the_winner = getWinner(board)
        congratulation_winner(the_winner, computer, human)
        if not ((getWinner(board) == TIE) and legal_moves(board) != []):
            root.quit()

# створити нову пусту дошку
def get_new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


# вивід дошки
def display_board(board):
    for i in range(len(board)):
        buttons[i]["text"] = board[i]


# перевірка на доступні пусті клітинки
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


# перевірка чи є переможець, якщо є то повернути його
def getWinner(board):
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    return TIE


# основна логіка бота
def computer_move(board, human, computer):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я виберу поле номер", end=" ")
    # дивлюсь чи можу я на цьому ході виграти, пробую це зробити
    for move in legal_moves(board):
        board[move] = computer
        if getWinner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    # дивлюсь чи може після мого ходу виграти людина, мішаю їй це зробити
    for move in legal_moves(board):
        board[move] = human
        if getWinner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    # якщо не можу виграти, то гляну на кілька кроків вперед, коли зможе виграти людина
    for move in legal_moves(board):
        board[move] = human
        if getWinner(board) == human:
            print(move)
            return move

# вітаю переможця
def congratulation_winner(the_winner, computer, human):

    def close_cong():
        cong.quit()

    def get_new_game():
        cong.destroy()
        global board
        board = get_new_board()
        display_board(board)

    cong = Tk()
    cong.minsize(20, 20)
    cong.title("Congratulation winner")

    ext = tk.Button(cong, text='EXIT', command=close_cong).grid(row=2, column=1)
    new_game = tk.Button(cong, text='TRY AGAIN', command=get_new_game).grid(row=2, column=2)
    value = ''
    if the_winner != TIE:
        value = ("Три", the_winner, "в ряд")
        print(value)
    if the_winner == computer:
        value = ("Я знову переміг")
        print(value)
    elif the_winner == human:
        value = ("Як ти переміг мене?")
        print(value)
    elif the_winner == TIE:
        value = ("Нічия")
        print(value)
    output = Text(cong, bg="lightblue", font="Arial 12", height=10, width=20)
    output.grid(row=1, columnspan=5)
    output.insert("0.0", value)
    cong.mainloop()


root = Tk()
root.title("Tic-Tac-Toe")



p0 = tk.Button(root, text='', height = 10, width = 20, command=pos0)
p1 = tk.Button(root, text='', height = 10, width = 20, command=pos1)
p2 = tk.Button(root, text='', height = 10, width = 20, command=pos2)
p3 = tk.Button(root, text='', height = 10, width = 20, command=pos3)
p4 = tk.Button(root, text='', height = 10, width = 20, command=pos4)
p5 = tk.Button(root, text='', height = 10, width = 20, command=pos5)
p6 = tk.Button(root, text='', height = 10, width = 20, command=pos6)
p7 = tk.Button(root, text='', height = 10, width = 20, command=pos7)
p8 = tk.Button(root, text='', height = 10, width = 20, command=pos8)


p0.grid(row=1, column=1)
p1.grid(row=1, column=2)
p2.grid(row=1, column=3)
p3.grid(row=2, column=1)
p4.grid(row=2, column=2)
p5.grid(row=2, column=3)
p6.grid(row=3, column=1)
p7.grid(row=3, column=2)
p8.grid(row=3, column=3)
buttons = [p0, p1, p2, p3, p4, p5, p6, p7, p8]
board = get_new_board()

root.mainloop()