#!/usr/bin/env bash

interface=`ip link | grep -Po '^\d+:\s+\K[^:]+' | grep 'w'`
sudo iwlist $interface scan | grep ESSID
