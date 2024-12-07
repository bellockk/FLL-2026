from robot import Robot

robot = Robot()

#collection 1
robot.drive(-240)
robot.turn(-50)
robot.drive(-250)
robot.drive(380)

#realignment 1
robot.turn(-54)
robot.drive(-170)
robot.turn(287)

#collection 2
robot.back_lift(120,2000)
robot.front_lift(350,2000)
robot.back_lift(-150,2000)
robot.drive(570)
robot.turn(60)
robot.drive(60)
robot.turn(-60)
robot.drive(50)
robot.drive(-250)


#realignment 2
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




# !! DO NOT REMOVE THE FOLLOWING LINE !!
robot.run()
