import chess
letter_to_number = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}

def board_to_robot_coordinate(board, is_white, is_capture, ):
    moves_list = board.move_stack
    move = moves_list[-1]
    p1 = chess.square_name(move.from_square)
    p2 = chess.square_name(move.to_square)
    p1_coords = position_to_coordinate(p1, is_white)
    p2_coords = position_to_coordinate(p2, is_white)
    return [p1_coords, p2_coords]

def position_to_coordinate(square: str, is_white: bool) -> list[int]:
    character_string = list(square)
    x = int(letter_to_number.character_string[0])
    y = int(character_string[0])-1
    if not is_white:
        x = (x-7)*-1
        y = (y-7)*-1
    return [x, y]

    #https://stackoverflow.com/questions/61778579/what-is-the-best-way-to-find-out-if-the-move-captured-a-piece-in-python-chess
def captured_piece(board, move):
    if board.is_capture(move):
        if board.is_en_passant(move):
            return chess.PAWN
        else:
            return board.piece_at(move.to_square).piece_type
    return 0