from graphics import Canvas
import time


def short_jump(canvas, shape_list, jump_height, jump_delay):

    space_in_loop = 0

    # Going up
    for i in range(int(jump_height / 10)):
        space_in_loop = canvas.get_last_key_press()
        if space_in_loop == "SPACE":
            break
        for n in range(len(shape_list)):
            x = canvas.get_left_x(shape_list[n])
            y = canvas.get_top_y(shape_list[n])
            canvas.moveto(shape_list[n], x, y - 10)
        time.sleep(jump_delay)

    # Going down
    for i in range(int(jump_height / 10)):
        if space_in_loop == "SPACE":
            break
        space_in_loop = canvas.get_last_key_press()
        if space_in_loop == "SPACE":
            break
        for n in range(len(shape_list)):
            x = canvas.get_left_x(shape_list[n])
            y = canvas.get_top_y(shape_list[n])
            canvas.moveto(shape_list[n], x, y + 10)
        time.sleep(jump_delay)

    return space_in_loop


def high_jump(canvas, shape_list, jump_height, shape_height, road_position, jump_delay):

    # Go up by jump_height more from current position
    for i in range(int(jump_height / 10)):
        for n in range(len(shape_list)):
            x = canvas.get_left_x(shape_list[n])
            y = canvas.get_top_y(shape_list[n])
            canvas.moveto(shape_list[n], x, y - 10)
        time.sleep(jump_delay)

    # dino_head = top of the dino = shape_list[0] (first shape = topmost)
    dino_head = canvas.get_top_y(shape_list[0])

    # distance from current dino top to where it should land
    # dino bottom should be at road_position, so dino top should be at road_position - shape_height
    target_top = road_position - shape_height
    h = target_top - dino_head  # total distance to move down

    # Move down in steps of 10
    steps = int(h / 10)
    for i in range(steps):
        for n in range(len(shape_list)):
            x = canvas.get_left_x(shape_list[n])
            y = canvas.get_top_y(shape_list[n])
            canvas.moveto(shape_list[n], x, y + 10)
        time.sleep(jump_delay)

    # Snap exactly to road level to fix any rounding leftover
    current_top = canvas.get_top_y(shape_list[0])
    leftover = target_top - current_top
    if leftover != 0:
        for n in range(len(shape_list)):
            x = canvas.get_left_x(shape_list[n])
            y = canvas.get_top_y(shape_list[n])
            canvas.moveto(shape_list[n], x, y + leftover)