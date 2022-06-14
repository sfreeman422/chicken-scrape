PID=$(pgrep gnome-session | tail -n1)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)
. /home/steve/.profile
PATH=/usr/local/bin:$PATH
cd /home/steve/code/chicken-scrape
pipenv run python3.8 scrape.py /home/steve/Pictures/chicken
