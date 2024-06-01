import math

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


def get_distance_and_angle(square, bot_colour):
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

get_distance_and_angle("a1" , "black")