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
    robot.fork_lift(60)
    robot.turn(-97)
    robot.drive(-250)
    # robot.fork_lift(52)
    robot.fork_lift(50)
    robot.drive(150)
    robot.turn(50)
    robot.drive(-420)
    robot.turn(227)
    robot.plow_lower()
    robot.drive(260)
    robot.drive(-200)
    robot.plow(50)
    robot.turn(-45)
    robot.drive(140)
    robot.turn(45)
    robot.drive(-120)
    robot.fork_lift(55)
    robot.curve(100, 88)
    robot.fork_lift(53)
    robot.drive(-100)
    robot.fork_lift(48)
    #robot.turn(97)
    #robot.curve(-330, 140)

    # Hang Coral Tree (s 20pts)

    # s 324pts

    # Flip Coral Buds up (s 20pts)

    # s 344pts

    # Grab Scuba Dude (s 20pts)

    # s 364pts

    # Shark (s 20pts)

    # s 384pts

    # Raise the Mast (s 30pts)

    # s 414pts

    # Kraken's Treasure (s 20pts)

    # s 434pts

    # Drop Off Scuba Dude (s 20 pts)

    # s 454pts

    # Collect Seabed Sample (s 10pts)

    # s 274pts

    # Flip up Coral Reef (s 20pts)

    # s 294pts


def run4():
    pass

    # Drop Off Shark (s 10pts)

    # s 464pts

    # Get Trident Piece and Krill (20pts)

    # s 484
    # Push Coral Reef and fill Boat (35pts) 15pts coral + 20pts samples

def run5():

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

def run6():

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



def runA():
    # Align with crab trap
    robot.raise_all()
    robot.stow_all()
    robot.drive(100)
    robot.turn(135)
    robot.curve(380, -45)
    robot.fork_lift(250, 2000)

    # Drive Up to the crab trap
    robot.drive(-350)

    # Bend the middle joint and fold trap in half
    robot.turn(25)
    robot.drive(-150)

    # Lower the fork lift and get into position for the first flip
    robot.fork_lift(-45, 2000)
    robot.curve(300, -25)
    robot.fork_lift(70, 2000)
    robot.drive(-100)


def runA():
    # Drive to Sea Creature and Catch the creature (4s 20pts)
    robot.drive(140)
    robot.turn(-50)
    robot.drive(350)

    ## 4s 109pts

    #  Krill and Coral (6s -5pts)
    robot.drive(-240)
    robot.turn(50)
    robot.raise_all()
    robot.lower_plow_stow_fork_lift()
    robot.drive(400)

    ## 10s 104pts

    # Yellow Boat (18s 20pts)
    robot.drive(-300)
    robot.turn(-137)
    robot.drive(110)
    robot.fork_lift(340, 2000)
    robot.drive(-50)
    robot.fork_lift(-110)
    robot.turn(40)
    robot.fork_lift(-90, 2000)
    robot.turn(115)

    ## 20s 124pts

    # Sea Weed Sample (8s 10pts)
    robot.drive(350)
    robot.turn(-100)
    robot.drive(100)
    robot.fork_lift(160,2000)

    ## 28s 134pts

    # Angler Fish (4s 30pts)
    robot.curve(830, -20)
    robot.curve(700, 25)
    robot.drive(180)

    ## 32s 164pts

    # Remove krill and coral and drive off the mat (10s -5pts)
    robot.curve(400, -60)
    robot.curve(150, -20)
    robot.drive(200)
    robot.curve(450, 68)
    robot.raise_all()
    robot.stow_all()

    # 42s 159pts

def runA():
    robot.fork_lift_up()
    robot.plow_lift(100, 500)

