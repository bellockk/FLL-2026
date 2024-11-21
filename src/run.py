from robot import Robot

robot = Robot()

robot.drive(-240)
robot.turn(-50)
robot.drive(-250)
robot.drive(380)
robot.turn(-54)
robot.drive(-170)
robot.turn(290)

robot.back_lift(120,2000)
robot.front_lift(350,2000)
robot.back_lift(-150,2000)
robot.drive(570)
robot.turn(50)
robot.drive(60)
robot.turn(-50)
robot.drive(50)
robot.drive(-250)

robot.front_lift(-175,2000)
robot.turn(50)

robot.drive(-200)
robot.turn(-90)

robot.back_lift(350,2000)
robot.front_lift(-175,2000)

robot.turn(-105)
robot.drive(-55)
robot.back_lift(-80)
robot.turn(80)

'''
robot.drive(-95)
robot.back_lift(-80)
robot.turn(80)
robot.drive(50)
robot.turn(125)
robot.front_lift(350,2000)
robot.drive(370)
robot.turn(-100)
'''


# !! DO NOT REMOVE THE FOLLOWING LINE !!
robot.run()
