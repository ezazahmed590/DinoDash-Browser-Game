def duplicate_shapes(canvas, shape_list, color):
    new_list = []
    for shape_id in shape_list:
        coords = canvas.coords(shape_id)
        print(coords)  # debug — check what this actually looks like
        new_id = canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], color, color)
        new_list.append(new_id)
    return new_list