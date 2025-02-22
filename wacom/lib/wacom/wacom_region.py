import subprocess
import os

screen_w = 2560
screen_h = 1440


class Region:
    def __init__(self):
        self.percentage = 100

    def toggle(self):
        percentage = 50 if self.percentage == 100 else 100
        print("toggling to ", percentage)

        region_w = screen_w * percentage // 100
        region_h = screen_h * percentage // 100

        offset_x = (screen_w - region_w) // 2
        offset_y = (screen_h - region_h) // 2

        spec = f"{region_w}x{region_h}+{offset_x}+{offset_y}"

        subprocess.check_call(
            ["xsetwacom", "set", "Wacom Intuos Pro S Pen stylus", "MapToOutput", spec]
        )
        self.percentage = percentage
        return True
