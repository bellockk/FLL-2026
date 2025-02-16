from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Button, Icon, Stop
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
            'front': Motor(getattr(Port, FRONT_MOTOR_PORT),
                           reset_angle=False),
            'back': Motor(getattr(Port, BACK_MOTOR_PORT),
                           reset_angle=False)}

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
        self.font_motor_lower = None
        self.font_motor_upper = None
        self.font_motor_up = None
        self.back_motor_lower = None
        self.back_motor_upper = None
        self.back_motor_up = None

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
            self._motors['back'].run_target(speed, self.back_motor_up),
            self._motors['front'].run_target(speed*.25, self.front_motor_up))
    async def _stow_all(self, speed=500):
        await self._raise_all(speed)
        await multitask(
            self._motors['back'].run_until_stalled(-200, then=Stop.HOLD),
            self._motors['front'].run_until_stalled(-200, then=Stop.HOLD))
    async def _lower_all(self, speed=500):
        await multitask(
            self._motors['back'].run_target(speed, self.back_motor_lower),
            self._motors['front'].run_target(speed, self.front_motor_lower))
    async def _lower_plow_stow_fork_lift(self, speed=500):
        await self._raise_all()
        await multitask(
            self._motors['back'].run_target(speed, self.back_motor_upper),
            self._motors['front'].run_target(speed, self.front_motor_lower))
    async def _lower_fork_lift_stow_plow(self, speed=500):
        await self._raise_all()
        await multitask(
            self._motors['back'].run_target(speed, self.back_motor_lower),
            self._motors['front'].run_target(speed, self.front_motor_upper))

    async def _initialize(self):
        await multitask(
            self._motors['back'].run_until_stalled(200, then=Stop.HOLD),
            self._motors['front'].run_until_stalled(200, then=Stop.HOLD))
        backoff = 35
        await self._motors['back'].run_until_stalled(200, then=Stop.HOLD)
        self.back_motor_lower = self._motors['back'].angle() - backoff
        await self._motors['back'].run_until_stalled(-200, then=Stop.HOLD)
        self.back_motor_upper = self._motors['back'].angle() + backoff
        self.back_motor_up = self.back_motor_upper + 170
        await self._motors['back'].run_target(200, self.back_motor_up)
        await self._motors['front'].run_until_stalled(200, then=Stop.HOLD)
        self.front_motor_lower = self._motors['front'].angle() - backoff
        await self._motors['front'].run_until_stalled(-200, then=Stop.HOLD)
        self.front_motor_upper = self._motors['front'].angle() + backoff
        self.front_motor_up = self.front_motor_upper + 160
        await self._stow_all()

    def initialize(self):
        self.queue.append((self._initialize, (), {}))

    def fork_lift(self, angle, speed=120):
        print(f'angle: {angle}')
        target = int(self.back_motor_lower + (self.back_motor_upper - self.back_motor_lower) * angle * .01)
        self.queue.append((self._motors['back'].run_target, (speed, target,), {}))
    def fork_lift_stow(self, speed=500):
        self.queue.append((self._motors['back'].run_target, (speed, self.back_motor_upper), {}))
    def fork_lift_up(self, speed=500):
        self.queue.append((self._motors['back'].run_target, (speed, self.back_motor_up), {}))
    def fork_lift_lower(self, speed=500):
        self.queue.append((self._motors['back'].run_target, (speed, self.back_motor_lower), {}))

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

    def plow(self, angle, speed=120):
        target = int(self.front_motor_lower + (self.front_motor_upper - self.front_motor_lower) * angle * .01)
        self.queue.append((self._motors['front'].run_target, (speed, target,), {}))
    def plow_stow(self, speed=500):
        self.queue.append((self._motors['front'].run_target, (speed, self.front_motor_upper), {}))
    def plow_up(self, speed=500):
        self.queue.append((self._motors['front'].run_target, (speed, self.front_motor_up), {}))
    def plow_lower(self, speed=500):
        self.queue.append((self._motors['front'].run_target, (speed, self.front_motor_lower), {}))

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
                motor.hold()
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