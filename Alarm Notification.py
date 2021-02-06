# Simple code for alarm (Message)
# Written by Abdulazis Mijadinoski

import time
import winsound
from win10toast import ToastNotifier

def timer(message, minutes):
    # Windows Norification Instalator
    notificator = ToastNotifier()
    # Notification Details
    notificator.show_toast("Alarm", f"Alarm will start in {seconds} seconds..., duration=50")
    # Pause Script (When will alarm start ex: 2 sec * 2 = 4 sec(!!!BE CAREFULL WHAT ARE YOU DOING!!!))
    time.sleep(seconds * 1)
    # duration 1000 = 1 sec
    # Alarm Sound
    winsound.Beep(frequency=200, duration=1500)
    # Show Notification
    notificator.show_toast(f"Alarm", message, duration=50)
if __name__ == "__main__":
    message = "The End"
    seconds = 2
    timer(message, seconds)

# If you like this this code, follow me on GitHub for more projects!