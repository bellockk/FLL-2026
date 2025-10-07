from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase

# Define objects for a simple two motor rover using a DriveBase
hub = InventorHub()
hub.speaker.beep()

motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
motor.run_angle(90, 360)
motor.run_angle(-90, 360)

