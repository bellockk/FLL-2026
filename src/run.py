from robot import Robot

robot = Robot()

def run1():
    # Pre-Run Initialization (Get Motor Endpoints for up and down)
    robot.initialize()

    ## 0s 89pts  0deg is West

def run2():
    # Drive Up to the Artificial Habitat
    robot.lower_fork_lift_stow_plow()
    robot.fork_lift(15)
    robot.drive(-100)
    robot.curve(-450, 25)

    # Fold Artificial Habitat
    robot.turn(35)
    robot.drive(-100)
    robot.drive(80)
    robot.turn(-10)

    # Flip Artificial Habitat (40pts)
    robot.fork_lift(0)
    robot.drive(-150)
    robot.drive(20)
    robot.fork_lift_stow(2000)

    ## 129pts

    # Release the Unknown Creature (20pts)
    robot.turn(72)
    robot.drive(-180)

    ## 149pts

    # Collect Krill and Coral Segment (-5pts)
    robot.drive(30)
    robot.turn(-132)
    robot.lower_plow_stow_fork_lift()
    robot.drive(480)
    robot.turn(-33)
    robot.drive(70)
    robot.turn(-117)
    robot.drive(100)
    robot.turn(30)
    robot.drive(200)

    ## 144pts

    # Reveal East Whale (20pts)
    robot.plow_up()
    robot.drive(-215)
    robot.turn(90)
    robot.drive(155)
    robot.plow(19, 500)
    robot.drive(-125)
    robot.plow_up()

    ## 164pts

    # Change Shipping Lanes (20pts)
    robot.turn(45)
    robot.drive(60)
    robot.turn(-92)
    robot.drive(80)
    robot.fork_lift_lower()
    robot.drive(-70)
    robot.fork_lift_stow()

    ## 184pts

    # Collect Plankton Sample (10pts)
    robot.turn(-47)
    robot.drive(-70)
    robot.drive(30)
    robot.fork_lift_lower()

    ## 194pts

    #  Angler Fish (s 30pts)
    robot.turn(-6)
    robot.drive(200)
    robot.plow_lower()
    robot.drive(420)
    robot.turn(10)
    robot.drive(80)
    robot.drive(-20)
    robot.turn(15)
    robot.drive(150)
    robot.turn(-15)

    ## 224pts

    # Drive off board and collect krill and coral (-5 pts)
    robot.drive(110)
    robot.curve(350, -90)
    robot.curve(300, 90)
    robot.raise_all()

    ## 62s 219pts

def run3():

    # Get Reef
    robot.turn(95)
    robot.drive(290)
    robot.turn(-5)
    robot.plow(15)
    robot.drive(-290)

    # Release Shark (20pts)
    robot.turn(-161)
    robot.plow_up()
    robot.drive(-550)
    robot.turn(-65)
    robot.fork_lift_lower()
    robot.fork_lift_up()
    robot.turn(65)
    robot.drive(600)
    robot.turn(75)

    ## 72s 239pts

def run4():
    # Hang Coral Tree (20pts)
    robot.fork_lift(60)
    robot.turn(-97)
    robot.drive(-250)
    robot.fork_lift(50)

    # 259pts

    # Raise the Mast (30pts)
    robot.drive(150)
    robot.turn(50)
    robot.drive(-420)
    robot.turn(227)
    robot.plow_lower()
    robot.drive(260)

    # 289pts

    # Kraken's Treasure (20pts)
    robot.drive(-200)

    # 309pts

    # Flip Coral Buds up (20pts)
    robot.plow(50)
    robot.turn(-45)
    robot.drive(140)
    robot.turn(45)
    robot.drive(-120)

    # s 329pts

    # Grab Scuba Dude (20pts)
    robot.fork_lift(55)

    # s 249pts

    # Drop Off Scuba Dude (20 pts)
    robot.curve(100, 88)
    robot.fork_lift(53)
    robot.drive(-100)
    robot.fork_lift(48)
    robot.drive(100)

    # s 269pts

    # Flip Coral Reef (20 pts)
    robot.fork_lift(38)
    robot.drive(-100)
    robot.fork_lift(15)
    robot.fork_lift(38)
    robot.drive(100)

    # s 289pts

    # Collect Seabed Sample (10 pts)
    robot.turn(40)
    robot.fork_lift(40)
    robot.drive(-300)
    robot.fork_lift(90)
    robot.fork_lift(48)

    # s 299pts

    # Send the Submersible (30 pts)
    robot.turn(62)
    robot.drive(-450)
    robot.turn(-130)
    robot.turn(120)

    # s 329pts

    # Drive off the mat
    robot.drive(500)
    robot.curve(350, -90)
    robot.curve(300, 90)

    # s 334pts

def run5():
    robot.stow_all()

def run6():
    # Coral Reef Segments (s 15pts)
    robot.drive(-100, 100)

    # 349pts

    # Sample Dump (s 15pts)
    robot.fork_lift(60)
    robot.fork_lift_stow()
    robot.drive(150, 100)
    robot.turn(-30)

    # 364pts

def run7():

    # Drive Off Matt
    robot.drive(-200, 100)


def run8():

    # Dump Krill (40pts)
    robot.turn(80)
    robot.drive(-635)
    robot.turn(-125)
    robot.drive(100)
    robot.drive(60, 100)

    # 404 pts

    # Reveal West Whale (s 10pts)
    robot.curve(-340, -100)
    robot.turn(-124)

    # 414pts

    # Park on Unknown Creature in cold seep (10pts)
    robot.turn(18)
    robot.fork_lift(15)
    robot.drive(-220)

    # 424s


# !! DO NOT REMOVE THE FOLLOWING LINES !!
robot.menu(run1, run2, run3, run4, run5, run6, run7, run8)
