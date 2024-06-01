import chess
import chess.engine
import random


engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-android-armv8")
limit = chess.engine.Limit(time=0.1)
board = chess.Board()

def engine_move():
    result = engine.play(board, limit)
    board.push(result.move)
    
def check_state():
    if board.is_stalemate():
        print("stalemate")
        engine.quit()
        return True
    elif board.is_insufficient_material():
        print("insufficient material")
        engine.quit()
        return True
    elif board.can_claim_fifty_moves():
        print("fifty move rule")
        engine.quit()
        return True
    elif board.can_claim_threefold_repitition():
        print("threefoldrepitition")
        engine.quit()
        return True
    return False
    



def get_engine_move_and_coords(board):


    print(board)
    print()
    move = engine.play(board, limit)
    
    board.push(move.move)
    
    print(board)
    print()
    

