import math
import chess
import chess.engine

def move_piece(x1: int, y1, x2: int, y2: int):
    home = {x: -5, y: -5}
    lift_claw()
    move_arm(x, y)
    open_claw()
    lower_claw()
    close_claw()
    lift_claw()
    move_arm(x2, y2)
    lower_claw()
    open_claw()
    lift_claw()
    move_claw(home.x, home.y)


flip_num = { 0 : 7, 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 : 2, 6 : 1, 7 : 0}
bot_colour =  "white"

def get_distance_and_angle(square):
    X = ord(square[0]) - 97
    Y = int(square[1]) - 1
    print("coordinates = " + str(X) + "," + str(Y))

    if bot_colour == "black":
        X , Y = flip_num[X] , flip_num[Y]

    rX = X - 3.5
    rY = Y + 1.5 # distance from center of motor to middle of first row of squares (in square size, eg. center of motor right on edge of board = 0.5) (multiple by size of one square later)

    distance = math.sqrt(rX ** 2 + rY ** 2)
    angle = math.degrees(math.atan(rX / rY)) + 90 # from 0 degrees (all the way left) to 180 degrees (all the way right)

    print("distance = " + str(round(distance , 2)) + " squares")
    print("angle = " + str(round(angle , 2)) + " degrees")

def move_motors(move):
    sq1 = move[0] + move[1]
    sq2 = move[2] + move[3]
    Wsq3 = move[2] + str(int(move[3]) - 1)
    Bsq3 = move[2] + str(int(move[3]) + 1)

    if board.is_capture(move):
        if board.is_en_passant(move):
            if turn_colour == "white":
                capture_sq = Wsq3
            else:
                capture_sq = Bsq3
        else:
            capture_sq = sq2
        
        get_distance_and_angle(capture_sq)
        grab_piece(board.piece_at(chess.capture_sq))
        move_to_piece_storage()
        release_piece(board.piece_at(chess.capture_sq))


    get_distance_and_angle(sq1)
    grab_piece(board.piece_at(chess.sq1))
    get_distance_and_angle(sq2)
    release_piece(board.piece_at(chess.sq1))
    defalt_position()

def grab_piece(piece):
    pass

def release_piece(piece):
    pass