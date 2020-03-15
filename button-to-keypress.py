"""
# Microbit button to keypress
In this script, the A button on the microbit triggers a press and release keyboard event that is recognized by the operating system. You can use it for playing one-button games and the key being activated can be customized.
"""

# Libraries being used
import time
import microbit
import keyboard

# Intro moment: the first button press activates the script.
print("Press A to start and B to stop afterwards.")
time.sleep(2)
started = False
while not started:
    time.sleep(0.01)
    if microbit.button_a.was_pressed():
        print("Button A pressed")
        started = True

# Customization variable
key_to_activate = 'space'

# Main loop
is_playing = True
while is_playing:
    time.sleep(0.01)
    if microbit.button_a.was_pressed():
        keyboard.press_and_release(key_to_activate)
        print("Button A -> " + key_to_activate)

    # Exit logic
    if microbit.button_b.was_pressed():
        is_playing = False

print("Finished.")
