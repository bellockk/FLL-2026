from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task
from config import (
    LEFT_MOTOR_PORT,
    RIGHT_MOTOR_PORT,
    BACK_MOTOR_PORT,
    FRONT_MOTOR_PORT,
    LEFT_COLOR_SENSOR_PORT,
    RIGHT_COLOR_SENSOR_PORT,
    WHEEL_DIAMETER,
    AXLE_TRACK,
    STRAIGHT_SPEED,
    STRAIGHT_ACCELERATION,
    TURN_RATE,
    TURN_ACCELERATION)


def diff_angles(a: int, b: int):
    return ((b - a) + 180) % 360 - 180


def dict2json(dictionary: dict):
    return '{' + ', '.join([
        '"' + key + '": ' + ['', '"'][int(isinstance(value, str))] + str(
            value) + ['', '"'][int(isinstance(
                value, str))] for key, value in dictionary.items()]) + '}'


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
            'right': ColorSensor(getattr(Port, RIGHT_COLOR_SENSOR_PORT))}

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
        self._drive_base.use_gyro(True)
        self.trigger: bool = True
        self.queue = []

    async def mainandlog(self):
        await multitask(
            self.main(),
            self.logit())

    async def main(self):
        for callable, args, kwargs in self.queue:
            await callable(*args, **kwargs)
        self.trigger = False

    async def logit(self):
        while self.trigger:
            print(dict2json({
                # 'Left Color Sensor': self._color_sensors[
                #     'left'].reflection(),
                # 'Right Color Sensor': self._color_sensors[
                #     'right'].reflection(),
                'Right Motor Angle': self._motors['right'].angle(),
                # 'Right Motor Speed': self._motors['right'].speed(),
                'Left Motor Angle': self._motors['left'].angle(),
                # 'Left Motor Speed': self._motors['left'].speed(),
                'Front Motor Angle': self._motors['front'].angle(),
                # 'Front Motor Speed': self._motors['front'].speed(),
                'Back Motor Angle': self._motors['back'].angle(),
                # 'Back Motor Speed': self._motors['back'].speed()}))
                }))
            await wait(500)

    def run(self):
        run_task(self.mainandlog())

    def reset_heading(self):
        self._hub.imu.reset_heading()

    def wait(self, time):
        self.queue.append((wait, (time,), {}))

    def heading(self):
        return self._hub.imu.heading()

    def drive(self, distance):
        self.queue.append((self._drive_base.straight, (distance,), {}))

    def turn(self, angle):
        self.queue.append((self._drive_base.turn, (angle,), {}))

    def back_lift(self, angle, speed=120):
        self.queue.append(
            (self._motors['back'].run_angle, (speed, angle,), {}))

    def front_lift(self, angle, speed=120):
        self.queue.append(
            (self._motors['front'].run_angle, (speed, angle,), {}))
