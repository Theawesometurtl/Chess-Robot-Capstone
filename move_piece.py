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
