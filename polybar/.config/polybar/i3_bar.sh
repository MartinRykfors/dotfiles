#!/usr/bin/env bash

# Terminate already running bar instances
# If all your bars have ipc enabled, you can use
polybar-msg cmd quit
# Otherwise you can use the nuclear option:
# killall -q polybar

# Launch bar1 and bar2
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
polybar --config=~/.config/polybar/config.ini i3_bar 2>&1 | tee -a /tmp/polybar_i3.log & disown
polybar --config=~/.config/polybar/config.ini talon_bar 2>&1 | tee -a /tmp/polybar_talon.log & disown

echo "Bars launched..."
