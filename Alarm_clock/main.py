from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def sound_alarm(duration):
    time_elapsed = 0
    print()
    while time_elapsed < duration:
        time.sleep(1)
        time_elapsed += 1

        time_left = duration - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Activity is set for: {minutes_left:02d}:{seconds_left:02d}")

    playsound('ring.mp3')


sound_alarm(10)
