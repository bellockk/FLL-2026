from robot import Robot
robot = Robot()

def run1():
    # Pre-Run Initialization (Get Motor Endpoints for up and down)
    robot.initialize()

    ## Precision Tokens 50pts

    ## Equipment Inspection 20pts

    ## 0s 70pts  0deg is West

def run2():

    robot.fork_lift(50)
    robot.plow(57)
    robot.plow(55)
    robot.drive(630)
    robot.turn(-150)
    robot.drive(-50)
    robot.curve(-250, -40)
    robot.turn(35)
    robot.plow(45)
    robot.drive(110)
    robot.plow(60)
    robot.turn(-12)
    robot.fork_lift(10)
    robot.drive(-110)
    robot.fork_lift(20)
    robot.drive(105)
    robot.fork_lift(40)
    robot.turn(11)
    robot.fork_lift(10)
    robot.drive(-110)
    robot.fork_lift(50)
    robot.fork_lift(35)
    robot.turn(30)
    robot.plow(95)
    robot.drive(-100)
    robot.plow(50)
    robot.drive(100)
    robot.turn(75)
    robot.drive(-650)

def run3():
    # Drive from Left Home to Salvage Operation
    robot.fork_lift(35)
    robot.plow(60)
    robot.drive(-370)
    robot.plow(85)
    robot.turn(8)
    robot.drive(40)
    robot.drive(-40)
    robot.drive(40)
    robot.drive(-40)
    robot.drive(40)
    robot.turn(-8)
    robot.fork_lift(50)
    robot.turn(12)
    robot.drive(200)
    robot.fork_lift(47)
    robot.drive(-155)
    robot.fork_lift(60)
    robot.turn(-25)
    robot.drive(-550)
    robot.turn(20)
    robot.drive(-900)


    # Salvage Operation (30pts)

    # Site Marking (10pts)

    # Drive from Salvage Operation to Angler Artifacts

    # Angler Artifacts (30pts)

    # Drive from Angler Artifacts to Tip the Scales

    # Tip the Scales (30pts)

    # Drive from Tip the Scales to What's on Sale

    # What's on Sale (30pts)

    # Drive from What's on Sale to Right Home
    # Remove Scale Pan

    # XXXs 130pts (350pts Total)



def run4():
    # Drive to What's on Sale? (Wares)
    robot.plow(50)
    robot.fork_lift(15)
    robot.drive(-235)

    # Raise Market Wares
    robot.turn(-14)

    # Tip scale so it touches the mat
    robot.fork_lift(20)

    # Raise the roof on What's for Sale
    robot.drive(-105)

    # Ensure Raise Market Wares is Touching the mat
    robot.plow(90)
    robot.turn(2)
    robot.fork_lift(15)

    # Raise the roof on What's for Sale?
    robot.drive(174)

    # Unhook the fork lift from What's for Sale's Roof
    robot.fork_lift(22)
    robot.drive(-70)

    # Drive to Who Lived Here
    robot.plow(60)
    robot.turn(56)
    robot.drive(-310)

    # Upright structure floor
    robot.turn(-17)

    # Drive to Forge
    robot.drive(30)
    robot.fork_lift(0)
    robot.turn(40)
    robot.drive(95)
    robot.turn(-10)
    robot.fork_lift(40)

    # Release Ore Blocks from Forge
    robot.turn(14)

    # Heavy Lifting
    robot.plow(78)
    robot.drive(-120)
    robot.plow(50)

    # Drive off mat
    robot.turn(-22)
    robot.drive(700)


    # robot.turn(-17)
    # robot.drive(-35)
    # robot.plow(99)
    # robot.turn(-40)
    # robot.plow(50)
    # robot.fork_lift(50)
    # robot.drive(-90)
    # robot.turn(120)
    # robot.fork_lift(22)
    # robot.drive(-325)

    # robot.turn(-15)
    # robot.drive(30)
    # robot.fork_lift(0)
    # robot.turn(43)
    # robot.drive(95)
    # robot.turn(-10)
    # robot.fork_lift(40)
    # robot.turn(8)
    # robot.plow(76)
    # robot.drive(-120)
    # robot.plow(50)
    # robot.turn(-22)
    # robot.drive(580)


    # Site Marking (10pts)

    # Drive from Site Marking Opposing Team's Minecart

    # Obtain Opposing Team's Minecart

    # Drive from Opposing Team's Minecart to Statue Rebuild

    # Statue Rebuild (30pts)

    # Drive from Statue to Forum

    # Forum (35pts)

    # Move away from Forum so no pieces are touching robot

    # XXXs 75pts (545pts Total)


    # Drive from Site Marking Opposing Team's Minecart

    # Obtain Opposing Team's Minecart

    # Drive from Opposing Team's Minecart to Statue Rebuild

    # Statue Rebuild (30pts)

    # Drive from Statue to Forum

    # Forum (35pts)

    # Move away from Forum so no pieces are touching robot

    # XXXs 75pts (545pts Total)

def run5():
    robot.plow(60)
    robot.fork_lift(50)
    robot.fork_lift(20)
    robot.drive(-620)
    robot.turn(-22)
    robot.drive(30)
    robot.fork_lift(0)
    robot.turn(43)
    robot.drive(95)
    robot.turn(-10)
    robot.fork_lift(40)
    robot.turn(8)
    robot.plow(76)
    robot.drive(-120)
    robot.plow(50)
    robot.turn(-22)
    robot.drive(580)


def run6():
    robot.fork_lift(80)
    robot.drive(-225)
    robot.fork_lift(80, 2000)
    robot.fork_lift(10, 2000)
    robot.fork_lift(80, 2000)
    robot.fork_lift(10, 2000)
    robot.fork_lift(80, 2000)

def run7():
    # Drive from Right Home to Silo
    robot.plow(55)
    robot.fork_lift(50)
    robot.turn(13)
    robot.drive(620)
    robot.turn(-13)
    robot.drive(1100)


    # Silo (30pts)

    # Drive from Silo to Forge

    # Forge (30pts)

    # Heavy Lifting (30pts)

    # Push Boulders off table

    # Drive from Boulder Push to Who Lived Here

    # Who Lived Here (30pts)

    # Drive from Who Lived Here to Right Home
    # Load all Forum Artifacts collected so far
    # Load Site Marker

    # XXXs 120pts (470pts Total)

def run8():
    robot.drive(658)
    robot.turn(-35)
    robot.drive(115)
    robot.drive(-90)

def run9():
    robot.drive(100)


# !! DO NOT REMOVE THE FOLLOWING LINES !!
robot.menu(run1, run2, run3, run4, run5, run6, run7, run8, run9)
