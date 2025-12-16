from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Button, Icon, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task
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
        args[0]._queue.append((func, args, kwargs))
    for attr in ['doc', 'name', 'module']:
        attribute = f'__{attr}__'
        if hasattr(func, attribute):
            setattr(wrapper, attribute, getattr(func, attribute))
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
        self._queue = []
        self._front_motor_lower = None
        self._front_motor_upper = None
        self._font_motor_up = None
        self._back_motor_lower = None
        self._back_motor_upper = None
        self._back_motor_up = None
        self._persistent_data = [
            '_front_motor_lower',
            '_front_motor_upper',
            '_front_motor_up',
            '_back_motor_lower',
            '_back_motor_upper',
            '_back_motor_up']

        # Load persistent initialization data
        self._load_persistent_data()

    def reset_heading(self, heading: int | float = 0):
        self._hub.imu.reset_heading(heading)

    def wait(self, time):
        self._queue.append((wait, (time,), {}))

    def heading(self):
        return self._hub.imu.heading('3D')

    def turn(self, angle: int):
        """
        Turn the robot.

        Args:
          angle: The angle to turn the robot relative to the current position.
        """
        self._queue.append((self._drive_base.turn, (angle,), {}))

    def lower_all(self, speed=500):
        """
        Lower both the fork lift and plow.

        Args:
            speed (int, optional): Speed at which to move both the fork lift and plow. Defaults to 500.
        """
        self._queue.append((self._lower_all, (speed,), {}))

    def lower_fork_lift_stow_plow(self, speed=500):
        """
        Lower the fork lift and stow the plow.

        Args:
            speed (int, optional): Speed at which to move both the fork lift and plow. Defaults to 500.
        """
        self._queue.append((self._lower_fork_lift_stow_plow, (speed,), {}))

    def lower_plow_stow_fork_lift(self, speed=500):
        """
        Lower the plow and stow the fork lift.

        Args:
            speed (int, optional): Speed at which to move both the fork lift and plow. Defaults to 500.
        """
        self._queue.append((self._lower_plow_stow_fork_lift, (speed,), {}))

    def raise_all(self, speed=500):
        """
        Raise both the fork lift and plow.

        Args:
            speed (int, optional): Speed at which to move both the fork lift and plow. Defaults to 500.
        """
        self._queue.append((self._raise_all, (speed,), {}))

    def stow_all(self, speed=500):
        self._queue.append((self._stow_all, (speed,), {}))

    def plow(self, percent: float, speed: float=120):
        """
        Set the plow height.

        This takes a percent value that will be gated to between 0 and 100.  0
        corresponds to completely lowered, and 100 corresponds to fully stowed.

        Args:
            percent (float, deg): The percent position to move the plow to.
            speed (float, mm/s): The speed to move the plow at. Defaults to 120.
        """
        # Gate to between 0 and 100
        percent = min(max(percent, 0), 100)
        assert self._front_motor_upper is not None
        assert self._front_motor_lower is not None
        target = int(self._front_motor_lower + (
            self._front_motor_upper - self._front_motor_lower) * percent * .01)
        self._queue.append((self._motors['front'].run_target, (speed, target,), {}))

    def plow_stow(self, speed=500):
        """
        Stow the plow.

        Args:
            speed (int, optional): The speed at which to move the plow. Defaults to 500.
        """
        self._queue.append((self._motors['front'].run_target, (speed, self._front_motor_upper), {}))

    def plow_up(self, speed=500):
        """
        Raise the plow.

        Args:
            speed (int, optional): The speed at which to move the plow. Defaults to 500.
        """
        self._queue.append((self._motors['front'].run_target, (speed, self._front_motor_up), {}))

    def plow_lower(self, speed=500):
        """
        Lower the plow.

        Args:
            speed (int, optional): The speed at which to move the plow. Defaults to 500.
        """
        self._queue.append((self._motors['front'].run_target, (speed, self._front_motor_lower), {}))

    def fork_lift(self, percent: float, speed: float=120):
        """
        Set the fork lift height.

        This takes a percent value that will be gated to between 0 and 100.  0
        corresponds to completely lowered, and 100 corresponds to fully stowed.

        Args:
            percent (float, deg): The percent position to move the fork lift to.
            speed (float, mm/s): The speed to move the fork lift at. Defaults to 120.
        """
        # Gate to between 0 and 100
        percent = min(max(percent, 0), 100)
        assert self._back_motor_upper is not None
        assert self._back_motor_lower is not None
        target = int(self._back_motor_lower + (
            self._back_motor_upper - self._back_motor_lower) * percent * .01)
        self._queue.append((self._motors['back'].run_target, (speed, target,), {}))

    def fork_lift_stow(self, speed=500):
        """
        Stow the fork lift.

        Args:
            speed (int, optional): The speed at which to move the fork lift. Defaults to 500.
        """
        self._queue.append((self._motors['back'].run_target, (speed, self._back_motor_upper), {}))

    def fork_lift_up(self, speed=500):
        """
        Raise the fork lift.

        Args:
            speed (int, optional): The speed at which to move the fork lift. Defaults to 500.
        """
        self._queue.append((self._motors['back'].run_target, (speed, self._back_motor_up), {}))

    def fork_lift_lower(self, speed=500):
        """
        Lower the fork lift.

        Args:
            speed (int, optional): The speed at which to move the fork lift. Defaults to 500.
        """
        self._queue.append((self._motors['back'].run_target, (speed, self._back_motor_lower), {}))

    def curve(self, radius: float, angle: float, then: Stop = Stop.HOLD):
        """
        Drives an arc along a circle of a given radius, by a given angle.

        Args:
          radius (Number, mm): Radius of the circle.
          angle (Number, deg): Angle along the circle.
          then: What to do after coming to a standstill.
        """
        self._queue.append((self._drive_base.curve, (radius, angle, then), {}))

    @robot_api
    async def drive(self, distance: float, speed: int=STRAIGHT_SPEED):
        """
        Drive a set distance in a straight line.

        Args:
          distance (Number, mm): The distance to travel.  Positive to drive forwards,
            negative to drive backwards.
          speed (Number, mm/s): The speed at which to drive.
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

    @robot_api
    async def initialize(self):
        """
        Initialize robot.

        This determines the min/max rotation of the front and back motors.  This
        should be run once then not again until the motor gears have slipped.
        """
        await multitask(
            self._motors['back'].run_until_stalled(200, then=Stop.HOLD),
            self._motors['front'].run_until_stalled(200, then=Stop.HOLD))
        backoff = 5
        await self._motors['back'].run_until_stalled(200, then=Stop.HOLD)
        self._back_motor_lower = self._motors['back'].angle() - backoff
        await self._motors['back'].run_until_stalled(-200, then=Stop.HOLD)
        self._back_motor_upper = self._motors['back'].angle() + backoff
        self._back_motor_up = self._back_motor_upper + 170
        await self._motors['back'].run_target(200, self._back_motor_up)
        await self._motors['front'].run_until_stalled(200, then=Stop.HOLD)
        self._front_motor_lower = self._motors['front'].angle() - backoff
        await self._motors['front'].run_until_stalled(-200, then=Stop.HOLD)
        self._front_motor_upper = self._motors['front'].angle() + backoff
        self._front_motor_up = self._front_motor_upper + 160
        await self._raise_all()
        self._save_persistent_data()

    def menu(self, *runs):
        run_task(self._menuandlog(*runs))

    async def _menuandlog(self, *runs):
        await multitask(
            self._menu(*runs),
            self._logit())

    async def _process_queue(self):
        for callable, args, kwargs in self._queue:
            await callable(*args, **kwargs)
        self._queue[:] = []

    async def _logit(self):
        while True:
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

    async def _menu(self, *runs):

        index = 0
        num_choices = len(runs)

        while True:
            self._display_item(str(index + 1))
            pressed = self._hub.buttons.pressed()
            if Button.CENTER in pressed:
                self._hub.display.icon(Icon.HEART)
                runs[index]()
                await self._process_queue()
                for motor in self._motors.values():
                    motor.stop()
            elif Button.LEFT in pressed:
                index = (index - 1) % num_choices
                await wait(300)  # Debounce
            elif set([Button.RIGHT]) == pressed:
                index = (index + 1) % num_choices
                await wait(300)  # Debounce
            await wait(10)

    def _display_item(self, item):
        if isinstance(item, str):
            self._hub.display.char(item)
        elif isinstance(item, int):
            self._hub.display.number(item)
        else:
            raise ValueError("Items must be str or int")

    def _save_persistent_data(self):
        data = {member: getattr(
            self, member) for member in self._persistent_data}
        payload = bytes(json.dumps(data), 'utf-8')
        header = struct.pack(HEADER_FORMAT, len(payload))
        self._hub.system.storage(offset=0, write=header + payload)

    def _load_persistent_data(self):
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
            if member in persistent_data:
                setattr(self, member, persistent_data[member])

    async def _raise_all(self, speed=500):
        await multitask(
            self._motors['back'].run_target(speed, self._back_motor_up),
            self._motors['front'].run_target(speed*.25, self._front_motor_up))

    async def _stow_all(self, speed=500):
        await self._raise_all(speed)
        await multitask(
            self._motors['back'].run_until_stalled(-200, then=Stop.HOLD),
            self._motors['front'].run_until_stalled(-200, then=Stop.HOLD))

    async def _lower_all(self, speed=500):
        await multitask(
            self._motors['back'].run_target(speed, self._back_motor_lower),
            self._motors['front'].run_target(speed, self._front_motor_lower))

    async def _lower_plow_stow_fork_lift(self, speed=500):
        await self._raise_all()
        await multitask(
            self._motors['back'].run_target(speed, self._back_motor_upper),
            self._motors['front'].run_target(speed, self._front_motor_lower))

    async def _lower_fork_lift_stow_plow(self, speed=500):
        await self._raise_all()
        await multitask(
            self._motors['back'].run_target(speed, self._back_motor_lower),
            self._motors['front'].run_target(speed, self._front_motor_upper))
