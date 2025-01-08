from robot import Robot

robot = Robot()

# Drive to Sea Creature and Catch the creature
robot.drive(140)
robot.turn(-50)
robot.drive(350)
robot.drive(-440)

# Remove the sea creature while the robot is back in the start area
robot.drive(200)
robot.turn(50)
robot.fork_lift(120, 2000)
robot.plow_lift(350, 2000)
robot.fork_lift(-120, 2000)
robot.drive(400)
robot.drive(-300)
robot.turn(-135)
robot.drive(120)
robot.fork_lift(350, 2000)
robot.drive(-80)
robot.fork_lift(-100)
robot.turn(40)
robot.fork_lift(-90, 2000)
robot.turn(35)
robot.drive(350)

#robot.turn(60)
#robot.drive(400)
#robot.drive(-200)
#robot.turn(55)
#robot.drive(360)

# WHO TOOK THE COOKIE FROM THE COOKIE JAR? CONNOR TOOK THE COOKIE FROM THE
# COOKIE JAR!

"""
robot.fork_lift(350, 2000)
robot.drive(-180)
robot.fork_lift(-80)
robot.turn(90)

#collection 2
robot.back_lift(120,2000)
robot.front_lift(350,2000)
robot.back_lift(-150,2000)
robot.drive(570)
robot.turn(60)
robot.drive(60)




#robot.drive(-500)


#realignment 2
robot.turn(-60)
robot.drive(50)
robot.drive(-250)
robot.front_lift(-175,2000)
robot.turn(50)
robot.drive(-220)
robot.turn(-90)
robot.back_lift(350,2000)
robot.front_lift(-175,2000)


#yellow boat
robot.turn(-110)
robot.drive(-80)
robot.back_lift(-80)
robot.turn(90)


#Realigmment 3 """


# !! DO NOT REMOVE THE FOLLOWING LINE !!
robot.run()
