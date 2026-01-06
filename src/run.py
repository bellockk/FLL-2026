from robot import Robot
robot = Robot()

def run1():
    # Pre-Run Initialization (Get Motor Endpoints for up and down)
    robot.initialize()

    ## Precision Tokens 50pts

    ## Equipment Inspection 20pts

    ## 0s 70pts  0deg is West

def run2():

    robot.plow(55)
    robot.plow(50)
    robot.drive(720)
    robot.drive(-50)
    robot.turn(-135)
    robot.drive(-130)
    robot.turn(34)
    robot.fork_lift(10)
    robot.drive(-105)
    robot.fork_lift(18)
    robot.drive(110)
    robot.fork_lift(40)
    robot.turn(15)
    robot.fork_lift(10)
    robot.drive(-100)
    robot.fork_lift(40)
    robot.drive(50)
    robot.turn(27)
    robot.plow(90)
    robot.drive(-80)
    robot.plow(45)
    robot.drive(150)
    robot.plow(60)
    robot.turn(75)
    robot.plow(50)
    robot.drive(-550)

def run3():
    # Drive from Left Home to Salvage Operation
    robot.fork_lift(35)
    robot.plow(60)
    robot.drive(-230)
    robot.plow(80)
    robot.drive(200)
    robot.plow(70)
    robot.drive(-130)
    robot.plow(80)
    robot.drive(-100)
    robot.plow(60)
    robot.drive(100)
    robot.turn(-45)
    robot.drive(-220)
    robot.turn(45)
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
    # Drive from Right Home to Site Marking
    robot.plow(50)
    robot.fork_lift(50)
    robot.fork_lift(15)
    robot.drive(-285)
    robot.turn(-60)
    robot.fork_lift(25)
    robot.drive(-110)
    robot.plow(75)
    robot.turn(3)
    robot.fork_lift(5)
    robot.plow(90)
    robot.drive(170)
    robot.drive(-40)
    robot.plow(60)
    robot.turn(-20)
    robot.drive(-28)
    robot.plow(90)
    robot.turn(-40)
    robot.plow(50)
    robot.fork_lift(50)
    robot.drive(100)
    robot.turn(-45)
    robot.drive(-180)

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
    robot.fork_lift(50)
    robot.drive(-225)
    robot.fork_lift(50)
    robot.fork_lift(5)
    robot.fork_lift(50)

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


# !! DO NOT REMOVE THE FOLLOWING LINES !!
robot.menu(run1, run2, run3, run4, run5, run6, run7)

robot.fork_lift(50)
robot.fork_lift(15)
robot.fork_lift(50)