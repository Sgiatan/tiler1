from graphics import *
from random import choice
import math
import os

tiles_x = 10
tiles_y = 6
tile_size = 101
dimensions = (100, 100)
tiles = []
os.chdir("tiles")


def tile(path, win, angle=-1):
    for tile in tiles:
        tile.undraw()
        tiles.clear()
    for y in range(tile_size // 2, tiles_y * tile_size, tile_size):
        for x in range(tile_size // 2, tiles_x * tile_size, tile_size):
            img = Image(Point(x, y), path)
            img.angle = choice([0, 90, 180, 270]) if angle == -1 else angle
            img.transform(dimensions=dimensions, angle=img.angle)
            tiles.append(img)
            img.draw(win)


def rotate(point):
    if not point:
        return

    x, y = point.x, point.y
    x = math.floor(x / tile_size)
    y = math.floor(y / tile_size)
    tile_num = tiles_x * y + x

    img = tiles[tile_num]
    img.angle = img.angle - 90 if img.angle != 0 else 270
    img.transform(dimensions=dimensions, angle=img.angle)
    img.redraw()


def main():
    global tiles_x, tiles_y

    win_x = tile_size * tiles_x
    win_y = tile_size * tiles_y
    win = GraphWin("sTile", win_x, win_y)

    prompt_filename = Text(Point(win_x / 2, win_y / 2 - 60), "Enter filename:")
    prompt_filename.draw(win)

    filename_box = Entry(Point(win_x / 2, win_y / 2 - 40), 15)
    filename_box.setFill('gray90')
    filename_box.draw(win)

    # prompt_dim = Text(Point(win_x / 2, win_y / 2 - 20), "Enter dimensions:")
    # prompt_dim.draw(win)

    # x_box = Entry(Point(win_x / 2 - 40, win_y / 2), 5)
    # x_box.setFill('gray90')
    # x_box.draw(win)

    # y_box = Entry(Point(win_x / 2 + 40, win_y / 2), 5)
    # y_box.setFill('gray90')
    # y_box.draw(win)

    image_file = ""

    while win.getKey() != "Return" or image_file not in [x.name for x in os.scandir()] or not tiles_x or not tiles_y:
        image_file = filename_box.getText()
        # entry_x = x_box.getText() if x_box.getText() else 0
        # entry_y = y_box.getText()

    # tiles_x = int(entry_x)
    # tiles_y = int(entry_y)
    # win.width = tiles_x * tile_size
    # win.height = tiles_y * tile_size
    prompt_filename.undraw()

    filename_box.undraw()
    # prompt_dim.undraw()
    # x_box.undraw()
    # y_box.undraw()

    tile(image_file, win)

    while win.checkKey() != "Escape":
        rotate(win.checkMouse())
        key = win.checkKey()
        if key == "r":
            tile(image_file, win)
        elif key in ["0", "1", "2", "3"]:
            tile(image_file, win, int(key) * 90)

    win.close()


main()
