# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for zin in range(5):
    zin += 1
    for xin in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for yin in range(2):
        if zin == 5:
            break
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()