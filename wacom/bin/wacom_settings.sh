#! /bin/sh

# Make the output max out at slightly lower physical pressures
xsetwacom set "Wacom Intuos Pro S Pen stylus" PressureCurve 58 53 44 100
# xsetwacom set "Wacom Intuos Pro S Pen stylus" Button 1 key "a"
xsetwacom set "Wacom Intuos Pro S Pen stylus" Button 1 1
xsetwacom set "Wacom Intuos Pro S Pen stylus" Button 2 3
xsetwacom set "Wacom Intuos Pro S Pen stylus" Button 3 2


xsetwacom set "Wacom Intuos Pro S Pad pad" Button 1 key "Control_L"
xsetwacom set "Wacom Intuos Pro S Pad pad" Button 2 key "Shift_L"
xsetwacom set "Wacom Intuos Pro S Pad pad" Button 3 key "key f"

# Center round button
xsetwacom set "Wacom Intuos Pro S Pad pad" Button 11 2
# wheel ccw
xsetwacom set "Wacom Intuos Pro S Pad pad" AbsWheelUp "0"
# # wheel cw
xsetwacom set "Wacom Intuos Pro S Pad pad" AbsWheelDown "0"
# xsetwacom set "Wacom Intuos Pro S Pad pad" Button 4 "key a"

# lower group
xsetwacom set "Wacom Intuos Pro S Pad pad" Button 8 key "key +shift space -shift"
xsetwacom set "Wacom Intuos Pro S Pad pad" Button 9 key "key +ctrl +shift z -ctrl -shift"
xsetwacom set "Wacom Intuos Pro S Pad pad" Button 10 key "key +ctrl z -ctrl"
