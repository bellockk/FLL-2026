from robot import Robot

robot = Robot()

def run1():
    # Pre-Run Initialization/Calibration
    robot.initialize()
    robot.raise_all()

    ## 0s 89pts  0deg is West

def run2():
    # Drive Up to the Artificial Habitat
    robot.lower_fork_lift_stow_plow()
    robot.fork_lift(15)
    robot.drive(-100)
    robot.curve(-450, 25)  # -25deg

    # Fold Artificial Habitat
    robot.turn(35)         #  10deg
    robot.drive(-100)
    robot.drive(80)
    robot.turn(-10)        #   0deg

    # Flip Artificial Habitat (s 40pts)
    robot.fork_lift(0)
    robot.drive(-150)
    robot.drive(20)
    robot.fork_lift_stow(2000)

    ## s 129pts

    # Release the Unknown Creature (s 20pts)
    robot.turn(72)         #  72
    robot.drive(-180)

    ## s 149pts

    # Collect Krill and Coral Segment (s -5pts)
    robot.drive(30)
    robot.turn(-132)       # -60
    robot.lower_plow_stow_fork_lift()
    robot.drive(480)
    robot.turn(-33)       # -93
    robot.drive(70)
    robot.turn(-117)      # -210
    robot.drive(100)
    robot.turn(30)      # -180
    robot.drive(200)

    # Reveal East Whale (s 20pts)
    robot.plow_up()
    robot.drive(-215)
    robot.turn(90)         # -90
    robot.drive(155)
    robot.plow(19, 500)
    robot.drive(-125)
    robot.plow_up()

    # Change Shipping Lanes (s 20pts)
    robot.turn(45)         # -45
    robot.drive(60)
    robot.turn(-92)        # -137
    robot.drive(80)
    robot.fork_lift_lower()
    robot.drive(-70)
    robot.fork_lift_stow()

    # Collect Plankton Sample (s 10pts)
    robot.turn(-47)    # -184
    robot.drive(-70)
    robot.drive(30)
    robot.fork_lift_lower()

    #  Angler Fish (s 30pts)
    robot.turn(-6)     # -190
    robot.drive(200)
    robot.plow_lower()
    robot.drive(420)
    robot.turn(10)     # -180
    robot.drive(80)
    robot.drive(-20)
    robot.turn(15)     # -180
    robot.drive(150)
    robot.turn(-15)     # -180
    robot.drive(150)
    robot.curve(350, -90)
    robot.curve(300, 90)
    robot.raise_all()

def run3():

    # Get Reef
    robot.turn(95)
    robot.drive(290)
    robot.turn(-5)
    robot.plow(15)
    robot.drive(-290)
    robot.turn(-161)
    robot.plow_up()
    robot.drive(-550)
    robot.turn(-65)
    robot.fork_lift_lower()
    robot.fork_lift_up()
    robot.turn(65)
    robot.drive(600)
    robot.turn(75)

def run4():
    # Hang Coral Tree (s 20pts)
    robot.fork_lift(60)
    robot.turn(-97)
    robot.drive(-250)
    robot.fork_lift(50)

    # s 324pts

    # Raise the Mast (s 30pts)
    robot.drive(150)
    robot.turn(50)
    robot.drive(-420)
    robot.turn(227)
    robot.plow_lower()
    robot.drive(260)

    # Kraken's Treasure (s 20pts)
    robot.drive(-200)

    # Flip Coral Buds up (s 20pts)
    robot.plow(50)
    robot.turn(-45)
    robot.drive(140)
    robot.turn(45)
    robot.drive(-120)

    # s 344pts

    # Grab Scuba Dude (s 20pts)
    robot.fork_lift(55)

    # s 274pts

    # Drop Off Scuba Dude (s 20 pts)
    robot.curve(100, 88)
    robot.fork_lift(53)
    robot.drive(-100)
    robot.fork_lift(48)
    robot.drive(100)

    # Flip Coral Reef
    robot.fork_lift(38)
    robot.drive(-100)
    robot.fork_lift(15)
    robot.fork_lift(38)
    robot.drive(100)

    # Collect Seabed Sample (s 10pts)
    robot.turn(40)
    robot.fork_lift(40)
    robot.drive(-300)
    robot.fork_lift(90)
    robot.fork_lift(48)

    # Send the Submersible
    robot.turn(62)
    robot.drive(-450)
    robot.turn(-130)
    robot.turn(120)

    # Drive off the mat
    robot.drive(500)
    robot.curve(350, -90)
    robot.curve(300, 90)

    # s 454pts

def run5():
    robot.stow_all()

def run6():
    # Dump the goodies
    # Coral Reef Segments (s 15pts)
    robot.drive(-150, 100)

    # Sample Dump (s 15pts)
    robot.fork_lift(60)
    robot.fork_lift_stow()
    robot.drive(200, 50)
    robot.turn(-30)

def run7():

    # Drive Off Matt
    robot.drive(-200, 100)


def run8():

    # Dump Krill (s 50pts)
    robot.turn(80)
    robot.drive(-635)
    robot.turn(-125)
    robot.drive(100)
    robot.drive(60, 100)

    # s 589 pts

    # Reveal West Whale (s 10pts)
    robot.curve(-340, -100)
    robot.turn(-124)

    # s 599pts

    # Park on Unknown Creature in cold seep (10pts)
    robot.turn(20)
    robot.drive(-300)
    robot.fork_lift(10)

    # s 609s

def push_boat():

    # Push Boat to port latch (s 20pts)
    robot.turn(-2)
    robot.drive(300)
    robot.turn(-3)
    robot.drive(300)
    robot.drive(780, 140)
    robot.turn(40)
    robot.drive(200)
    robot.curve(200, 45)
    robot.turn(115)

    # s 539

def get_trident_handle():
    # Get Trident Handle (20pts)
    robot.drive(-385)
    robot.turn(-45)
    robot.fork_lift(30)
    robot.drive(-210)
    robot.fork_lift_up()

# !! DO NOT REMOVE THE FOLLOWING LINES !!
singlerun = False
if singlerun:
    run1()
    robot.run()
    run2()
    robot.run()
else:
    robot.menu(run1, run2, run3, run4, run5, run6, run7, run8)
