from graphics import Canvas

def create_cloud(canvas, cloud_height, starting_x, starting_y):
    no_of_cloud_layers = 8
    block_size = cloud_height / no_of_cloud_layers
    outline_size = block_size * 0.4   # thinner drawn size (tweak 0.2 - 0.5 to taste)
    # cloud width = 12 * block_size (width:height ratio = 12:8 = 1.5)

    cloud_parts = []

    cloud_parts.append(canvas.create_rectangle(starting_x + 4 * block_size, starting_y, starting_x + 7 * block_size, starting_y + outline_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x + 2 * block_size, starting_y + 1 * block_size, starting_x + 4 * block_size, starting_y + 1 * block_size + outline_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x + 7 * block_size, starting_y + 1 * block_size, starting_x + 9 * block_size, starting_y + 1 * block_size + outline_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x + 1 * block_size, starting_y + 2 * block_size, starting_x + 1 * block_size + outline_size, starting_y + 3 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x + 10 * block_size - outline_size, starting_y + 2 * block_size, starting_x + 10 * block_size, starting_y + 3 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x + 1 * block_size, starting_y + 3 * block_size, starting_x + 1 * block_size + outline_size, starting_y + 4 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x + 10 * block_size - outline_size, starting_y + 3 * block_size, starting_x + 10 * block_size, starting_y + 4 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x, starting_y + 4 * block_size, starting_x + outline_size, starting_y + 5 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x + 12 * block_size - outline_size, starting_y + 4 * block_size, starting_x + 12 * block_size, starting_y + 5 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x, starting_y + 5 * block_size, starting_x + outline_size, starting_y + 6 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x + 12 * block_size - outline_size, starting_y + 5 * block_size, starting_x + 12 * block_size, starting_y + 6 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x, starting_y + 6 * block_size, starting_x + outline_size, starting_y + 7 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x + 12 * block_size - outline_size, starting_y + 6 * block_size, starting_x + 12 * block_size, starting_y + 7 * block_size, '#535353', '#535353'))
    cloud_parts.append(canvas.create_rectangle(starting_x, starting_y + 7 * block_size, starting_x + 12 * block_size, starting_y + 8 * block_size - (block_size - outline_size), '#535353', '#535353'))

    return cloud_parts

def main():
    canvas = Canvas(800, 400)

    cloud1 = create_cloud(canvas, 80, 100, 150)


if __name__ == '__main__':
    main()