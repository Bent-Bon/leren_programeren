start = str(input("is de kaas geel?: ")).lower()
if start == "ja":
    gaten = str(input("zitten er gaten in?: ")).lower()
    if gaten == "ja":
        duur = str(input("is de kaas belachelijk duur?: ")).lower()
        if duur == "yes":
            print("emmenthaler")
        else:
            print("leerdammer")
    else:
        hard = str(input("is de kaas steenhard?: ")).lower()
        if hard == "yes":
            print("parmigiano reggiano")
        else:
            print("goudse kaas")
else:
    schimmel = str(input("heeft de kaas blauwe schimmel?: ")).lower()
    if schimmel == "yes":
        korst = str(input("heeft de kaas een korst?: ")).lower()
        if korst == "yes":
            print("blue de rochbaron")
        else:
            print("foume camben")
    else:
        korst_nee = str(input("heeft de kaas een korst?: ")).lower()
        if korst_nee == "yes":
            print("camembert")
        else:
            print("mozarella")