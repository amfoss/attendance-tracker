#!/usr/bin/env bash

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

if [[ "$machine" = "Mac" ]];then
    /usr/local/bin/python3 /Users/"$1"/.attendance/attendance.py "$1" >/tmp/stdout.log 2>/tmp/stderr.log
else
    python3 /opt/attendance/attendance.py &> /opt/attendance/attendance.log

fi
