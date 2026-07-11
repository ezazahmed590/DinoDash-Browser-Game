def create_cactus(canvas, cactus_height, starting_x, starting_y):
    no_of_cactus_layers = 16
    block_size = cactus_height / no_of_cactus_layers

    # 23rd shape (index 22) is the left-most block
    # 21st shape (index 20) is one of the right-most blocks

    cactus = []

    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y, starting_x + 6 * block_size, starting_y + 1 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 1 * block_size, starting_x + 6 * block_size, starting_y + 2 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 2 * block_size, starting_x + 6 * block_size, starting_y + 3 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 3 * block_size, starting_x + 6 * block_size, starting_y + 4 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 4 * block_size, starting_x + 6 * block_size, starting_y + 5 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 7 * block_size, starting_y + 4 * block_size, starting_x + 9 * block_size, starting_y + 5 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x, starting_y + 5 * block_size, starting_x + 2 * block_size, starting_y + 6 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 5 * block_size, starting_x + 6 * block_size, starting_y + 6 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 7 * block_size, starting_y + 5 * block_size, starting_x + 9 * block_size, starting_y + 6 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x, starting_y + 6 * block_size, starting_x + 2 * block_size, starting_y + 7 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 6 * block_size, starting_x + 6 * block_size, starting_y + 7 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 7 * block_size, starting_y + 6 * block_size, starting_x + 9 * block_size, starting_y + 7 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x, starting_y + 7 * block_size, starting_x + 2 * block_size, starting_y + 8 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 7 * block_size, starting_x + 6 * block_size, starting_y + 8 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 7 * block_size, starting_y + 7 * block_size, starting_x + 9 * block_size, starting_y + 8 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x, starting_y + 8 * block_size, starting_x + 2 * block_size, starting_y + 9 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 8 * block_size, starting_x + 6 * block_size, starting_y + 9 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 7 * block_size, starting_y + 8 * block_size, starting_x + 9 * block_size, starting_y + 9 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x, starting_y + 9 * block_size, starting_x + 2 * block_size, starting_y + 10 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 9 * block_size, starting_x + 6 * block_size, starting_y + 10 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 7 * block_size, starting_y + 9 * block_size, starting_x + 9 * block_size, starting_y + 10 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x, starting_y + 10 * block_size, starting_x + 8 * block_size, starting_y + 11 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 1 * block_size, starting_y + 11 * block_size, starting_x + 6 * block_size, starting_y + 12 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 12 * block_size, starting_x + 6 * block_size, starting_y + 13 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 13 * block_size, starting_x + 6 * block_size, starting_y + 14 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 14 * block_size, starting_x + 6 * block_size, starting_y + 15 * block_size, '#535353', '#535353'))
    cactus.append(canvas.create_rectangle(starting_x + 3 * block_size, starting_y + 15 * block_size, starting_x + 6 * block_size, starting_y + 16 * block_size, '#535353', '#535353'))

    return cactus