def runA():

    # Flip up coral buds (s 20pts)
    robot.stow_all()
    robot.drive(350)
    robot.curve(150, 90)
    robot.drive(-75)

    ## s 179pts

    # Lift Scuba Dude (s 20pts)
    robot.plow_lift(23, 500)
    robot.plow_lift(-10, 500)

    ## s 199pts

    # Release the Shark (s 20pts)
    robot.drive(15)
    robot.curve(150, 45)
    robot.drive(-160)
    robot.fork_lift(340, 2000)
    robot.fork_lift_up()

    ## s 219pts

    # Drop off Scuba Dude (s 20 pts)
    robot.curve(190, 45)
    robot.drive(-100)
    robot.plow_lift(-18, 500)
    robot.drive(80)

    ## s 239pts

    # Raise the Mast (s 30pts)
    robot.turn(45)
    robot.fork_lift_lower()
    robot.curve(40, 45)
    robot.plow_up()
    robot.drive(-20)
    robot.fork_lift(-160, 2000)
    robot.fork_lift(160, 2000)

    ## s 269pts

    # Coral Reef (s 20pts)
    robot.turn(-40)
    robot.drive(-200)
    robot.turn(40)
    robot.drive(-200)
    robot.fork_lift_up()
    robot.turn(25)
    robot.drive(160)
    robot.plow_lower()
    robot.plow_up()
    robot.plow_stow()
    robot.fork_lift_stow()

    ## s 289pts

    # Send over the submersible (s 30pts)
    robot.drive(-160)
    robot.turn(-18)
    robot.drive(-190)
    robot.plow_lift(-8, 500)
    robot.turn(-95)

    ## s 319pts

    # Seabed Sample Collection (s 10pts)

    robot.turn(137)
    robot.fork_lift_up()
    robot.plow_lift(200, 500)
    robot.drive(100)
    robot.turn(-60)

    ## s 329pts

    # Drive off mat
    robot.drive(400)
    robot.turn(-40)
    robot.drive(740)
    robot.turn(48)
    robot.drive(100)
    robot.raise_all()
    robot.stow_all()

def runA():
    # Coral Reef Segments (s 15pts)
    robot.wait(500)
    robot.drive(-80, 50)

    ## s 344pts

    # Sample Dump (s 15pts)
    robot.fork_lift(70)
    robot.fork_lift(-70)

    ## s 359pts

    # Shark Dropoff (s 10pts)
    robot.drive(100)
    robot.turn(-26)
    robot.wait(750)
    robot.drive(-600)

    ## s 369pts

    # Drive to other starting area
    robot.turn(26)
    robot.drive(-1200)

def runA():  # 21s 40pts
    # Align with crab trap
    robot.raise_all()
    robot.stow_all()
    robot.drive(100)
    robot.turn(135)
    robot.curve(380, -45)
    robot.fork_lift(250, 2000)

    # Drive Up to the crab trap
    robot.drive(-350)

    # Bend the middle joint and fold trap in half
    robot.turn(25)
    robot.drive(-150)

    # Lower the fork lift and get into position for the first flip
    robot.fork_lift(-45, 2000)
    robot.curve(300, -25)
    robot.fork_lift(70, 2000)
    robot.drive(-100)

    # Flip up the traps
    robot.fork_lift(-200, 2000)

    # Push over the traps
    robot.fork_lift(150, 2000)
    robot.drive(-160)

    # Re-align on right side
    robot.fork_lift(-150, 2000)
    robot.curve(300, -35)
    robot.turn(35)
    robot.fork_lift_lower()
    robot.drive(-170)
    robot.fork_lift(-200, 2000)

    ## s 409pts

    # Creature Park (s 10pts)
    robot.drive(100)
    robot.turn(45)
    robot.drive(-300)
    robot.turn(45)
    robot.drive(-100)

    ## s 419pts
def runA():  # 21s 40pts
    robot.fork_lift(-270, 9000)

# !! DO NOT REMOVE THE FOLLOWING LINES !!
singlerun = False
if singlerun:
    run1()
    robot.run()
    run2()
    robot.run()
else:
    robot.menu(run1, run2, run3, run4, run5, run6)
