from robot import Robot

robot = Robot()

def run1():
    robot.raise_all()
    robot.stow_all()

def run2():

    # Drive to Sea Creature and Catch the creature
    robot.drive(140)
    robot.turn(-50)
    robot.drive(350)
    robot.drive(-440)

    #  Krill and Coral
    robot.drive(200)
    robot.turn(50)

    ## Un-Stow and lower plow
    robot.raise_all()
    robot.lower_plow_stow_fork_lift()

    ## Push Krill and coral
    robot.drive(400)
    robot.drive(-300)

    # Yellow Boat
    robot.turn(-137)
    robot.drive(110)
    robot.fork_lift(340, 2000)
    robot.drive(-60)
    robot.fork_lift(-110)
    robot.turn(40)
    robot.fork_lift(-90, 2000)
    robot.turn(115)
    robot.drive(350)
    robot.turn(-100)
    robot.drive(100)

    # Sea Weed Sample
    robot.fork_lift(160,2000)

    # Angler Fish
    robot.curve(800, -19)
    robot.curve(700, 25)
    robot.drive(160)

    # Remove krill and coral and drive off the mat
    robot.curve(400, -60)
    robot.curve(150, -20)
    robot.curve(600, 80)
    robot.plow_up()
    robot.plow_stow()
    robot.curve(500, 20)
    robot.fork_lift_up()
    robot.fork_lift_stow()

def run3():
    robot.drive(200)
    robot.curve(700, -15)
    robot.curve(700, 20)
    #robot.curve(600, 15)



def run4():
    robot.drive(100)
    robot.turn(135)
    robot.curve(380, -45)
    robot.fork_lift(250, 2000)
    robot.drive(-350)
    robot.turn(25)
    robot.drive(-150)
    robot.fork_lift(-45, 2000)
    robot.curve(300, -25)
    robot.fork_lift(70, 2000)
    robot.drive(-100)
    robot.fork_lift(-200, 2000)


# robot.raise_all()
# robot.lower_all()
# robot.wait(5000)
# robot.fork_lift_up()
# robot.plow_up()
# robot.fork_lift_lower()
# robot.plow_lower()
# robot.raise_all()
# robot.plow_lower()
# robot.fork_lift_lower()
# robot.stow_all()

'''
# Drive to Sea Creature and Catch the creature
robot.drive(140)
robot.turn(-50)
robot.drive(350)
robot.drive(-440)
#robot.wait(500)


#  Krill and Coral
robot.drive(200)
robot.turn(50)
robot.fork_lift(120, 2000)
robot.plow_lift(340, 2000)
robot.fork_lift(-120, 2000)
robot.drive(400)
robot.drive(-300)

# Yellow Boat
robot.turn(-137)
robot.drive(120)
robot.fork_lift(340, 2000)
robot.drive(-60)
robot.fork_lift(-110)
robot.turn(40)
robot.fork_lift(-90, 2000)
robot.turn(115)
robot.drive(350)
robot.turn(-100)
robot.drive(100)
robot.fork_lift(160,2000)
robot.turn(-10)
robot.drive(200)
robot.drive(320)
robot.turn(25)
robot.drive(270)
robot.turn(-25)


'''

#Grab krill and do drop the shark (Only tested on jaws)
'''
robot.drive(200)
robot.turn(147)
robot.drive(-185)
robot.fork_lift(350,2000)
robot.drive(520)
robot.fork_lift(-350,2000)
robot.turn(-30)
robot.drive(-500)
robot.turn(-30)
robot.drive(-200)
robot.turn(-40)
robot.fork_lift(350, 500)
'''
# !! DO NOT REMOVE THE FOLLOWING LINES !!
robot.menu(run1, run2, run3, run4)
