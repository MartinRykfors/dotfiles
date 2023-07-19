chosen=$(echo "1 Suspend\n2 Reboot\n3 Shutdown" | rofi -dmenu -i -theme-str 'configuration { show-icons: false; }')

if [[ $chosen = "1 Suspend" ]]; then
	systemctl suspend
elif [[ $chosen = "2 Reboot" ]]; then
	systemctl reboot
elif [[ $chosen = "3 Shutdown" ]]; then
	systemctl poweroff
fi
