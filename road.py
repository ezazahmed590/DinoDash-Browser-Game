from graphics import Canvas

def create_road(canvas, canvas_height, canvas_width, percent_height, starting_x, starting_y):
    road_height = percent_height * canvas_height
    no_of_road_layers = 8
    block_size = road_height / no_of_road_layers

    road = []

    # Width of a single road segment, derived from the image's own proportions
    no_of_road_blocks_wide = 108  # 13.5 * 8 layers
    segment_width = no_of_road_blocks_wide * block_size

    # Dash marks: each dash is 4 blocks wide, 1 block tall, positioned within each segment
    dash_width = 4 * block_size
    dash_height = block_size
    dash_y_offset = 6 * block_size
    dash_x_fractions = [0.19, 0.56, 0.92]

    # Repeat the road segment side by side until canvas_width is covered
    no_of_segments = int(canvas_width // segment_width) + 1

    for s in range(no_of_segments):
        segment_x = starting_x + s * segment_width

        # Main horizontal road line for this segment, 1 block thick (top layer)
        road.append(canvas.create_rectangle(segment_x, starting_y, segment_x + segment_width, starting_y + block_size, 'black', 'black'))

        # Dash marks below the main line
        dash_y = starting_y + dash_y_offset
        for frac in dash_x_fractions:
            dash_x = segment_x + frac * segment_width
            road.append(canvas.create_rectangle(dash_x, dash_y, dash_x + dash_width, dash_y + dash_height, 'black', 'black'))

    return road