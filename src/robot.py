from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Button, Icon, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task, hub_menu
import ujson as json
import ustruct as struct
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
    TURN_ACCELERATION,
    HEADER_FORMAT)


def robot_api(func):
    def wrapper(*args, **kwargs):
        args[0].queue.append((func, args, kwargs))
    for attr in ['doc', 'name', 'module']:
        if hasattr(func, f'__{attr}__'):
            wrapper.__doc__ = func.__doc__
    return wrapper


class Robot():
    """Robot controller."""

    def __init__(self):
        # Initialize Hub
        self._hub = PrimeHub()

        # Change the stop program button to pressing both side buttons at the
        # same time
        self._hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

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
        self.front_motor_lower = None
        self.front_motor_upper = None
        self.font_motor_up = None
        self.back_motor_lower = None
        self.back_motor_upper = None
        self.back_motor_up = None
        self._persistent_data = [
            'front_motor_lower',
            'front_motor_upper',
            'front_motor_up',
            'back_motor_lower',
            'back_motor_upper',
            'back_motor_up']

        # Load persistent initialization data
        self.load_persistent_data()

    def save_persistent_data(self):
        data = {member: getattr(
            self, member) for member in self._persistent_data}
        payload = bytes(json.dumps(data), 'utf-8')
        header = struct.pack(HEADER_FORMAT, len(payload))
        self._hub.system.storage(offset=0, write=header + payload)

    def load_persistent_data(self):
        payload_size = struct.unpack(
            HEADER_FORMAT,
            self._hub.system.storage(
                offset=0, read=struct.calcsize(HEADER_FORMAT)))[0]
        payload = self._hub.system.storage(
            offset=struct.calcsize(HEADER_FORMAT),
            read=payload_size)
        if payload == b'':
            return
        persistent_data = json.loads(str(payload, 'utf-8'))
        for member in self._persistent_data:
            setattr(self, member, persistent_data[member])

    def reset_heading(self, heading: int | float = 0):
        self._hub.imu.reset_heading(heading)

    def wait(self, time):
        self.queue.append((wait, (time,), {}))

    def heading(self):
        return self._hub.imu.heading('3D')

    def turn(self, angle: int):
        """
        Turn the robot.

        Args:
          angle: The angle to turn the robot relative to the current position.
        """
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

    def initialize(self):
        self.queue.append((self._initialize, (), {}))

    async def _initialize(self):
        await multitask(
            self._motors['back'].run_until_stalled(200, then=Stop.HOLD),
            self._motors['front'].run_until_stalled(200, then=Stop.HOLD))
        backoff = 5
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
        await self._raise_all()
        self.save_persistent_data()



    def fork_lift(self, percent, speed=120):
        # Gate to between 0 and 100
        percent = min(max(percent, 0), 100)

        target = int(self.back_motor_lower + (
            self.back_motor_upper - self.back_motor_lower) * percent * .01)
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

    def plow(self, percent, speed=120):
        # Gate to between 0 and 100
        percent = min(max(percent, 0), 100)

        target = int(self.front_motor_lower + (
            self.front_motor_upper - self.front_motor_lower) * percent * .01)
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

    @robot_api
    async def drive(self, distance: int, speed: int=STRAIGHT_SPEED):
        """
        Drive a set distance in a straight line.

        Args:
          distance: The distance to travel.  Positive to drive forwards,
            negative to drive backwards.
          speed: The speed at which to drive.
        """
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

    async def logit(self):
        self.trigger = True
        while self.trigger:
            print(json.dumps({
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
                'Back Motor Speed': self._motors['back'].speed(),
                'Heading': self.heading()}))
            await wait(500)

    async def process_queue(self):
        for callable, args, kwargs in self.queue:
            await callable(*args, **kwargs)
        self.queue[:] = []

    def menu(self, *runs):
        run_task(self.menuandlog(*runs))

    async def menuandlog(self, *runs):
        await multitask(
            self._menu(*runs),
            self.logit())

    async def _menu(self, *runs):
        choices = [str(i + 1) for i in range(len(runs))]
        run_map = dict(zip(choices, runs))

        # Set stop button to Bluetooth to allow center button for selection

        index = 0
        self.display_item(choices[index])

        debounce_count = 2  # Consecutive polls for debounce (40ms effective time)

        # Button states and counters
        state = {}
        for button in [Button.LEFT, Button.RIGHT, Button.CENTER]:
            state[button] = {
                'state': False,
                'press': 0,
                'release': 0}
        state[Button.LEFT]['direction'] = -1
        state[Button.RIGHT]['direction'] = 1
        selecting = False  # Flag to indicate center press initiated

        while True:
            pressed = self._hub.buttons.pressed()
            for button, status in state.items():
                if button in pressed:
                    if not status['state']:
                        status['press'] += 1
                        if status['press'] >= debounce_count:
                            status['state'] = True
                            status['press'] = 0
                            # Act on Button Press
                            if button == Button.CENTER:
                                self._hub.display.icon(Icon.HEART)
                                runs[index]()
                                await self.process_queue()
                            else:
                                index = (index + state[button][
                                    'direction']) % len(choices)
                            self.display_item(choices[index])

                    status['release'] = 0
                else:
                    if status['state']:
                        status['release'] += 1
                        if status['release'] >= debounce_count:
                            status['state'] = False
                            status['release'] = 0
                    status['press'] = 0
                await wait(10)

    def display_item(self, item):
        if isinstance(item, str):
            self._hub.display.char(item)
        elif isinstance(item, int):
            self._hub.display.number(item)
        else:
            raise ValueError("Items must be str or int")
