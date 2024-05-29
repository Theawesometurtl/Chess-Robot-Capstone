import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-android-armv8")
limit = chess.engine.Limit(time=0.001)
board = chess.Board()
result = engine.play(board, limit)

print(board)
print()

while True:
    try:
        x = input()
        if x == "stop":
            engine.quit()
            break
        board.push_san(x)
        print(board)
        print()
        result = engine.play(board, limit)
        board.push(result.move)
        print(result.move)
        print(board)
        print()
    except:
        print("wrong notation try again")