from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Button, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task, hub_menu
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

        # Change the stop program button to pressing both side buttons at the
        # same time
        self._hub.system.set_stop_button([Button.RIGHT_UP])

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
        self.queue[:] = []
        self.trigger = False

    async def logit(self):
        while self.trigger:
            print(dict2json({
                'Left Color Sensor': await self._color_sensors[
                    'left'].reflection(),
                'Right Color Sensor': await self._color_sensors[
                    'right'].reflection(),
                'Right Motor Angle': self._motors['right'].angle(),
                'Right Motor Speed': self._motors['right'].speed(),
                'Left Motor Angle': self._motors['left'].angle(),
                'Left Motor Speed': self._motors['left'].speed(),
                'Front Motor Angle': self._motors['front'].angle(),
                'Front Motor Speed': self._motors['front'].speed(),
                'Back Motor Angle': self._motors['back'].angle(),
                'Back Motor Speed': self._motors['back'].speed()}))
            await wait(500)

    def run(self):
        run_task(self.mainandlog())

    def reset_heading(self):
        self._hub.imu.reset_heading()

    def wait(self, time):
        self.queue.append((wait, (time,), {}))

    def heading(self):
        return self._hub.imu.heading()

    def turn(self, angle):
        self.queue.append((self._drive_base.turn, (angle,), {}))

    async def _raise_all(self, speed=500):
        await multitask(
            self._motors['back'].run_target(speed, 215),
            self._motors['front'].run_target(speed*.25, 215))
    async def _stow_all(self, speed=500):
        await multitask(
            self._motors['back'].run_target(speed*.4, 75),
            self._motors['front'].run_target(speed, 80))
    async def _lower_all(self, speed=500):
        await multitask(
            self._motors['back'].run_target(speed, 360),
            self._motors['front'].run_target(speed, 360))
    async def _lower_plow_stow_fork_lift(self, speed=500):
        await multitask(
            self._motors['back'].run_target(speed, 75),
            self._motors['front'].run_target(speed, 360))
    async def _lower_fork_lift_stow_plow(self, speed=500):
        await multitask(
            self._motors['back'].run_target(speed, 360),
            self._motors['front'].run_target(speed, 80))

    def fork_lift(self, angle, speed=120):
        self.queue.append((self._motors['back'].run_angle, (speed, angle,), {}))
    def fork_lift_stow(self, speed=500):
        self.queue.append((self._motors['back'].run_target, (speed, 75), {}))
    def fork_lift_up(self, speed=500):
        self.queue.append((self._motors['back'].run_target, (speed, 215), {}))
    def fork_lift_lower(self, speed=500):
        self.queue.append((self._motors['back'].run_target, (speed, 360), {}))

    def raise_all(self, speed=500):
        self.queue.append((self._raise_all, (speed,), {}))
    def stow_all(self, speed=500):
        self.queue.append((self._stow_all, (speed,), {}))
    def lower_all(self, speed=500):
        self.queue.append((self._lower_all, (speed,), {}))
    def lower_fork_lift_stow_plow(self, speed=500):
        self.queue.append((self._lower_fork_lift_stow_plow, (speed,), {}))
    def lower_plow_stow_fork_lift(self, speed=500):
        self.queue.append((self._lower_plow_stow_fork_lift, (speed,), {}))

    def plow_lift(self, angle, speed=120):
        self.queue.append((self._motors['front'].run_angle, (speed, angle,), {}))
    def plow_stow(self, speed=500):
        self.queue.append((self._motors['front'].run_target, (speed, 80), {}))
    def plow_up(self, speed=500):
        self.queue.append((self._motors['front'].run_target, (speed, 215), {}))
    def plow_lower(self, speed=500):
        self.queue.append((self._motors['front'].run_target, (speed, 360), {}))

    def curve(self, radius, angle):
        self.queue.append((self._drive_base.curve, (radius, angle,), {}))

    def drive_and_raise_fork_lift(
            self, distance, rotation_angle,
            speed=STRAIGHT_SPEED,
            rotation_speed=TURN_RATE):
        self.queue.append((self._drive_and_raise_fork_lift, (
            distance, speed, rotation_angle, rotation_speed), {}))
    async def _drive_and_raise_fork_lift(
            self, distance, rotation_angle,
            speed=STRAIGHT_SPEED,
            rotation_speed=TURN_RATE):
        self._drive_base.settings(
            speed,
            STRAIGHT_ACCELERATION,
            TURN_RATE,
            TURN_ACCELERATION)
        await multitask(
            self._drive_base.straight(distance),
            self._motors['back'].run_angle(rotation_speed, rotation_angle))
        self._drive_base.settings(
            STRAIGHT_SPEED,
            STRAIGHT_ACCELERATION,
            TURN_RATE,
            TURN_ACCELERATION)

    def drive_and_raise_plow(
            self, distance, rotation_angle,
            speed=STRAIGHT_SPEED,
            rotation_speed=TURN_RATE):
        self.queue.append((self._drive_and_raise_plow, (
            distance, speed, rotation_angle, rotation_speed), {}))
    async def _drive_and_raise_plow(
            self, distance, rotation_angle,
            speed=STRAIGHT_SPEED,
            rotation_speed=TURN_RATE):
        self._drive_base.settings(
            speed,
            STRAIGHT_ACCELERATION,
            TURN_RATE,
            TURN_ACCELERATION)
        await multitask(
            self._drive_base.straight(distance),
            self._motors['front'].run_angle(rotation_speed, rotation_angle))
        self._drive_base.settings(
            STRAIGHT_SPEED,
            STRAIGHT_ACCELERATION,
            TURN_RATE,
            TURN_ACCELERATION)

    def drive(self, distance, speed=STRAIGHT_SPEED):
        self.queue.append((self._drive, (distance,speed,), {}))
    async def _drive(self, distance, speed=STRAIGHT_SPEED):
        self._drive_base.settings(
            speed,
            STRAIGHT_ACCELERATION,
            TURN_RATE,
            TURN_ACCELERATION)
        await self._drive_base.straight(distance)
        self._drive_base.settings(
            STRAIGHT_SPEED,
            STRAIGHT_ACCELERATION,
            TURN_RATE,
            TURN_ACCELERATION)

    def menu(self, *runs):
        run_map = {str(i + 1): run for i, run in enumerate(runs)}
        choices = list(sorted(run_map.keys())) + ['X']
        while True:
            selected = None
            for motor in self._motors.values():
                motor.stop()
            if len(choices) > 1:
                selected = hub_menu(*choices)
            elif len(choices) == 1:
                self._hub.display.char("1")
                while not Button.CENTER in self._hub.buttons.pressed():
                    pass
                selected = "1"
            if selected is not None:
                if selected == 'X':
                    self.raise_all()
                    self.stow_all()
                    break
                run_map[selected]()
                while choices[0] != selected:
                    choices.append(choices.pop(0))
                choices.append(choices.pop(0))
                self._hub.display.icon(Icon.HEART)
            self.wait(250)
            self.run()