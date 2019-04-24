"""
# Microbit controller for the game Sagittarius (https://gprosser.itch.io/sagittarius).
In this script (based on the accelerometer example), we use mouse dragging (by holding the 0 pin and tilting the microbit), clicking (touching pin 2), and keypresses (by tilting).
"""

# Libraries being used
import time
import microbit
import mouse
import keyboard

# Intro moment: the first button press activates the script.
print("=== Sagittarius controller ===\nPress A to start and B to stop afterwards.")
started = False
time.sleep(1)
while not started:
    time.sleep(0.02)
    if microbit.button_a.was_pressed():
        print("Ready to play.")
        started = True

# Customization variables
horizontal_threshold = 200
vertical_threshold = 200
speed = 15
move_x = 0
move_y = 0
is_mouse_pressed = False

# Main loop
is_playing = True
while is_playing:
    time.sleep(0.01)

    if move_x < 0:
        keyboard.release('a')

    if move_x > 0:
        keyboard.release('d')

    # Get data from the accelerometer sensor
    accel_x = microbit.accelerometer.get_x()
    accel_y = microbit.accelerometer.get_y()
    move_x = 0
    move_y = 0

    if accel_x < -horizontal_threshold:
        # Prepare move mouse left and key press A
        move_x = -speed
        keyboard.press('a')

    if accel_x > horizontal_threshold:
        # Prepare move mouse right and key press D
        move_x = speed
        keyboard.press('d')

    if accel_y < -vertical_threshold:
        # Prepare move mouse down
        move_y = -speed

    if accel_y > vertical_threshold:
        # Prepare move mouse up
        move_y = speed

    # Apply the calculated movement to the operating system's mouse
    mouse.move(move_x, move_y, absolute=False)

    if microbit.pin0.is_touched() and not is_mouse_pressed:
        # Moves to a point closer to the center of the screen
        # for better dragging.

        mouse.move(400, 400, True)
        mouse.press('left')
        is_mouse_pressed = True

    if not microbit.pin0.is_touched() and is_mouse_pressed:
        mouse.release('left')
        is_mouse_pressed = False

    if microbit.pin2.is_touched():
        mouse.click()

    # Exit logic
    if microbit.button_b.was_pressed():
        is_playing = False

print("Finished.")
