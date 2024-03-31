# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
move = 1
color = "blank"
robotArm.grab()
while color != "":
    for x in range(move):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(move):
        robotArm.moveLeft()
    move += 1
    robotArm.grab()
    color = robotArm.scan()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()