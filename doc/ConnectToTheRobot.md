# [Connect to the Robot](../README.md)

## Entering Update Mode

### Preparation

1. Disconnect the USB cable.
1. Make sure the hub is turned off.

### Enter update mode (see video)

1. Press and hold the Bluetooth button on the hub.
1. Connect the USB cable.  (The light on the hub will come on solid purple.)
1. Continue to hold the Blutooth button down until the light starts blinking pink-green-blue-off.
1. Release the Bluetooth button.

## Backing Up Firmware

To backup firmware, execute the following steps.  This procedure was used to create the `firmware/spike-prime-original-20240829.zip` from the Spike Prime Hub after updating the hub using the Lego Education Edition official software.  This firmware backup can be used to restore the hub to its original state.

1. Enter update mode. (Instructions above.)
1. Execute the following code.  Change the filename to save the image to to indicate what version you are backing up.

    ```bash
    mkdir -p firmware
    pybricksdev dfu backup firmware/spike-prime-original.zip
    ```

## Restoring a Backup of Firmware

To restore a backup of firmware (i.e. restoring the original firmware), follow these procedures changing the name of the filename to be the firmware image you wish to restore.

1. Enter update mode. (Instructions above.)
1. Execute the following code.

    ```bash
    pybricksdev dfu restore firmware/spike-prime-original.zip
    ```

## Flashing the PyBricks Firmware

Before you can start developing with VSCode and pushing code to the hub, you have to install the PyBricks firmware to the hub.  These can be downloaded from the releases page found here <https://github.com/pybricks/pybricks-micropython/releases>.

1. Enter update mode. (Instructions above.)
1. Execute the following code.  Change the name in the snippet below to name your robot appropriately.  In this example we will be naming the robot `batman`.

    ```bash
    pybricksdev flash firmware/pybricks-primehub-v3.5.0.zip --name batman
    ```

1. Use the labelmaker to create a label with the name you used and attach it to the robot.

## Running Code on the Robot

Execute the following to run code on the robot.  Make sure to update the following command with the file name you wish to execute and the robot name you wish to run it on.  (Note that the robot must be on and have been flashed with the PyBricks firmware with an identifying name for the following to work.)

```bash
pybricksdev run ble --wait --name batman test.py
