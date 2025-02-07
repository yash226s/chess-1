from engine import Board
from engine_types import Color
from fen_utils import from_fen


def classic_setup(board: Board) -> None:
    from_fen(board, "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")


if __name__ == "__main__":
    board = Board()
    from_fen(board, "7k/N5pp/8/8/2R1r3/8/8/4K3")
    print(board)
    print(board.generate_possible_moves(Color.WHITE))
