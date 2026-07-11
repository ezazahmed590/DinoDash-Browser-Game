from graphics import Canvas
from dinosaur import create_dinosaur
from road import create_road
from cactus import create_cactus
from scorecard import create_scorecard
from new_jump import short_jump
from new_jump import high_jump
import time
from cloud import create_cloud
import random
from duplicate_shape import duplicate_shapes

# ============================================================
#                    GAME CONTROL CONSTANTS
# ============================================================

# ---- Canvas & Dino size ----
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 400
DINO_HEIGHT = CANVAS_HEIGHT * 0.15

# ---- Dino Position ----
dino_position_x = 150

# ---- Play variables ----
JUMP_HEIGHT = 70
JUMP_TIME = 0.05
ROAD_POSITION = 300
BG_MVT_SPEED = 0.05

# ---- Positional controls of cactus ----
MIN_DIFF_CACTUS = 0.4 * CANVAS_WIDTH
MAX_RANGE = 0.2 * CANVAS_WIDTH
INT_CACTUS_HEIGHT_1 = 0.18 * CANVAS_HEIGHT
INT_CACTUS_HEIGHT_2 = 0.12 * CANVAS_HEIGHT

# ---- Cloud controls ----
CLOUD_HEIGHT = 0.1 * CANVAS_HEIGHT
CLOUD_WIDTH = 1.5 * CLOUD_HEIGHT
MIN_DIFF_CLOUD = (CANVAS_WIDTH - 3 * CLOUD_WIDTH) / 4
CLOUD_LEVEL = ROAD_POSITION - DINO_HEIGHT - 2 * JUMP_HEIGHT - CLOUD_HEIGHT
MAX_RANGE_CLOUD = 0.2 * CANVAS_WIDTH

# ---- Score variables ----
SCORE_X = 370
SCORE_Y = 30
SCR_HEIGHT = 70
SCR_WIDTH = 400

# ---- "Game Over" variables ----
GAME_OVER_X = 30
GAME_OVER_Y = SCORE_Y
GM_OVR_HEIGHT = 60
GM_OVR_WIDTH = 280

# ============================================================
#                         GAME CODE
# ============================================================

