from robot import Robot

robot = Robot()


# Drive to Sea Creature and Catch the creature
robot.drive(140)
robot.turn(-50)
robot.drive(350)
robot.drive(-440)

#  Krill and Coral
robot.drive(200)
robot.turn(50)
robot.fork_lift(120, 2000)
robot.plow_lift(350, 2000)
robot.fork_lift(-120, 2000)
robot.drive(400)
robot.drive(-300)

# Yellow Boat
robot.turn(-137)
robot.drive(120)
robot.fork_lift(350, 2000)
robot.drive(-80)
robot.fork_lift(-100)
robot.turn(40)
robot.fork_lift(-90, 2000)
robot.turn(115)
robot.drive(315)
robot.turn(-100)
robot.drive(90)
robot.fork_lift(150,2000)
#robot.turn(-10)
#robot.drive(550)
#robot.turn(20)
#robot.drive(200)


#robot.turn(-15)
#robot.drive(100)
#robot.turn(10)
#robot.drive(500)
#robot.turn(15)
#robot.drive(50)
#robot.turn(-15)
#robot.drive(200)

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
