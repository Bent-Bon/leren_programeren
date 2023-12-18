artist_list = []
for x in range(2):
    artist = {}
    artist["artist name"] = input("what is the artists name?: ")
    artist["artist toptrack"] = input("what is the artists toptrack?: ")
    #artist["artist date"] = int(input("when did the artist start?: "))
    #artist["artist album count"] = int(input("how many albums did this artist release?: "))
    #artist["artist genre"] = input("what genre music does this artist make?: ")
    artist_list.append(artist)

print (artist_list)
print(artist_list[0:]["artist name"])