from robot import Robot
robot = Robot()

def run1():
    # Pre-Run Initialization (Get Motor Endpoints for up and down)
    robot.initialize()

    ## Precision Tokens 50pts

    ## Equipment Inspection 20pts

    ## 0s 70pts  0deg is West

def run2():

    # Drive from Left Home to Surface Brushing
    robot.drive(400)
    robot.drive(200)

    # Surface Brushing (30pts)

    # Drive from Surface Brushing to Map Reveal

    # Map Reveal (30pts)

    # Drive from Map Reveal to Mineshaft Explorer

    # Mineshaft Explorer (40pts)

    # Careful Recovery (40pts)

    # Site Marking (10pts)

    # Drive to Left Home
    # Remove and store Brush, Minecart, Topsoil and Precious Artifact
    # Load Site Marker

    # XXXs 150pts (220pts Total)

def run3():
    # Drive from Left Home to Salvage Operation
    robot.fork_lift(0)
    robot.plow(0)

    # Salvage Operation (30pts)

    # Site Marking (10pts)

    # Drive from Salvage Operation to Angler Artifacts

    # Angler Artifacts (30pts)

    # Drive from Angler Artifacts to Tip the Scales

    # Tip the Scales (30pts)

    # Drive from Tip the Scales to What's on Sale

    # What's on Sale (30pts)

    # Drive from What's on Sale to Right Home
    # Remove Scale Pan

    # XXXs 130pts (350pts Total)

def run4():
    # Drive from Right Home to Silo
    robot.fork_lift(100)
    robot.plow(100)

    # Silo (30pts)

    # Drive from Silo to Forge

    # Forge (30pts)

    # Heavy Lifting (30pts)

    # Push Boulders off table

    # Drive from Boulder Push to Who Lived Here

    # Who Lived Here (30pts)

    # Drive from Who Lived Here to Right Home
    # Load all Forum Artifacts collected so far
    # Load Site Marker

    # XXXs 120pts (470pts Total)

def run5():
    # Drive from Right Home to Site Marking
    robot.fork_lift(-200)
    robot.plow(-200)

    # Site Marking (10pts)

    # Drive from Site Marking Opposing Team's Minecart

    # Obtain Opposing Team's Minecart

    # Drive from Opposing Team's Minecart to Statue Rebuild

    # Statue Rebuild (30pts)

    # Drive from Statue to Forum

    # Forum (35pts)

    # Move away from Forum so no pieces are touching robot

    # XXXs 75pts (545pts Total)

def run6():
    robot.fork_lift(200)
    robot.plow(200)


# !! DO NOT REMOVE THE FOLLOWING LINES !!
robot.menu(run1, run2, run3, run4, run5, run6)
