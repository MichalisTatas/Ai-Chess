import sys

import chess

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5 import *

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
                            # print(self.board.pieces(piece_type=1,color=True))
                            # m=0
                            # for i in self.board.pieces(piece_type=1,color=True):
                            #     if i == 1:
                            #         m=m+1
                            # print(m)
                            self.playerMove()
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

    def minimax(self, depth, player, a, b):              
        # minimax algorithm with alpha beta pruning
        #black is maximizing player

        #minimax problem successor is move and not state
        #fix this and then evaluation function

        if depth == 0:
            return self.evaluationFunction(player)

        if player == 'ai' :
            maxEvaluation = -float("inf")
            for successor in self.board.legal_moves:
                b = self.board.san(successor)
                evaluation = minimax(b, depth, 'human', a, b)
                maxEvaluation = max(maxEvaluation, evaluation)
                a = max(a, maxEvaluation)
                if b < a:
                    return maxEvaluation
            return maxEvaluation

        else: 
            minEvaluation = float("inf")
            for successor in self.board.legal_moves:
                b = self.board.san(successor)
                evaluation = minimax(b, depth-1, 'ai', a, b)
                minEvaluation = min(minEvaluation, evaluation)
                b = min(b, minEvaluation)
                if b < a:
                    return minEvaluation
            return minEvaluation

    def playerMove(self):
        # print(self.board.pseudo_legal_moves)
        a = -float("inf")
        b = float("inf")
        bestScore = -float("inf")
        
        for successor in self.board.legal_moves:
            b = self.board.san(successor)
            score = minimax(b, 3, 'human', a, b)
            if score > bestScore:
                bestScore = score
                bestMove = successor
            a = max(a, bestScore)
        move = chess.Move.from_uci(bestMove)
        


    def evaluationFunction(self, player):
    #     #simple evaluation functon for start 
    #     # takes into consideration only pieces value
        if player == 'human':   #white for the time being
            return 5
        else :        #ai so black pieces for the time being
            return 5




if __name__ == "__main__":
    chessGui = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(chessGui.exec_())