level_1_layout = [
    "                                                                                                                      ",
    "                                                                                                                      ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                         ",
    "  P                                                                                                                            ",
    "                                                                                                                                    ",
    "                 xx                      xx                   xxxxx                                                         ",
    "               xxxxxxx                 xxxxxxxx          xxxxxxxxxxxxxxx                        e                      ",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]

level_2_layout = [
    "                                                                                                                      ",
    "                                                                                                                      ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                         ",
    "  P                                                                                                                                                       ",
    "                                                                                                                                                           ",
    "                                                                                                                                                           ",
    "                                                                                                                                                           ",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]

level_3_layout = [
    "                                                                                                                      ",
    "                                                                                                                      ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                         ",
    "  P                                                                                                                                                       ",
    "                                                                                                                                                           ",
    "                                                                                                                                                           ",
    "                                                                                                                                                           ",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]

level_s21_layout = [
    "                                                                                                                      ",
    "                                                                                                                      ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                         ",
    "  P                                                                                                                                                       ",
    "                                                                                                                                                x          ",
    "                                     x                                   xx                      xx                    x                       xx                  ",
    "                                    xx                               xxxxxx                     xxxx                xxxxx                   xxxxx               ",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]

level_s22_layout = [
    "                                                                                                                      ",
    "                                                                                                                      ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                         ",
    "  P                                                                                                                                                       ",
    "                                                                                                                                                           ",
    "                                                                                                                                                           ",
    "                                                                                                                                                           ",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]

level_s23_layout = [
    "                                                                                                                      ",
    "                                                                                                                      ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                                                                                    ",
    "                                                         ",
    "  P                                                                                                                                                       ",
    "                                                                                                                                                           ",
    "                                                                                                                                                           ",
    "                                                                                                                                                           ",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]





level_dict = {
    "level 1" : level_1_layout,
    "level 2" : level_2_layout,
    "level 3" : level_3_layout,
    "level s2-1" : level_2_layout,
    "level s2-2" :  level_2_layout,
    "level s2-3" :  level_3_layout,
}



tile_size = 64
screen_width = 1280
level_rows = len(level_1_layout)
screen_height = tile_size * level_rows


