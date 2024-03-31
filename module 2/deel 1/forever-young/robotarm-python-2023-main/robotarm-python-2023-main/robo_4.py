# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for x in range(5):
    robotArm.grab()
    for x in range(2):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(2):
        robotArm.moveLeft()
for x in range(2):
    robotArm.moveRight()
for x in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()