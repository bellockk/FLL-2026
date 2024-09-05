from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task


LEFT_MOTOR_PORT = 'A'
RIGHT_MOTOR_PORT = 'B'
BACK_MOTOR_PORT = 'F'
FRONT_MOTOR_PORT = 'D'
LEFT_COLOR_SENSOR_PORT = 'C'
RIGHT_COLOR_SENSOR_PORT = 'E'
GYRO_SENSOR_PORT = 'S4'
WHEEL_DIAMETER = 55.5
AXLE_TRACK = 124


class Robot():
    """Robot controller."""

    def __init__(self):
        # Initialize Hub
        self._hub = PrimeHub()

        # Initialize Motors
        self._motors = {
            'left': Motor(
                getattr(Port, LEFT_MOTOR_PORT),
                Direction.COUNTERCLOCKWISE),
            'right': Motor(getattr(Port, RIGHT_MOTOR_PORT)),
            'front': Motor(getattr(Port, FRONT_MOTOR_PORT)),
            'back': Motor(getattr(Port, BACK_MOTOR_PORT))}

        # Initialize the drive base
        self._drive_base = DriveBase(
            self._motors['left'], self._motors['right'],
            wheel_diameter=WHEEL_DIAMETER,
            axle_track=AXLE_TRACK)

    async def main(self):
        # await self._drive_base.straight(1000)
        await self._motors['back'].run_angle(90, 90)

    def run(self):
        run_task(self.main())
