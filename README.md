# microbit-to-keyboard-mouse-gamepad

Experiments in using the microbit board to simulate keyboards, mouse and gamepads (not yet, though) via USB.

![Example of using the accelerometer to control mouse movement.](microbit-mouse-smaller.gif)

_Example of using the accelerometer to control mouse movement._

## Motivation

One of the obstacles when creating alternative controllers and more accessible interfaces is that few games or software have open and flexible ways to customize their inputs. Many support devices like keyboards and mouse, so creating ways for different devices to "disguise" themselves as keyboard and mouse can facilitate experimentation. So, I prepared these examples in order to prepare for the _DesignJam: Accessible Gamepad Challenge_ at the [accessXchange forum](https://www.accessxchangeforum.com/).

The microbit is an interesting device for this because it features a variety of sensors that can be combined to create new interfaces. Projects like [bitio](https://github.com/whaleygeek/bitio) and [MicroBike](https://github.com/musabkilic/MicroBike) were inspirations in making these examples.

## Installation guide

1. Install Python 3.7 and the `pip` package manager.
2. Install the mouse and keyboard libraries by running the commands `pip install mouse` and `pip install keyboard` from a terminal window.
3. Download [bitio](https://github.com/whaleygeek/bitio) library.
4. Copy the `microbit` folder from the `bitio` folder to the same folder where you will be creating your scripts.
5. Connect the microbit to the computer via USB.
6. Flash the `bitio.hex` (on the `bitio` folder you downloaded) to the microbit by copying it the MICROBIT drive that shows in the explorer.
7. Now you are ready to run the examples using the commands `python accelerometer-to-mouse.py` or `python button-to-keypress.py`.

You can create your own scripts by copying and changing the example scripts. The scripts are commented. To run your scripts, you can use the `python your_script_filename.py`.

## Dependencies

If you'd like to explore the possibilities of the libraries being used, please check their documentation linked below. It can be good for coming up with ideas.

- [bitio](https://github.com/whaleygeek/bitio)
- [mouse](https://github.com/boppreh/mouse)
- [keyboard](https://github.com/boppreh/keyboard)

## License

The code specific to this project is licensed under the [LGPLv3 license](https://choosealicense.com/licenses/lgpl-3.0/). As for the dependencies licenses, please check their specific websites.