def main():

    # ---------- SETUP: canvas & dino ----------
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Give the window keyboard focus so SPACE presses register when running
    # locally. (Harmless on the Code in Place IDE.) If this line ever errors on
    # your setup, delete it and just click the game window once before playing.
    try:
        canvas.focus_set()
    except Exception:
        pass

    dino = create_dinosaur(canvas, DINO_HEIGHT, dino_position_x, ROAD_POSITION - DINO_HEIGHT - 1)

    # ---------- SETUP: road ----------
    road_1 = create_road(canvas, CANVAS_HEIGHT, CANVAS_WIDTH, 0.02, 0, ROAD_POSITION)
    road_2 = create_road(canvas, CANVAS_HEIGHT, CANVAS_WIDTH, 0.02, CANVAS_WIDTH, ROAD_POSITION)

    # ---------- SETUP: cactus positioning ----------
    cactus_1_position = CANVAS_WIDTH + 20 +random.randint(0, int(MAX_RANGE/10))*10
    cactus_2_position = cactus_1_position + MIN_DIFF_CACTUS + random.randint(0, int(MAX_RANGE/10))*10

    if random.randint(0,1) == 0:
        CACTUS_HEIGHT_1 = INT_CACTUS_HEIGHT_1
        CACTUS_HEIGHT_2 = INT_CACTUS_HEIGHT_2
    else:
        CACTUS_HEIGHT_1 = INT_CACTUS_HEIGHT_2
        CACTUS_HEIGHT_2 = INT_CACTUS_HEIGHT_1

    cactus_1 = create_cactus(canvas, CACTUS_HEIGHT_1, cactus_1_position, ROAD_POSITION - CACTUS_HEIGHT_1)
    cactus_2 = create_cactus(canvas, CACTUS_HEIGHT_2, cactus_2_position, ROAD_POSITION - CACTUS_HEIGHT_2)
    cactus_3 = create_cactus(canvas, CACTUS_HEIGHT_1, cactus_1_position, ROAD_POSITION - CACTUS_HEIGHT_1)
    cactus_4 = create_cactus(canvas, CACTUS_HEIGHT_2, cactus_2_position, ROAD_POSITION - CACTUS_HEIGHT_2)

    # ---------- SETUP: cloud positioning ----------
    cloud_1_position = CANVAS_WIDTH + 20 + random.randint(0, int(MAX_RANGE_CLOUD/10))*10
    cloud_2_position = cloud_1_position + MIN_DIFF_CLOUD + random.randint(0, int(MAX_RANGE_CLOUD/10))*10
    cloud_3_position = cloud_2_position + MIN_DIFF_CLOUD + random.randint(0, int(MAX_RANGE_CLOUD/10))*10

    cloud_1 = create_cloud(canvas, CLOUD_HEIGHT, cloud_1_position, CLOUD_LEVEL)
    cloud_2 = create_cloud(canvas, CLOUD_HEIGHT, cloud_2_position, CLOUD_LEVEL)
    cloud_3 = create_cloud(canvas, CLOUD_HEIGHT, cloud_3_position, CLOUD_LEVEL)
    cloud_4 = create_cloud(canvas, CLOUD_HEIGHT, cloud_1_position, CLOUD_LEVEL)
    cloud_5 = create_cloud(canvas, CLOUD_HEIGHT, cloud_2_position, CLOUD_LEVEL)
    cloud_6 = create_cloud(canvas, CLOUD_HEIGHT, cloud_2_position, CLOUD_LEVEL)

    # ---------- SETUP: score initiation ----------
    score = 0
    canvas.create_rectangle(SCORE_X, SCORE_Y, SCORE_X + SCR_WIDTH, SCORE_Y + SCR_HEIGHT, "white")
    score_shape = create_scorecard(canvas, SCORE_X, SCORE_Y, f"SCORE: {score:06}", 40, "black")

    # ---------- SETUP: jump state machine ----------
    # states: "grounded", "short_up", "short_down", "long_up", "long_down"
    jump_state = "grounded"
    jump_step = 0
    short_jump_steps = int(JUMP_HEIGHT / 10)
    long_jump_extra_steps = int(JUMP_HEIGHT / 10)   # extra height for high_jump's "up" phase
    long_jump_down_steps = 0                        # computed dynamically once long_up finishes
    dino_shape_height = CANVAS_HEIGHT * 0.15

    # ---------- SETUP: timing ----------
    last_bg_update = time.time()
    last_jump_update = time.time()
    FRAME_TIME = min(BG_MVT_SPEED, JUMP_TIME)

    # Paint the first frame and pause briefly so you can see the starting scene
    # and click the window / get ready before the action begins.
    canvas.update()
    time.sleep(1)

    # ---------- GAME LOOP ----------
    while True:
        now = time.time()

        # ---------- BACKGROUND MOVEMENT ----------
        if now - last_bg_update >= BG_MVT_SPEED:
            last_bg_update = now

            if canvas.get_left_x(road_1[0]) == -CANVAS_WIDTH:
                # recycle road
                road_1 = road_2
                road_2 = create_road(canvas, CANVAS_HEIGHT, CANVAS_WIDTH, 0.02, CANVAS_WIDTH, ROAD_POSITION)

                # recycle cacti
                for i in range(len(cactus_1)):
                    canvas.delete(cactus_1[i])
                    canvas.delete(cactus_2[i])

                cactus_1 = cactus_3
                cactus_2 = cactus_4

                cactus_1_position = CANVAS_WIDTH + random.randint(0, int(MAX_RANGE/10))*10
                cactus_2_position = cactus_1_position + MIN_DIFF_CACTUS + random.randint(0, int(MAX_RANGE/10))*10

                if random.randint(0,1) == 0:
                    CACTUS_HEIGHT_1 = INT_CACTUS_HEIGHT_1
                    CACTUS_HEIGHT_2 = INT_CACTUS_HEIGHT_2
                else:
                    CACTUS_HEIGHT_1 = INT_CACTUS_HEIGHT_2
                    CACTUS_HEIGHT_2 = INT_CACTUS_HEIGHT_1

                cactus_3 = create_cactus(canvas, CACTUS_HEIGHT_1, cactus_1_position, ROAD_POSITION - CACTUS_HEIGHT_1)
                cactus_4 = create_cactus(canvas, CACTUS_HEIGHT_2, cactus_2_position, ROAD_POSITION - CACTUS_HEIGHT_2)

                # recycle clouds
                for i in range(len(cloud_1)):
                    canvas.delete(cloud_1[i])
                    canvas.delete(cloud_2[i])
                    canvas.delete(cloud_3[i])

                cloud_1 = cloud_4
                cloud_2 = cloud_5
                cloud_3 = cloud_6

                cloud_1_position = CANVAS_WIDTH + random.randint(0, int(MAX_RANGE_CLOUD/10))*10
                cloud_2_position = cloud_1_position + MIN_DIFF_CLOUD + random.randint(0, int(MAX_RANGE_CLOUD/10))*10
                cloud_3_position = cloud_2_position + MIN_DIFF_CLOUD + random.randint(0, int(MAX_RANGE_CLOUD/10))*10

                cloud_4 = create_cloud(canvas, CLOUD_HEIGHT, cloud_1_position, CLOUD_LEVEL)
                cloud_5 = create_cloud(canvas, CLOUD_HEIGHT, cloud_2_position, CLOUD_LEVEL)
                cloud_6 = create_cloud(canvas, CLOUD_HEIGHT, cloud_3_position, CLOUD_LEVEL)

                # score bg stays in front of the clouds, so the clouds don't mess (visually) with the scorecard.
                canvas.create_rectangle(SCORE_X, SCORE_Y, (SCORE_X + SCR_WIDTH), (SCORE_Y + SCR_HEIGHT), "white")
                score_shape = create_scorecard(canvas, SCORE_X, SCORE_Y, f"SCORE: {score:06}", 40, "black")
                ##

            # scroll road
            for i in range(len(road_1)):
                canvas.moveto(road_1[i], canvas.get_left_x(road_1[i]) - 10, canvas.get_top_y(road_1[i]))
                canvas.moveto(road_2[i], canvas.get_left_x(road_2[i]) - 10, canvas.get_top_y(road_2[i]))

            # scroll cacti
            for i in range(len(cactus_1)):
                canvas.moveto(cactus_1[i], canvas.get_left_x(cactus_1[i]) - 10, canvas.get_top_y(cactus_1[i]))
                canvas.moveto(cactus_2[i], canvas.get_left_x(cactus_2[i]) - 10, canvas.get_top_y(cactus_2[i]))
                canvas.moveto(cactus_3[i], canvas.get_left_x(cactus_3[i]) - 10, canvas.get_top_y(cactus_3[i]))
                canvas.moveto(cactus_4[i], canvas.get_left_x(cactus_4[i]) - 10, canvas.get_top_y(cactus_4[i]))

            # scroll clouds
            for i in range(len(cloud_1)):
                canvas.moveto(cloud_1[i], canvas.get_left_x(cloud_1[i]) - 10, canvas.get_top_y(cloud_1[i]))
                canvas.moveto(cloud_2[i], canvas.get_left_x(cloud_2[i]) - 10, canvas.get_top_y(cloud_2[i]))
                canvas.moveto(cloud_3[i], canvas.get_left_x(cloud_3[i]) - 10, canvas.get_top_y(cloud_3[i]))
                canvas.moveto(cloud_4[i], canvas.get_left_x(cloud_4[i]) - 10, canvas.get_top_y(cloud_4[i]))
                canvas.moveto(cloud_5[i], canvas.get_left_x(cloud_5[i]) - 10, canvas.get_top_y(cloud_5[i]))
                canvas.moveto(cloud_6[i], canvas.get_left_x(cloud_6[i]) - 10, canvas.get_top_y(cloud_6[i]))

        # ---------- DINO JUMP STATE MACHINE ----------
        if now - last_jump_update >= JUMP_TIME:
            last_jump_update = now
            key = canvas.get_last_key_press()

            if jump_state == "grounded":
                if key == "SPACE":
                    jump_state = "short_up"
                    jump_step = 0

            elif jump_state == "short_up":
                if key == "SPACE":
                    # SPACE pressed again mid-way up -> this becomes a long jump
                    jump_state = "long_up"
                    jump_step = 0
                else:
                    for n in range(len(dino)):
                        x = canvas.get_left_x(dino[n])
                        y = canvas.get_top_y(dino[n])
                        canvas.moveto(dino[n], x, y - 10)
                    jump_step += 1
                    if jump_step >= short_jump_steps:
                        jump_state = "short_down"
                        jump_step = 0

            elif jump_state == "short_down":
                if key == "SPACE":
                    # SPACE pressed again while coming down -> also becomes a long jump
                    jump_state = "long_up"
                    jump_step = 0
                else:
                    for n in range(len(dino)):
                        x = canvas.get_left_x(dino[n])
                        y = canvas.get_top_y(dino[n])
                        canvas.moveto(dino[n], x, y + 10)
                    jump_step += 1
                    if jump_step >= short_jump_steps:
                        jump_state = "grounded"
                        jump_step = 0

            elif jump_state == "long_up":
                for n in range(len(dino)):
                    x = canvas.get_left_x(dino[n])
                    y = canvas.get_top_y(dino[n])
                    canvas.moveto(dino[n], x, y - 10)
                jump_step += 1
                if jump_step >= long_jump_extra_steps:
                    # compute how far down we now need to go to reach the road
                    dino_head = canvas.get_top_y(dino[0])
                    target_top = ROAD_POSITION - dino_shape_height
                    h = target_top - dino_head
                    long_jump_down_steps = max(int(h / 10), 0)
                    jump_state = "long_down"
                    jump_step = 0

            elif jump_state == "long_down":
                if jump_step < long_jump_down_steps:
                    for n in range(len(dino)):
                        x = canvas.get_left_x(dino[n])
                        y = canvas.get_top_y(dino[n])
                        canvas.moveto(dino[n], x, y + 10)
                    jump_step += 1
                else:
                    # snap exactly to road level to fix rounding leftover
                    target_top = ROAD_POSITION - dino_shape_height
                    current_top = canvas.get_top_y(dino[0])
                    leftover = target_top - current_top
                    if leftover != 0:
                        for n in range(len(dino)):
                            x = canvas.get_left_x(dino[n])
                            y = canvas.get_top_y(dino[n])
                            canvas.moveto(dino[n], x, y + leftover)
                    jump_state = "grounded"
                    jump_step = 0

        time.sleep(FRAME_TIME)

        # ---------- COLLISION CHECK ----------
        ol_left_x = canvas.get_left_x(dino[98])
        ol_top_y = canvas.get_top_y(dino[0])
        ol_right_x = canvas.get_left_x(dino[17])
        ol_bottom_y = canvas.get_top_y(dino[166])

        overlap_check = canvas.find_overlapping(ol_left_x, ol_top_y, ol_right_x, ol_bottom_y)

        if len(overlap_check) > 167:
            canvas.create_rectangle(GAME_OVER_X, GAME_OVER_Y, GAME_OVER_X + GM_OVR_WIDTH, GAME_OVER_Y + GM_OVR_HEIGHT, "white")
            canvas.create_text(GAME_OVER_X, GAME_OVER_Y, "GAME OVER!", "Space Mono", 40, "black")
            print("Game Over!!!")
            break

        # ---------- SCORE CHANGE ----------
        score += 1
        if score > 100000:
            canvas.change_text(score_shape, "WINNER!")
            break
        else:
            canvas.change_text(score_shape, f"SCORE: {score:06}")

        # Repaint the window so all the movement above becomes visible. Without
        # this, the canvas stays blank when running locally (the Code in Place
        # IDE refreshes automatically, but a plain Tkinter window does not).
        canvas.update()

if __name__ == '__main__':
    main()