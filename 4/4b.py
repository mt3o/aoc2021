import sys
from typing import List, Any

BoardLine = List[int]
Board = List[BoardLine]

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def parse_board_line(board_line) -> List[int]:
    return [int(i) for i in board_line.split(" ") if is_integer(i)]


def is_winning_board(board):

    for row in range(5):
        if sum(board[row]) == 0:
            return True
    for col in range(5):
        single_column = [board[n][col] for n in range(5)]
        if sum(single_column) == 0:
            return True
    return False

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.readlines()
    randoms = [int(i) for i in input[0].split(",")]

    boards: List[Board] = []
    board_pointer = -1
    board_lines = (l.replace("\n", "") for l in input[1:])

    for _ in board_lines:
        boards.append([
            parse_board_line(next(board_lines)),
            parse_board_line(next(board_lines)),
            parse_board_line(next(board_lines)),
            parse_board_line(next(board_lines)),
            parse_board_line(next(board_lines)),
        ])  # add new board

    for attempt, sample in enumerate(randoms):
        for board in boards:
            if is_winning_board(board):
                continue
            for i in range(5):
                for j in range(5):
                    if board[i][j] == sample:
                        board[i][j] = 0
            if is_winning_board(board):
                unmarked = [number for  line in board for number in line]
                summed = sum(unmarked)
                result = summed * sample
                print(f"{attempt=} {sample=} {result=} {summed=}")
