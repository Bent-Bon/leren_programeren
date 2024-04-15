# name of student: 
# number of student:
# purpose of program: 
# structure of program: 

coinValues = [50,20,10,5,2,1] #lijst met valeus die de munten moeten voostellen
euros = [5,2,1] #lijst et data om te checken later in de code of het een euro is
gegeven = [] #hier komt alles wat gegeven is in een string in te staan

toPay = int(float(input('Amount to pay: '))* 100) #input wat er betaald moet worden
paid = int(float(input('Paid amount: ')) * 100) #input met wat er betaald is
change = paid - toPay #het totale bedrag met wat er terug gegeven moet worden

while change > 0 and len(coinValues) > 0: #de loop blijft gaan zolang change meer dan 0 blijft en als er nog wat in de lijst coinvalues staat
  coinValue = coinValues.pop(0) #coinvalue is de value van wat er net gepopt is in coinvaleus en haalt de eerste waarde uit de lijst
  geld = coinValue #dit is om de orginele waarden te behouden voor later als hij bewerkt word
  if coinValue in euros: #hier checkt hij of het een euro is
    coinValue = coinValue * 100 #hier maakt er centen van
  nrCoins = change // coinValue #het berekend hoeveel munten er nodig zijn om het bedrag rond re maken

  if nrCoins > 0: #checkt of hij door alle munt sorten heen is gegaan
    if geld in euros: #checkt weer of het een euro is zodat het goed er in staat of het een euro is
      print('return maximal ', nrCoins, ' coins of ', geld, ' euros!' ) #print munt soort en hoeveel hij je er terug kan geven in die munt hoeveelheid
      nrCoinsReturned = int(input('How many coins of ' + str(geld) +  ' euros did you return? ')) #print hoeveel hij terug geeft
      gegeven.append([f"je kreeg {nrCoinsReturned}x {geld}euro"]) #hier append hij wat er net gebeurt is
    else:
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #print munt soort en hoeveel hij je er terug kan geven in die munt hoeveelheid
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #print hoeveel hij terug geeft
      gegeven.append([f"je kreeg {nrCoinsReturned}x {geld}cent"]) #hier append hij wat er net gebeurt is
    change -= nrCoinsReturned * coinValue #haalt de aangegeven hoeveelheid van totaal af

if change > 0: #checked of al het geld terug gegeven is
  print('Change not returned: ', str(change) + ' cents') #geeft aan hoeveel terug gegeven is

else:
  print('done')

print("dit zijn de munten die er terug geven waren:")
for x in gegeven: #een loop voor alles wat er net gebeurt is
  print(x)