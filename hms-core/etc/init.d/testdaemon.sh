#!/bin/sh

# - The action we're concerned with appears as $1 in a standard 
#   bash-script
case $1 in
    start)
        echo "Starting $0"
        /usr/bin/python /usr/local/bin/testdaemon.py
        ;;
    stop)
        echo "Stopping $0"
        /usr/bin/pkill -f testdaemon.py
        ;;
    restart)
        echo "Restarting $0"
        /usr/bin/pkill -f testdaemon.py
        /usr/bin/python /usr/local/bin/testdaemon.py
        ;;
esac
