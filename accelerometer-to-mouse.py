"""
# Microbit accelerometer to mouse
In this script, tilting the microbit is converted to mouse movements that are recognized by the operating system. You can customize the speed of the mouse movement, as well as the sensitivity of the tilting axes.
"""

# Libraries being used
import time
import microbit
import mouse

# Intro moment: the first button press activates the script.
print("Press A to start and B to stop afterwards.")
started = False
time.sleep(1)
while not started:
    time.sleep(0.02)
    if microbit.button_a.was_pressed():
        print("Started!")
        started = True

# Customization variables
horizontal_threshold = 200
vertical_threshold = 200
speed = 3

# Main loop
is_playing = True
while is_playing:
    microbit.sleep(5)

    # Get data from the accelerometer sensor
    input_x = microbit.accelerometer.get_x()
    input_y = microbit.accelerometer.get_y()
    move_x = 0
    move_y = 0

    if input_x < -horizontal_threshold:
        # Prepare move mouse left
        print('left')
        move_x = -speed

    if input_x > horizontal_threshold:
        # Prepare move mouse right
        print('right')
        move_x = speed

    if input_y < -vertical_threshold:
        # Prepare move mouse down
        print('down')
        move_y = -speed

    if input_y > vertical_threshold:
        # Prepare move mouse up
        print('up')
        move_y = speed

    # Apply the calculated movement to the operating system's mouse
    mouse.move(move_x, move_y, absolute=False, duration=0.01)

    # Exit logic
    if microbit.button_b.was_pressed():
        is_playing = False

print("Finished.")
