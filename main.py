import sys

from evaluation import evaluationFunction

import chess
import time
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

# to do : 
# when minimax finds a score > 0 so black is winning
# terminate the funtion so it doesnt search the whole tree
# maybe add iterative deepening to keep the depth of the tree flexible and increase or decrease accordingly
# if use iterative deepening maybe store some results to not evaluate them again
# add null move heuristic

counter=0

def minimax(board, depth, player, a, b):              
    global counter
        # minimax algorithm with alpha beta pruning
        # black is maximizing player
    if depth == 0 or board.is_game_over():
        counter = counter +1
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
        score=minimax(board, 3, 'human', a, b)
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
                            time1=time.time()
                            playerMove(self.board)
                            time2=time.time()
                            print('Ai move took {:.3f} seconds and reached {:d} terminal states'.format((time2-time1),counter))
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







# minimax with a-b pruning about 25 s in average for depth =3 i.e. 2 moves for each player 

# To avoid using the null-move heuristic in zugzwang positions, most chess-playing programs that use the null-move heuristic put restrictions on its use. Such restrictions often include not using the null-move heuristic if
# the side to move is in check
# the side to move has only its king and pawns remaining
# the side to move has a small number of pieces remaining
# the previous move in the search was also a null move.