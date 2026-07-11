from graphics import Canvas
import time


def short_jump(canvas, shape_list, jump_height, jump_delay):
    
    space_in_loop = 0

    for i in range(int(jump_height/10)):
        space_in_loop = canvas.get_last_key_press()
        if space_in_loop == "SPACE":
            break
        for n in range(len(shape_list)):
            x = canvas.get_left_x(shape_list[n])
            y = canvas.get_top_y(shape_list[n])
            canvas.moveto(shape_list[n], x, (y- 10))
        time.sleep(jump_delay)
    
    for i in range(int(jump_height/10)):
        if space_in_loop == "SPACE":
            break
        space_in_loop= canvas.get_last_key_press()
        if space_in_loop == "SPACE":
            break
            
        for n in range(len(shape_list)):
            x = canvas.get_left_x(shape_list[n])
            y = canvas.get_top_y(shape_list[n])
            canvas.moveto(shape_list[n], x, (y+ 10))
        time.sleep(jump_delay)

    return space_in_loop


def high_jump(canvas, shape_list, jump_height, shape_height, road_position, jump_delay):

    new_shape = []

    for i in range(int(jump_height/10)):
        for n in range(len(shape_list)):
            x = canvas.get_left_x(shape_list[n])
            y = canvas.get_top_y(shape_list[n])
            canvas.moveto(shape_list[n], x, (y- 10))
            new_shape.append(shape_list[n])
        time.sleep(jump_delay)
    
    dino_head = canvas.get_top_y(new_shape[len(new_shape)-1])
    h = road_position - dino_head - shape_height

    for i in range(int(h/10)):
        for n in range(len(new_shape)):
            x = canvas.get_left_x(new_shape[n])
            y = canvas.get_top_y(new_shape[n])
            canvas.moveto(new_shape[n], x, (y+ 10))
        time.sleep(jump_delay)

    return [h, dino_head, shape_height, len(range(int(h/10)))]

    
