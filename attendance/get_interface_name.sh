#!/usr/bin/env bash

ip link | grep -Po '^\d+:\s+\K[^:]+' | grep 'w'
