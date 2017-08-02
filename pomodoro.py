#!/usr/share/env python3
import os
import time

def send_notification(message):
    """ Sends notification with given string as content using notify-send command
    :param message: string containing the notification content
    :returns: None"""

    os.system("notify-send " + message)

work_time = int(input("Enter work duration in minutes: "))
break_time = int(input("Enter break duration in minutes: "))

mode = int(input("""Please select the mode,
        1. Continuous mode - script will keep runnig until you stop it.
        2. Per cycle mode - script will ask to continue after every cycle.
        """))
per_cycle_mode_choice = "Y"

while True:
    send_notification("'Start! Focus on your work.'")
    time.sleep(work_time * 60)
    send_notification("'Good job! Take a break.'")
    time.sleep(break_time * 60)
    if mode == 2:
        per_cycle_mode_choice =  input("Do you want to continue? [Y/n]") 
        if per_cycle_mode_choice != "Y" and per_cycle_mode_choice != "y":
            break
        
