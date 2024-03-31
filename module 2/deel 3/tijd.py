# teller = 0
# tijd_teller = 0
# tijd = "AM ✞"

# while True:
#     teller += 1
#     if teller == 12:
#         tijd = "PM ♨"
#         if tijd == "PM ♨" and tijd_teller == 1:
#             tijd = "AM ✞"
#     elif teller == 13:
#         teller = 0
#         tijd_teller += 1
#     if tijd_teller == 2:
#         break
#     print(teller, tijd)

# tijd_AM = 1
# tijd_PM = 1

# while tijd_AM < 25:
#     if tijd_AM <= 12:
#         if tijd_AM < 12:
#             print(f"{tijd_AM} AM")
#         else: 
#             print("12 PM")
#     else:
#         if tijd_PM <= 11:
#             print(f"{tijd_PM} PM")
#         else:
#             print("12 AM")
#         tijd_PM += 1
#     tijd_AM += 1



########################################################
# tijd = 1
# teller = 0
# am_pm = "AM ✞"

# while teller < 25:

#     if tijd <= 12:
#         print(tijd, am_pm)
#     elif teller == 13:
#     else:
#         tijd = 0
#         if  am_pm == "AM ✞":
#             am_pm = "PM ♨"
#         else:
#             am_pm = "AM ✞"

#     tijd += 1
#     teller += 1
######################################################################################

switch = 0
am_pm = "AM ✞"
teller = 1

for x in range(24):
    print(teller, am_pm)
    if switch == 10:
        if  am_pm == "AM ✞":
            am_pm = "PM ♨"
        else:
            am_pm = "AM ✞"

    elif switch == 11:
        switch = -1
        teller = 0
    switch += 1
    teller += 1
