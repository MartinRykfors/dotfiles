import subprocess
import os

screen_w = 2560
screen_h = 1440


class Region:
    def __init__(self):
        self.percentage = 100
        self.outline_proc = None
        print("instantiating region")

    def toggle(self):
        if self.outline_proc is not None:
            self.outline_proc.terminate()
            self.outline_proc = None

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
        if percentage != 100:
            if self.outline_proc is None:
                print("starting outliner")
                self.outline_proc = subprocess.Popen(
                    ["uv", "run", "--with", 'ewmh', "/home/rykarn/lib/wacom/wacom_overlay.py", spec]
                )
                print("outliner running", self.outline_proc.pid)

        self.percentage = percentage
        return True
