#!/usr/bin/env bash

cat /proc/net/wireless | perl -ne '/(\w+):/ && print $1'
