"""
# Microbit button to keypress
In this script, the A button on the microbit triggers a press and release keyboard event that is recognized by the operating system. You can use it for playing one-button games and the key being activated can be customized.
"""

# Libraries being used
import time
import keyboard
import serial
import io

ser = serial.Serial('COM15', baudrate=115200, timeout=0, parity=serial.PARITY_NONE,
                    bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
print(ser.name)
# ser.open()
print(ser.is_open)

horizontal_threshold = 300
vertical_threshold = 300
action = ''

# Intro moment: the first button press activates the script.
started = False
while not started:
    time.sleep(0.060)
    input_raw = sio.readline()

    if(input_raw != ''):
        accel_data_str = input_raw.split()
        print(accel_data_str)
        input_x = int(accel_data_str[0])
        input_y = int(accel_data_str[1])
        btn_left = int(accel_data_str[2])
        btn_right = int(accel_data_str[3])

        if input_y < -vertical_threshold:
            # Select up movement
            action = 'down arrow'

        if input_y > vertical_threshold:
            # Select down movement
            action = 'up arrow'

        if btn_left > 0:
            action = 'left arrow'

        if btn_right > 0:
            action = 'right arrow'

        if action != '':
            keyboard.press_and_release(action)

time.sleep(1)
ser.close()
