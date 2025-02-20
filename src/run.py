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
    robot.turn(-117)       # -45
    robot.lower_plow_stow_fork_lift()
    robot.drive(300)
    robot.turn(-45)       # -90
    robot.curve(300, 30)  # -120
    robot.curve(100, -30) # -90
    robot.drive(80)
    robot.turn(-90 - 45)  # -225
    robot.curve(200, 45)  # -185
    robot.drive(200)

    # s 144pts

    # Change Shipping Lanes (s 20pts)
    robot.lower_fork_lift_stow_plow()
    robot.curve(-400, 45) # -230
    robot.turn(90)        # -140
    robot.drive(-50)
    robot.plow(25)
    robot.fork_lift_stow()

    # s 164pts

    # Reveal East Whale (s 20pts)
    robot.turn(-15)      # -155
    robot.drive(170)
    robot.plow(20, 500)
    robot.curve(-400, 25) #  -180
    robot.drive(-40)
    robot.drive(40)

    # s 184pts

    # Collect Plankton Sample (s 10pts)
    robot.fork_lift_lower()

    # s 194pts

    # Send over the Submersible (s 30pts)
    robot.plow(40, 300)
    robot.curve(100, -45)  #  -150
    robot.curve(200, 45)  #  -180
    robot.plow_lower()
    robot.drive(125)
    robot.curve(100, 40)  #  -180

    # s 224pts

    #  Angler Fish (s 30pts)
    robot.curve(200, -85)  #  -180
    robot.curve(100, 70)  #  -180
    robot.curve(100, -25)  #  -180

    # s 254pts

    # Drive Off Board with Krill, samples, and Coral Tree (s -10pts)
    robot.drive(100)
    robot.curve(400, -70)
    #robot.drive(300)
    # robot.curve(800, 70)


    # s 244pts



def run3():
    # Get Trident Piece and Krill (20pts)
    pass

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
    robot.turn(45)
    robot.drive(300)
    #TODO: Drive Off Matt

    # s 454pts

    # Collect Seabed Sample (s 10pts)

    # s 384pts

    # Flip up Coral Reef (s 20pts)

    # s 434pts

    # Shark (s 20pts)

    # s 414pts


def run5():
    # Coral Reef Segments (s 15pts)
    robot.wait(500)
    robot.drive(-80, 50)

    ## s 344pts

    # Sample Dump (s 15pts)
    robot.fork_lift(70)
    robot.fork_lift(-70)

def run6():

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

def run7():

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

    # s 609s


# !! DO NOT REMOVE THE FOLLOWING LINES !!
singlerun = False
if singlerun:
    run1()
    robot.run()
    run2()
    robot.run()
else:
    robot.menu(run1, run2, run3, run4, run5, run6)
