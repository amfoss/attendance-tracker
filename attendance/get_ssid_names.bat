
set interface=`ip link | findstr -Po '^\d+:\s+\K[^:]+' | findstr 'w'`
netsh %interface% show all | findstr ESSID
