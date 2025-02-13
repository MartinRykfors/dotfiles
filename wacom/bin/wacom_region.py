#!/usr/bin/python

import subprocess
import os

screen_w = 2560
screen_h = 1440


# TODO: ensure that the directory and file exists
def read_current_percentage():
    filepath = os.path.expanduser(
        os.path.join("~", ".local", "state", "wacom", "region")
    )
    with open(filepath, "r") as f:
        return int(f.readline())


def write_current_percentage(percentage):
    filepath = os.path.expanduser(
        os.path.join("~", ".local", "state", "wacom", "region")
    )
    with open(filepath, "w") as f:
        f.write(str(percentage))


percentage = read_current_percentage()
percentage = 50 if percentage == 100 else 100

region_w = screen_w * percentage // 100
region_h = screen_h * percentage // 100

offset_x = (screen_w - region_w) // 2
offset_y = (screen_h - region_h) // 2

spec = f"{region_w}x{region_h}+{offset_x}+{offset_y}"

subprocess.check_call(
    ["xsetwacom", "set", "Wacom Intuos Pro S Pen stylus", "MapToOutput", spec]
)

write_current_percentage(percentage)
