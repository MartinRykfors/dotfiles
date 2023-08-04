#! /usr/bin/bash
chosen=$(echo -e "󰒲  Suspend\n  Reboot\n  Shutdown" | rofi -dmenu -i -theme-str 'configuration { show-icons: false; } window { anchor: north east; location: north east; width: 6%; y-offset: 32px; border: 0px; padding: 0px;} inputbar {enabled: false;} listview {border: 0px;}')

if [[ $chosen == "󰒲  Suspend" ]]; then
	systemctl suspend
elif [[ $chosen = "  Reboot" ]]; then
	systemctl reboot
elif [[ $chosen = "  Shutdown" ]]; then
	systemctl poweroff
fi
