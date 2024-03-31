# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for y in range(7):
    robotArm.grab()
    for x in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(8):
        if y == 6:
            break
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()