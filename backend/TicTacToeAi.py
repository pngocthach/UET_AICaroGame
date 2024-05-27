import copy
import random

import requests

AI_URL = "http://localhost:8080"


def get_move(board, size):
    # Find all available positions on the board
    size = int(size)
    available_moves = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == " ":
                available_moves.append((i, j))

    # If there are no available moves, return None
    if not available_moves:
        return None
    # Choose a random available move
    return available_moves[random.randint(0, len(available_moves) - 1)]


def get_move2(new_board, old_board):
    size = len(new_board)

    ## find new move
    row = 0
    col = 0
    for i in range(size):
        for j in range(size):
            if new_board[i][j] != old_board[i][j]:
                row = i
                col = j
                break

    ## send new_move to ai server
    headers = {"Content-Type": "application/json"}
    request_data = {"Row": int(row + 1), "Col": int(col + 1)}
    response = requests.post(AI_URL + "/move", json=request_data, headers=headers)
    print("AI response: ", response.text)
    response_data = response.json()
    return int(response_data["Move"]["Row"]) - 1, int(response_data["Move"]["Col"]) - 1
