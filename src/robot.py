from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task, StopWatch
from config import *


def diff_angles(self, a, b):
    return ((b - a) + 180) % 360 - 180


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

        # Initialize Color Sensors
        self._color_sensors = {
            'left': ColorSensor(getattr(Port, LEFT_COLOR_SENSOR_PORT)),
            'right': ColorSensor(getattr(Port, LEFT_COLOR_SENSOR_PORT))}

        # Initialize the drive base
        self._drive_base = DriveBase(
            self._motors['left'], self._motors['right'],
            wheel_diameter=WHEEL_DIAMETER,
            axle_track=AXLE_TRACK)
        self._drive_base.settings(
            STRAIGHT_SPEED,
            STRAIGHT_ACCELERATION,
            TURN_RATE,
            TURN_ACCELERATION)
        self.queue = []

    async def main(self):
        for callable, args, kwargs in self.queue:
            await callable(*args, **kwargs)

    def run(self):
        run_task(self.main())

    def reset_heading(self):
        self._hub.imu.reset_heading()

    def wait(self, time):
        wait(time)

    def heading(self):
        return self._hub.imu.heading()

    def drive(self, distance):
        self.queue.append((self._drive_base.straight, (distance,), {}))

    def turn(self, angle):
        self.queue.append((self._drive_base.turn, (angle,), {}))

    def back_lift(self, angle):
        self.queue.append((self._motors['back'].run_angle, (90, angle,), {}))

    def front_lift(self, angle):
        self.queue.append((self._motors['front'].run_angle, (90, angle,), {}))