import subprocess

pad_button_map = {
    "top_1": "1",
    "top_2": "2",
    "top_3": "3",
    "center": "11",
    "bottom_1": "8",
    "bottom_2": "9",
    "bottom_3": "10",
}

wheel_map = {
    "wheel_cw": "AbsWheelDown",
    "wheel_ccw": "AbsWheelUp",
}

pen_button_map = {
    "pen_press": "1",
    "pen_lower": "2",
    "pen_upper": "3",
}

default_profile = {
    "pen_press": "1",
    "pen_lower": "3",
    "pen_upper": "2",
    "top_1": "key Control_L",
    "top_2": "key Shift_L",
    "top_3": "0",
    "center": "key +lsuper f12 -lsuper",
    "bottom_1": "0",
    "bottom_2": "key +ctrl +shift z -ctrl -shift",
    "bottom_3": "key +ctrl z -ctrl",
    "wheel_cw": "0",
    "wheel_ccw": "0",
}

blender_profile = {
    "top_3": "key f",
    "bottom_1": "key +shift space -shift",
}

krita_profile = {
    "top_3": "0",
    "bottom_1": "0",
}

profiles = {
    "blender": blender_profile,
    "krita": krita_profile,
}


def set_profile(profile_name):
    profile = default_profile | profiles[profile_name]
    set_pad_buttons(profile)
    set_pen_buttons(profile)
    set_wheel(profile)
    set_pressure_curve(0,0,100,100)


def set_pressure_curve(a, b, c, d):
    subprocess.check_call(
        [
            "xsetwacom",
            "set",
            "Wacom Intuos Pro S Pen stylus",
            "PressureCurve",
            a,
            b,
            c,
            d,
        ]
    )


def set_wheel(profile):
    for wheel_action in wheel_map.keys():
        subprocess.check_call(
            [
                "xsetwacom",
                "set",
                "Wacom Intuos Pro S Pad pad",
                wheel_map[wheel_action],
                profile[wheel_action],
            ]
        )


def set_pad_buttons(profile):
    for pad_action in pad_button_map.keys():
        subprocess.check_call(
            [
                "xsetwacom",
                "set",
                "Wacom Intuos Pro S Pad pad",
                "Button",
                pad_button_map[pad_action],
                profile[pad_action],
            ]
        )


def set_pen_buttons(profile):
    for pen_action in pen_button_map.keys():
        subprocess.check_call(
            [
                "xsetwacom",
                "set",
                "Wacom Intuos Pro S Pen stylus",
                "Button",
                pen_button_map[pen_action],
                profile[pen_action],
            ]
        )
