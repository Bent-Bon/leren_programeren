# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
move = 9
for x in range(5):
    robotArm.grab()
    for x in range(move):
        robotArm.moveRight()
    move -= 1
    robotArm.drop()
    for x in range(move):
        robotArm.moveLeft()
    move -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()