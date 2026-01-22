from robot import Robot
robot = Robot()

def run1():
    # Pre-Run Initialization (Get Motor Endpoints for up and down)
    robot.initialize()

    # Prepare for Run 2
    robot.raise_all(1000)


def run2():
    # Drive from Left for the Final Run (30 points)
     robot.raise_all(400)
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
     robot.plow(80)
     robot.drive(-260)
#    robot.raise_all(1000)
 #   robot.drive(610,700)
  #  robot.turn(-21)
   # robot.drive(145,700)
    #robot.turn(-36)
    #robot.raise_all(1000)


def run3():
    # Drive from Left Home to Salvage Operation
    robot.fork_lift(60)
    robot.plow(95)
    robot.drive(-230,700)

    # Clear the Sand
    robot.fork_lift(48)
    robot.drive(130,700)

    # Raise Ship
    robot.fork_lift(38)
    robot.drive(-100)

    # Drive to Right Launch Area
    robot.plow(60)
    robot.turn(-30)
    robot.drive(-500,1000)
    robot.turn(38)
    robot.raise_all(1000)
    robot.drive(-1000,1000)

    # Angler Artifacts
    angler_artifacts()  # <-- Comment just this line to remove angler artifacts


def angler_artifacts():
    robot.fork_lift(35)
    robot.plow(60)
    robot.drive(-370)
    robot.plow(85)
    robot.turn(8)
    robot.drive(43)
    robot.drive(-43)
    robot.drive(43)
    robot.drive(-43)
    robot.drive(43)
    robot.turn(-8)
    robot.fork_lift(50)
    robot.turn(13)
    robot.drive(200)
    robot.fork_lift(48)
    robot.drive(-155)
    robot.fork_lift(60)
    robot.turn(-27)
    robot.drive(-550)
    robot.turn(22)
    robot.drive(-900)


def run4():
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


def run5():
    # Drive from Right Launch Area to Tip the Scales
    robot.raise_all(1000)
    robot.drive(-400,700)

    # Remove the Scale Pan
    robot.fork_lift(8)
    robot.turn(-25)

    # Drive to Left Launch Area
    robot.drive(-1350,1000)
    robot.raise_all(1000)


def run6():
    # Drive from Left for Artifact Drop
    robot.raise_all(1000)
    robot.drive(410,700)
    robot.plow(75,700)

    # Return to Left Launch Area
    robot.drive(-410,1000)
    robot.raise_all(1000)


def run7():
    # Drive from Left for the Final Run (30 points)
    robot.raise_all(1000)
    robot.drive(610,700)
    robot.turn(-21)
    robot.drive(145,700)
    robot.turn(-36)
    robot.raise_all(1000)

# !! DO NOT REMOVE THE FOLLOWING LINES !!
robot.menu(run1, run2, run3, run4, run5, run6, run7)
