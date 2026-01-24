from robot import Robot
robot = Robot()


def run1():
    # Pre-Run Initialization (Get Motor Endpoints for up and down)
    robot.initialize()

    # Prepare for Run 2
    robot.plow(56)
    robot.fork_lift(56)


def run2():
    # Drive out of starting area
    robot.drive(400,800)

    # Configure for Surface Brushingrive from Left for the FIrst Run (30 points)
    robot.fork_lift(46)
    robot.plow(91)

    # Surface Brushing (First Pass)
    robot.drive(250,800)

    # Drive to Careful Recovery
    robot.plow(60)
    robot.drive(182)
    robot.turn(-89)
    robot.drive(65)
    robot.fork_lift(8)

    # Careful Recovery
    robot.drive(-112,50)
    robot.fork_lift(18)
    robot.plow(47)
    robot.drive(130,50)

    # Remove Topsoil Section from Map Reveal
    robot.fork_lift(47)
    robot.plow(65)

    # Complete Mineshaft Explorer
    robot.turn(10)
    robot.drive(-90,500)
    robot.plow(85)
    robot.turn(-38)

    # Drive to Statue Rebuild
    robot.turn(77)
    robot.fork_lift(41)
    robot.plow(95)
    robot.drive(-115,500)
    robot.turn(-17)

    # Statue Rebuild
    robot.fork_lift(48,1000)

    # Surface Brushing (Pass 2)
    robot.plow(70,1000)
    robot.drive(115,800)
    robot.turn(82)
    robot.plow(95)
    robot.fork_lift(50)
    robot.drive(-360)

    # Drive Off Mat
    robot.turn(-30)
    robot.raise_all(500)
    robot.drive(-510,1000)
    robot.plow(56)
    robot.fork_lift(56)

def run3():
    # Map Reveal
    robot.drive(540, 1000)
    robot.curve(300, -40)  #  Forwards left
    robot.drive(-50)
    robot.turn(38)
    robot.drive(-670,1000)


def run4():
    # Drop Pieces off at the Forum and Flag
    robot.plow(44)
    robot.drive(190,1000)
    robot.turn(44)
    robot.drive(235,500)
    robot.drive(-40,100)
    robot.plow(60)

    # Drive to Angler Artifacts
    robot.drive(-100,1000)
    robot.turn(-45)
    robot.drive(-200,1000)
    robot.turn(-90)
    robot.drive(-240,1000)
    robot.fork_lift(46)
    robot.plow(85)
    robot.turn(20)

    # Raise Artifact above the ground layer
    robot.drive(70,1000)
    robot.drive(-70)
    robot.drive(70,1000)
    robot.drive(-70)
    robot.drive(90,1000)
    robot.drive(-20,1000)

    # Remove Sand from Salvage Operation
    robot.turn(-20)
    robot.drive(95)

    # Raise the Ship
    robot.turn(15)
    robot.fork_lift(48)
    robot.drive(140,1000)

    # Drive to Right Starting Area
    robot.fork_lift(47)
    robot.drive(-127,1000)
    robot.raise_all(1000)


def run5():
    # Drive to What's on Sale? (Wares)
    robot.fork_lift(18)
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
    robot.turn(10)
    robot.turn(-20)

    # Heavy Lifting
    robot.drive(-90)
    robot.plow(78)
    robot.turn(45)
    robot.plow(70)

    # Drive to Right Launch Area
    robot.drive(75,1000)
    robot.turn(-80)
    robot.drive(600,1000)
    robot.raise_all(500)


def run6():
    # Drive from Right Launch Area to Tip the Scales
    robot.plow(65, 50)
    robot.drive(-270,1000)
    robot.turn(39)
    robot.drive(-166,1000)
    robot.fork_lift(5)

    # Remove the Scale Pan
    robot.turn(-22)

    # Drive to Forum
    robot.drive(-480,1000)
    robot.fork_lift(40)
    robot.turn(-45)
    robot.drive(-400)
    robot.turn(50)
    robot.plow(45, 100)
    robot.plow(60)

# !! DO NOT REMOVE THE FOLLOWING LINES !!
robot.menu(run1, run2, run3, run4, run5, run6)
