#! /usr/bin/env python3
'''
Small module that displays batter capacity of either 2 batteries
if your laptop has 2 of them or just of your one battery
'''

try:
    with open('/sys/class/power_supply/BAT1/capacity', 'r') as bat1_cap:
        BAT1_CAPACITY = bat1_cap.read()
    with open('/sys/class/power_supply/BAT0/capacity', 'r') as bat0_cap:
        BAT0_CAPACITY = bat0_cap.read()
    print(int((BAT1_CAPACITY + BAT0_CAPACITY) / 2))
except IOError:
    try:
        with open('/sys/class/power_supply/BAT0/capacity', 'r') as bat0_cap:
            print(bat0_cap.read())
    except IOError:
        with open('/sys/class/power_supply/BAT1/capacity', 'r') as bat1_cap:
            print(bat1_cap.read())
