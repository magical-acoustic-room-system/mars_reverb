# ROS 2 Package for Panel Control

This folder contains code for a ROS 2 Node for controlling the positions of an array of panels. The name "Panel Bus" is chosen because commands are sent on an I2C bus for reception by a configurable number of Arduino Nano nodes. These nodes will receive the data, verify that the ID associated with the message sent on the bus matches their own, and then rotate a servo motor attached to a single panel.

## Integrating with ROS 2

To use this package in your ROS 2 workspace, navigate to the src folder of your ROS 2 workspace, and clone the directory by running the following commands.

`git clone -n --depth=1 --filter=tree:0 \https://github.com/magical-acoustic-room-system/mars_reverb`

`cd mars_reverb`

`git sparse-checkout set --no-cone ROS`

`git checkout`

`cp -r ROS/panel_bus ..`

`rm -r mars_reverb`

Now navigate to the root directory of your ROS 2 workspace and build the package.

## Troubleshooting Tips

This package requires access to the smbus module, which allows python to integrate with the I2C bus of the raspberry pi. However, creating an instance of the SMBus requires root access, which raises complications in ROS. The workaround is to create a new user group, add the device file of the I2C bus, usually `\dev\i2c-1` to this group, and then adding the user to this group.

`sudo groupadd i2c` Create a new user group i2c

`sudo chown :i2c /dev/i2c-1` Add ownership of the device file to the new group.

`sudo usermod -aG i2c {user}` Add the user to the group.
