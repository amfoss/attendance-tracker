#!/usr/bin/env bash

#interface=`ip link | grep -Po '^\d+:\s+\K[^:]+' | grep 'w'`
#sudo iwlist $interface scan | grep ESSID

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac
#echo ${machine}
if [ "$machine" = "Mac" ];then
    /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/sbin/airport -s | awk '{print $1}'
else
    interface=`ip link | grep -Po '^\d+:\s+\K[^:]+' | grep 'w'`
    sudo iwlist $interface scanning | grep Address
fi