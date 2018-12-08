from tkinter import *

X = "X"
O = "O"
EMPTY = " "
TIE = "Нічия"
NUM_SQUARES = 9


#перевірка чи правильну відповідь дала людина
def ask_yes_no(question):
    answer = None
    while answer not in ("y", "n"):
        answer = input(question).lower()
    return answer

#перевірка чи правильну відповідь дала людина
def ask_number(question, low, high):
    answer = None
    while answer not in range(low, high):
        answer = int(input(question))
    return answer

#встановлюємо початкові значення гравців
def put_pieces():
    go_first = ask_yes_no("Хочеш ходити першим? (y/n): ")
    if go_first == "y":
        print("Що ж грай хрестиками")
        human = X
        computer = O
    else:
        print("Що ж почну я")
        human = O
        computer = X
    return computer, human

#створити нову пусту дошку
def get_new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#вивід дошки
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")


#перевірка на доступні пусті клітинки
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

#перевірка чи є переможець, якщо є то повернути його
def getWinner(board):
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    return TIE

#хід людини, перевірка чи можна встати на місце де людина хоче встати
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твій хід. Вибери поля (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("Це поле вже зайняте")
            continue
        return move

#основна логіка бота
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
    #дивлюсь чи може після мого ходу виграти людина, мішаю їй це зробити
    for move in legal_moves(board):
        board[move] = human
        if getWinner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    #якщо не можу виграти, то гляну на кілька кроків вперед, коли зможе виграти людина
    for move in legal_moves(board):
        board[move] = human
        if getWinner(board) == human:
            print(move)
            return move

#міняти грався
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

#вітаю переможця
def congratulation_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("Три", the_winner, "в ряд")

    if the_winner == computer:
        print("Я знову переміг")
    elif the_winner == human:
        print("Як ти переміг мене?")
    elif the_winner == TIE:
        print("Нічия")


def main():
    computer, human = put_pieces()
    turn = X
    board = get_new_board()
    display_board(board)
    while (getWinner(board) == TIE) and legal_moves(board) != []:
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, human, computer)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = getWinner(board)
    congratulation_winner(the_winner, computer, human)


main()
input("Натисни ентер, щоб вийти")