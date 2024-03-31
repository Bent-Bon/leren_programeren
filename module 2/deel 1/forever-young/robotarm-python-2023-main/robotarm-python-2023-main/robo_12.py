# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
mr = 1
count = 1
for x in range(8):
    robotArm.moveRight()
for x in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for x in range(mr):
            robotArm.moveRight()
        robotArm.drop()
        if count != 9:
            for x in range(mr + 1):
                robotArm.moveLeft()
        mr += 1
        count += 1
    else:
        robotArm.drop()
        if count != 9:
            robotArm.moveLeft()
        mr += 1
        count += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()