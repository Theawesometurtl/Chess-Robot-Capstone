import chess
import chess.engine
import random


engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-android-armv8")
limit = chess.engine.Limit(time=0.1)
board = chess.Board()

def player_move():
    move = input()
    if move == "resign":
        engine.quit()
        return True
    board.push_san(move)
    print(board)
    print()
    return False

def engine_move():
    result = engine.play(board, limit)
    board.push(result.move)
    print(result.move)
    print(board)
    print()

def check_state():
    if board.is_stalemate():
        print("stalemate")
        engine.quit()
        return True
    elif board.is_insufficient_material():
        print("insufficient material")
        engine.quit()
        return True
    elif board.is_fifty_moves():
        print("fifty move rule")
        engine.quit()
        return True
    elif board.is_repitition(3):
        print("threefold repitition")
        engine.quit()
        return True
    elif board.is_checkmate():
        print("checkmate")
        engine.quit()
        return True
    return False
    
def terminal_game():
    print("Do you want to play black, white, or random")
    while True:
        player_colour = input()
        if player_colour == "random":
            player_colour = random.choice(["white","black"])
            print(player_colour)
        if player_colour == "white":
            PB = False
            break
        elif player_colour == "black":
            PB = True
            break
        else:
            print("invalid input")
print(board)
print()
if PB:
    engine_move()

while True:
    try:
        if player_move():
            break

        if check_state():
            break
        
        engine_move()

        if check_state():
            break

    except:
        print("wrong notation try again")



def get_engine_move_and_coords(board):


    print(board)
    print()
    move = engine.play(board, limit)
    
    board.push(move.move)
    
    print(board)
    print()
    

