"""
# microbitsy: a microbit-based controller for bitsy games (https://ledoux.itch.io/bitsy) 

A one-script controller for Bitsy games. The Bitsy tool allows for 4 directional movement (represented by WASD or arrow keys) and skipping text using the same keys. You can find many Bitsy games to play here: https://itch.io/games/tag-bitsy.

 The microbitsy script lets you control games by tilting the microbit to choose your direction and touching pin 0 to confirm your choice of action. 
"""

# Libraries being used
import time
import microbit
import keyboard

# Intro moment: the first button press activates the script.
print("---*** microbitsy ***---\nPress A to start and B to quit.")
started = False
time.sleep(1)
while not started:
    time.sleep(0.02)
    if microbit.button_a.was_pressed():
        print("Started!")
        started = True
        microbit.display.show(microbit.Image.HEART)

# Customization variables
horizontal_threshold = 300
vertical_threshold = 300
speed = 1
action = ''
time.sleep(1)
# Main loop
is_playing = True
while is_playing:
    time.sleep(0.01)
    # microbit.display.show(microbit.Image.HAPPY)
    microbit.display.clear()
    action = ''

    # Get data from the accelerometer sensor
    input_x = microbit.accelerometer.get_x()
    input_y = microbit.accelerometer.get_y()
    move_x = 0
    move_y = 0

    if input_x < -horizontal_threshold:
        # Select left movement
        print('left')
        move_x = -speed
        microbit.display.show(microbit.Image.ARROW_W)
        action = 'a'

    if input_x > horizontal_threshold:
        # Select right movement
        print('right')
        move_x = speed
        microbit.display.show(microbit.Image.ARROW_E)
        action = 'd'

    if input_y < -vertical_threshold:
        # Select up movement
        print('up')
        move_y = -speed
        microbit.display.show(microbit.Image.ARROW_N)
        action = 'w'

    if input_y > vertical_threshold:
        # Select down movement
        print('down')
        move_y = speed
        microbit.display.show(microbit.Image.ARROW_S)
        action = 's'

    if move_x == 0 and move_y == 0:
        microbit.display.show(microbit.Image.SQUARE_SMALL)

    # Uses the button A or pin0 touch to confirm action.
    if microbit.button_a.was_pressed():
        is_action_pressed = False
        if action != '':
            keyboard.press_and_release(action)
    elif microbit.pin0.is_touched() and not is_action_pressed:
        is_action_pressed = True
        if action != '':
            keyboard.press_and_release(action)

    if not microbit.pin0.is_touched():
        is_action_pressed = False

    # Exit logic
    if microbit.button_b.was_pressed():
        is_playing = False

# Closing animation
microbit.display.show(microbit.Image.HEART)
time.sleep(1)
microbit.display.clear()
print("Finished.")
