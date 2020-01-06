import chess

def evaluationFunction(board, player):
    #     #simple evaluation functon for start 
    #     # takes into consideration only pieces value
    return PiecesValue(board)

def PiecesValue(board):
    score=0
    for column in range(0,8):
        for row in range(0,8):
            square = chess.square(column, row)
            piece = board.piece_at(square)
            piece =str(piece)

            if piece is not None:

                #white pieces
                if piece == 'P':
                    score = score - 100   - P[row*8 + column]
                elif piece == 'N':
                    score = score - 320   - N[row*8 + column]
                elif piece == 'B':
                    score = score - 330   - B[row*8 + column]
                elif piece == 'R':
                    score = score - 500   - R[row*8 + column]
                elif piece == 'Q':
                    score = score - 900   - Q[row*8 + column]
                elif piece == 'K':
                    score = score - 20000 - K[row*8 + column]

                # black pieces
                elif piece == 'p':
                    score = score + 100   + P[(7-row)*8 + 7 - column]
                elif piece == 'n':
                    score = score + 320   + N[(7-row)*8 + 7 - column]
                elif piece == 'b':
                    score = score + 330   + B[(7-row)*8 + 7 - column]
                elif piece == 'r':
                    score = score + 500   + R[(7-row)*8 + 7 - column]
                elif piece == 'q':
                    score = score + 900   + Q[(7-row)*8 + 7 - column]
                elif piece == 'k':
                    score = score + 20000 + K[(7-row)*8 + 7 - column]
    return score


# WHITE PIECES
P = [
    0,  0 ,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5,  5 , 10, 25, 25, 10,  5,  5,
    0,  0 ,  0, 20, 20,  0,  0,  0,
    5, -5 ,-10,  0,  0,-10, -5,  5,
    5, 10 , 10,-20,-20, 10, 10,  5,
    0,  0 ,  0,  0,  0,  0,  0,  0
]

N = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50
]

B = [
    -20,-10,-10,-10,-10,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -20,-10,-10,-10,-10,-10,-10,-20,
]

R = [
     0,  0,  0,  0,  0,  0,  0,  0,
     5, 10, 10, 10, 10, 10, 10,  5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
     0,  0,  0,  5,  5,  0,  0,  0
]

Q = [
    -20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5,  5,  5,  5,  0,-10,
    -5,   0,  5,  5,  5,  5,  0, -5,
     0,   0,  5,  5,  5,  5,  0, -5,
    -10,  5,  5,  5,  5,  5,  0,-10,
    -10,  0,  5,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20
]

K = [
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -20,-30,-30,-40,-40,-30,-30,-20,
    -10,-20,-20,-20,-20,-20,-20,-10,
     20, 20,  0,  0,  0,  0, 20, 20,
     20, 30, 10,  0,  0, 10, 30, 20
]
