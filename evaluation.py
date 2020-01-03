import chess

def evaluationFunction(board, player):
    #     #simple evaluation functon for start 
    #     # takes into consideration only pieces value
    return PiecesValue(board)


def PiecesValue(board):
    score=0
    for row in range(0,8):
        for column in range(0,8):
            square = chess.square(row, column)
            piece = board.piece_at(square)
            piece =str(piece)
            if piece is not None:

                #white pieces
                if piece == 'P':
                    score = score - 1
                elif piece == 'N':
                    score = score - 2
                elif piece == 'B':
                    score = score - 3
                elif piece == 'R':
                    score = score - 4
                elif piece == 'Q':
                    score = score - 5
                elif piece == 'K':
                    score = score - 6

                # black pieces
                elif piece == 'p':
                    score = score + 1
                elif piece == 'n':
                    score = score + 2
                elif piece == 'b':
                    score = score + 3
                elif piece == 'r':
                    score = score + 4
                elif piece == 'q':
                    score = score + 5
                elif piece == 'k':
                    score = score + 6
    return score
