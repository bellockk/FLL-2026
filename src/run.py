from robot import Robot

robot = Robot()


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
# !! DO NOT REMOVE THE FOLLOWING LINE !!
robot.run()
