import sys

import chess

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

def evaluationFunction(board, player):
    #     #simple evaluation functon for start 
    #     # takes into consideration only pieces value

    score=0
    for row in range(0,8):
        for column in range(0,8):
            square = chess.square(row, column)
            piece = board.piece_at(square)
            piece =str(piece)
            if piece is not None:
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

def minimax(board, depth, player, a, b):              
        # minimax algorithm with alpha beta pruning
        #black is maximizing player
    if depth == 0 or board.is_game_over():
        return evaluationFunction(board, player)
    if player == 'ai' :
        maxEvaluation = -float("inf")
        for s in list(board.legal_moves):
            board.push(s)
            evaluation = minimax(board, depth - 1, 'human', a, b)
            board.pop()
            maxEvaluation = max(maxEvaluation, evaluation)
            a = max(a, maxEvaluation)
            if b < a:
                return maxEvaluation
        return maxEvaluation
    else:
        minEvaluation = float("inf")
        for s in list(board.legal_moves):
            board.push(s)
            evaluation = minimax(board, depth-1, 'ai', a, b)
            board.pop()
            minEvaluation = min(minEvaluation, evaluation)
            b = min(b, minEvaluation)
            if b < a:
                return minEvaluation
        return minEvaluation

def playerMove(board):
    a = -float("inf")
    b = float("inf")
    bestScore = -float("inf")       

    for s in list(board.legal_moves):
        board.push(s)
        score=minimax(board, 2, 'human', a, b)
        board.pop()
        if score > bestScore:
            bestScore = score
            bestMove = s
        a = max(a, bestScore)
    board.push(bestMove)



class MainWindow(QWidget):
    """
    Create a surface for the chessboard.
    """
    def __init__(self):
        """
        Initialize the chessboard.
        """
        super().__init__()

        self.setWindowTitle("Chess GUI")
        self.setGeometry(300, 300, 800, 800)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 600, 600)

        self.boardSize = min(self.widgetSvg.width(),
                             self.widgetSvg.height())
        self.coordinates = True
        self.margin = 0.05 * self.boardSize if self.coordinates else 0
        self.squareSize = (self.boardSize - 2 * self.margin) / 8.0
        self.pieceToMove = [None, None]

        self.board = chess.Board()
        self.drawBoard()

    @pyqtSlot(QWidget)
    def mousePressEvent(self, event):
        """
        Handle left mouse clicks and enable moving chess pieces by
        clicking on a chess piece and then the target square.

        Moves must be made according to the rules of chess because
        illegal moves are suppressed.
        """
        if event.x() <= self.boardSize and event.y() <= self.boardSize:
            if event.buttons() == Qt.LeftButton:
                if self.margin < event.x() < self.boardSize - self.margin and self.margin < event.y() < self.boardSize - self.margin:
                    file = int((event.x() - self.margin) / self.squareSize)
                    rank = 7 - int((event.y() - self.margin) / self.squareSize)
                    square = chess.square(file, rank) 
                    piece = self.board.piece_at(square)
                    coordinates = "{}{}".format(chr(file + 97), str(rank + 1))
                    if self.pieceToMove[0] is not None:
                        move = chess.Move.from_uci("{}{}".format(self.pieceToMove[1], coordinates))
                        if move in self.board.legal_moves:
                            self.board.push(move)
                            self.setWindowTitle("Ai making move")
                            playerMove(self.board)
                            self.setWindowTitle("Chess GUI")
                        piece = None
                        coordinates = None
                    self.pieceToMove = [piece, coordinates]
                    self.drawBoard()

    def drawBoard(self):
        """
        Draw a chessboard with the starting position and then redraw
        it for every new move.
        """
        self.boardSvg = self.board._repr_svg_().encode("UTF-8")
        self.drawBoardSvg = self.widgetSvg.load(self.boardSvg)

        return self.drawBoardSvg


if __name__ == "__main__":
    chessGui = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(chessGui.exec_())