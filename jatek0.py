#!/usr/bin/env python3
# -*- coding: utf8 -*-
import curses
from time import sleep

COLUMNS = 48
ROWS = 15
MIN_X = 5
MAX_X = MIN_X + COLUMNS + 1
MIN_Y = 5
MAX_Y = MIN_Y + ROWS + 1
TITLE_X = MIN_X + 8
TITLE_Y = MIN_Y - 2

FILL = " "


def run():
    # curses inicializálása
    screen = curses.initscr()
    screen.keypad(True)  # Így a curses által felismerhető kódokat ad vissza a billentyűzet,
    # nem ESC szekvenciákat (például kurzormozgató billentyűk esetében)
    screen.nodelay(True)
    curses.noecho()
    curses.cbreak(True)

    # Játék területének inicializálása
    screen.addstr(MIN_Y, MIN_X, "*" + "*" * COLUMNS + "*")
    for i in range(1, ROWS + 1):
        screen.addstr(MIN_Y + i, MIN_X, "*" + FILL * COLUMNS + "*")
    screen.addstr(MAX_Y, MIN_X, "*" + "*" * COLUMNS + "*")
    screen.addstr(TITLE_Y, TITLE_X, "Próbálj a négyszögön belül maradni!")

    # Maga a "játék"
    pressed_key = None
    cur_x = MIN_X + int(COLUMNS / 2)
    cur_y = MIN_Y + int(ROWS / 2)
    direction_x, direction_y = 0, 0

    while pressed_key != curses.KEY_END:
        screen.addch(cur_y, cur_x, FILL)
        cur_x += direction_x
        cur_y += direction_y
        screen.addch(cur_y, cur_x, "O")
        if cur_x <= MIN_X or cur_x >= MAX_X or \
                cur_y <= MIN_Y or cur_y >= MAX_Y:
            break

        pressed_key = screen.getch()
        # python 3.10-ig nincs switch/case/stb. szerkezet, ezért muszáj
        # találni valami workaroundot.
        if pressed_key == curses.KEY_DOWN:
            direction_x = 0
            direction_y = 1
            screen.addstr(MAX_Y + 3, MIN_X, "DOWN ")
        elif pressed_key == curses.KEY_UP:
            direction_x = 0
            direction_y = -1
            screen.addstr(MAX_Y + 3, MIN_X, "UP   ")
        elif pressed_key == curses.KEY_LEFT:
            direction_x = -1
            direction_y = 0
            screen.addstr(MAX_Y + 3, MIN_X, "LEFT ")
        elif pressed_key == curses.KEY_RIGHT:
            direction_x = 1
            direction_y = 0
            screen.addstr(MAX_Y + 3, MIN_X, "RIGHT")
        else:
            screen.addstr(MAX_Y + 3, MIN_X, "?????")
        sleep(0.1)

    # Terminál visszaállítása a használatbavétel előtti állapotba
    curses.endwin()


if __name__ == "__main__":
    run()
