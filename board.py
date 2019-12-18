import chess
import chess.svg
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def mike():
    board=chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', chess960=True)
    return chess.svg.board(board=board, size=600)

if __name__ == '__main__':
    app.run()