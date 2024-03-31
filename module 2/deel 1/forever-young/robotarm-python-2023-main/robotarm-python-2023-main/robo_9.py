# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(4):
#     robotArm.moveLeft()

# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(5):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(4):
#     robotArm.moveLeft()

# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(5):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(5):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(4):
#     robotArm.moveLeft()

# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(5):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(5):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(5):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(4):
#     robotArm.moveLeft()


fr = 1
mc = 4
fr_config = [1, 3, 6, 10]
while fr < 11:
    robotArm.grab()
    for x in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(mc):
        robotArm.moveLeft()
    mc = 5
    fr += 1
    if fr in fr_config:
        mc = 4

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()