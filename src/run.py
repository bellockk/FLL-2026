from robot import Robot
robot = Robot()

# robot.curve(300, 85)  #  Forwards right
# robot.curve(1000, -20)  #  Forwards left
# robot.curve(-1000, -20)  #  Backwards right
# robot.curve(-1000, 20)  #  Backwards left

def run1():
    # Pre-Run Initialization (Get Motor Endpoints for up and down)
    robot.initialize()

    # Prepare for Run 2
    robot.raise_all(1000)


def run2():
    # Drive from Left for the Final Run (30 points)
     robot.plow(48)
     robot.drive(400,800)
     robot.plow(90)
     robot.drive(250,800)
     robot.plow(60)
     robot.drive(173)
     robot.turn(-91.5)
     robot.drive(50)
     robot.fork_lift(8)
     robot.drive(-100,50)
     robot.fork_lift(18)
     robot.plow(47)
     robot.drive(130,50)
     robot.fork_lift(45)
     robot.plow(65)
     robot.turn(10)
     robot.drive(-90,500)
     robot.plow(85)
     robot.turn(-35)
     robot.turn(72)
     robot.fork_lift(40)
     robot.plow(95)
     robot.drive(-115,500)
     robot.turn(-12)
     robot.plow(70)
     robot.fork_lift(48)
     robot.drive(100,800)
     robot.turn(82)
     robot.plow(90)
     robot.drive(-360)
     robot.turn(-30)
     robot.raise_all(500)
     robot.drive(-400,1000)


def run3():
   # robot.curve(600, 30)  #  Forwards right
    robot.drive(540, 1000)
    robot.curve(300, -40)  #  Forwards left
    robot.drive(-50)
    robot.curve(-500, -90)  #  Backwards right


def run4():
    # Drive from Left for the Final Run (30 points)
    robot.plow(44)
    robot.drive(190,1000)
    robot.turn(44)
    robot.drive(235,500)
    robot.drive(-40,100)
    robot.plow(60)
    robot.drive(-100,1000)
    robot.turn(-45)
    robot.drive(-200,1000)
    robot.turn(-90)
    robot.drive(-240,1000)
    robot.fork_lift(46)
    robot.plow(85)
    robot.turn(20)
    robot.drive(70,1000)
    robot.drive(-70)
    robot.drive(70,1000)
    robot.drive(-70)
    robot.drive(90,1000)
    robot.drive(-20,1000)
    robot.turn(-20)
    robot.drive(95)
    robot.turn(22)
    robot.fork_lift(49)
    robot.drive(140,1000)
    robot.fork_lift(47)
    robot.drive(-127,1000)
    robot.raise_all(1000)
    robot.turn(-35)
    robot.drive(-400,1000)
    robot.turn(37)
    robot.drive(-1000,1000)


def run5():
    # Drive to What's on Sale? (Wares)
    robot.raise_all(1000)
    robot.fork_lift(19)
    robot.drive(-237)

    # Raise Market Wares
    robot.turn(-17)

    # Tip scale so it touches the mat
    robot.fork_lift(10)

    # Raise the roof on What's for Sale
    robot.drive(-105)

    # Ensure Raise Market Wares is Touching the mat
    robot.fork_lift(30)
    robot.turn(7)
    robot.plow(95)

    # Raise the roof on What's for Sale?
    robot.drive(174)

    # Unhook the fork lift from What's for Sale's Roof
    robot.drive(-70)

    # Drive to Who Lived Here
    robot.plow(60)
    robot.turn(55)
    robot.fork_lift(22)
    robot.drive(-308)

    # Upright structure floor
    robot.turn(-17)

    # Drive to Forge
    robot.drive(30)
    robot.fork_lift(5)
    robot.turn(40)
    robot.drive(93)
    robot.turn(-9)
    robot.fork_lift(35)

    # Release Ore Blocks from Forge
    robot.turn(12)

    # Heavy Lifting
    robot.plow(78)
    robot.drive(-150,50)
    robot.raise_all(1000)

    # Drive to Right Launch Area
    robot.drive(100,1000)
    robot.turn(-24)
    robot.drive(650,1000)


def run6():
    # # Drive from Right Launch Area to Tip the Scales
    robot.plow(70)
    robot.drive(-270,1000)
    robot.turn(39)
    robot.drive(-166,1000)
    robot.fork_lift(5)
    robot.turn(-22)
    robot.drive(-480,1000)
    robot.fork_lift(50)
    robot.turn(-176)
    robot.drive(210,1000)
    robot.plow(40)
    robot.plow(50)
    robot.drive(-130,1000)
    robot.turn(-45)
    robot.drive(850,1000)


def run7():
    robot.raise_all(300)
    robot.drive(-450,1000)
    robot.turn(20)
    robot.fork_lift(40,50)
    robot.drive(300)


# !! DO NOT REMOVE THE FOLLOWING LINES !!
robot.menu(run1, run2, run3, run4, run5, run6, run7)
