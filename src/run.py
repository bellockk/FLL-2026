from robot import Robot
robot = Robot()


def run1():
    # Pre-Run Initialization (Get Motor Endpoints for up and down)
    robot.initialize()

    # Prepare for Run 2
    robot.front_lift(47)
    robot.back_lift(56)

def run2():
    # Drive out of starting area
    robot.front_lift(60)
    robot.drive(-10)
    robot.drive(810,1000)

    # Drive to Careful Recovery
    robot.turn(-49)
    robot.drive(60)
    robot.back_lift(13)
    robot.turn(-45)

    # Careful Recovery & Complete Mineshaft Explorer
    robot.drive(-115,40)
    robot.front_lift(50)
    robot.back_lift(22,50)
    robot.drive(155,40)
    robot.back_lift(55,100)
    robot.back_lift(33)

    # Remove Topsoil Section from Map Reveal
    robot.turn(16)
    robot.front_lift(57)
    robot.drive(-30)
    robot.turn(29)
    robot.front_lift(45)
    robot.drive(40,50)
    robot.front_lift(95,50)

    # Drive to Statue Rebuild
    robot.drive(-240,50)

    # Statue Rebuild
    robot.back_lift(65,1000)
    robot.front_lift(70,1000)

    # Brush Pick Up & Drive Off Mat
    robot.drive(140)
    robot.turn(86)
    robot.drive(-106, 1000)
    robot.turn(-19)
    robot.drive(-100)
    robot.front_lift(40,50)
    robot.drive(-143, 1000)
    robot.turn(-15)
    robot.drive(-530,1000)
    robot.front_lift(60)
    robot.back_lift(60)

def run3():
    # Drop Pieces off at the Forum and Flag
    robot.front_lift(44)
    robot.drive(-10)
    robot.drive(190,1000)
    robot.turn(44)
    robot.drive(245,500)
    robot.drive(-40,100)
    robot.front_lift(60)

    # Drive to Angler Artifacts
    robot.drive(-208,1000)
    robot.turn(-112)
    robot.drive(-144,1000)
    robot.back_lift(49)
    robot.front_lift(85)
    robot.drive(71, 1000)
    robot.drive(-100, 1000)
    robot.back_lift(75)
    robot.turn(-20)
    robot.drive(-170, 1000)
    robot.back_lift(50)
    robot.turn(20)

    # Raise Artifact above the ground layer
    robot.drive(70,1000)
    robot.drive(-70)
    robot.drive(70,1000)
    robot.drive(-70)
    robot.drive(70,1000)
    robot.drive(-70)
    robot.drive(70,1000)
    robot.drive(-70)
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
    robot.drive(-1300, 1000)

def run4():
    # Drive to What's on Sale? (Wares)
    robot.raise_all(1000)
    robot.front_lift(50)
    robot.back_lift(19)
    robot.drive(-237)

    # Raise Market Wares
    robot.turn(-17)

    # Tip scale so it touches the mat
    robot.back_lift(10)

    # Raise the roof on What's for Sale
    robot.drive(-93)

    # Ensure Raise Market Wares is Touching the mat
    robot.back_lift(40)
    robot.turn(7)
    robot.front_lift(95)

    # Raise the roof on What's for Sale?
    robot.drive(175)

    # Unhook the fork lift from What's for Sale's Roof
    robot.drive(-25)

    # Drive to Forge
    robot.front_lift(60,500)
    robot.drive(40)
    robot.turn(42)
    robot.drive(-350,1000)

    # Heavy Lifting
    robot.back_lift(55)
    robot.front_lift(85)
    robot.turn(52)
    robot.front_lift(50,1000)
    robot.turn(-48)

    # Drive to Who Lived Here
    robot.drive(-168,50)

    # Drive to Right Launch Area
    robot.turn(-27)
    robot.turn(35)
    robot.drive(760,1000)
    robot.turn(50)

def run5():
  robot.front_lift(0, 1000)
  robot.front_lift(60,1000)
  robot.front_lift(0,1000)
  robot.front_lift(60,1000)
  robot.front_lift(0,1000)
  robot.front_lift(65,1000)

def run6():
    # Drive from Right Launch Area to Tip the Scales
    robot.raise_all(500)
    robot.front_lift(65, 50)
    robot.drive(-270,1000)
    robot.turn(37)
    robot.drive(-160,1000)
    robot.back_lift(5)

    # Remove the Scale Pan
    robot.turn(-22)
    robot.turn(5)

    # Drive to Forum
    robot.drive(-465,1000)
    robot.back_lift(55)
    robot.turn(95)
    robot.drive(235,1000)
    robot.front_lift(35,200)
    robot.drive(-120,1000)

# !! DO NOT REMOVE THE FOLLOWING LINES !!
robot.menu(run1, run2, run3, run4, run5, run6)
