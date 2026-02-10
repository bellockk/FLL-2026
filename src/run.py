from robot import Robot
robot = Robot()


def run1():
    # Pre-Run Initialization (Get Motor Endpoints for up and down)
    robot.initialize()

    # Prepare for Run 2
    robot.plow(47)
    robot.fork_lift(56)

def run2():
    # Drive out of starting area
    robot.plow(65)
   # robot.drive(-10)
    robot.drive(845,1000)

    # Drive to Careful Recovery
    robot.turn(-89)
    robot.drive(55,50)
    robot.fork_lift(8)

    # Careful Recovery
    robot.drive(-115,50)
    robot.fork_lift(19)
    robot.plow(30)
    robot.drive(160,100)
    robot.fork_lift(51)

    # Remove Topsoil Section from Map Reveal
    robot.turn(7)
    robot.plow(50)
    robot.drive(-30)
    robot.turn(25)
    robot.plow(35)
    robot.drive(57,50)
    robot.plow(85,50)

    # Complete Mineshaft Explorer
    robot.drive(-60)
    robot.turn(-56)

    # Drive to Statue Rebuild
    robot.turn(62)
    robot.fork_lift(33)
    robot.plow(99)
    robot.drive(-170,50)

    # Statue Rebuild
    robot.fork_lift(60)
    robot.plow(48)

    # Drive Off Mat
    robot.drive(150, 1000)
    robot.turn(79)
    robot.drive(-365, 1000)
    robot.turn(-25)
    robot.drive(-435, 1000)
    robot.plow(60)
    robot.fork_lift(60)

def run3():
    # Drop Pieces off at the Forum and Flag
    robot.plow(44)
    robot.drive(190,1000)
    robot.turn(44)
    robot.drive(235,500)
    robot.drive(-40,100)
    robot.plow(60)

    # Drive to Angler Artifacts
    robot.drive(-220,1000)
    robot.turn(-113)
    robot.drive(-190,1000)
    robot.fork_lift(50)
    robot.plow(85)
    robot.drive(107, 1000)
    robot.drive(-105, 1000)
    robot.fork_lift(77)
    robot.turn(-20)
    robot.drive(-200, 1000)
    robot.fork_lift(47)
    robot.turn(20)

    # Raise Artifact above the ground layer
    robot.drive(70,1000)
    robot.drive(-70)
    robot.drive(70,1000)
    robot.drive(-70)
    robot.drive(90,1000)
    robot.drive(-20,1000)

    # Drive to Right Starting Area
    robot.turn(-20)
    robot.drive(20)
    robot.raise_all(1000)
    robot.drive(-300, 1000)

def run4():
    # Drive to What's on Sale? (Wares)
   # robot.raise_all(1000)
    robot.fork_lift(20)
    robot.drive(-237)

    # Raise Market Wares
    robot.turn(-17)

    # Tip scale so it touches the mat
    robot.fork_lift(10)

    # Raise the roof on What's for Sale
    robot.drive(-115)

    # Ensure Raise Market Wares is Touching the mat
    robot.fork_lift(40)
    robot.turn(7)
    robot.plow(100)

    # Raise the roof on What's for Sale?
    robot.drive(164)

    # Unhook the fork lift from What's for Sale's Roof
    robot.drive(-10)

    # Drive to Who Lived Here
    robot.plow(60,500)
    robot.drive(40)
    robot.turn(47)
    robot.drive(-312,1000)
    robot.fork_lift(5)

    # Upright structure floor
    robot.turn(18)
    robot.drive(40)
    robot.fork_lift(40)
    robot.drive(-80)
    robot.plow(78)
    robot.turn(35)
    robot.raise_all(1000)
    robot.drive(20)
    robot.turn(-53)
    robot.drive(-160)
    robot.turn(-15)
    robot.drive(100)
    robot.turn(12)
    robot.drive(500)
   # robot.turn(-17)
   # robot.drive(100)
   # robot.turn(5)
   # robot.fork_lift(40,1000)

    # Drive to Forge
   # robot.drive(-80)
   # robot.turn(25)
   # robot.drive(70)

    # Heavy Lifting
   # robot.turn(15)
   # robot.plow(78)
   # robot.turn(30)
   # robot.plow(70)

    # Drive to Right Launch Area
  #  robot.drive(25,1000)
  #  robot.turn(-75)
  #  robot.drive(700,1000)
  #  robot.raise_all(500)

def run5():
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
robot.menu(run1, run2, run3, run4, run5)
