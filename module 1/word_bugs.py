a = input(str('voer iets in: '))
b = input(str('voer nog iets in: '))

tel_a = len(a)
tel_b = len(b)

if tel_a > tel_b:     
    print('input 1 heeft meer characters dan input 2')
elif tel_a < tel_b:   
    print('input 1 heeft minder characters dan input 2')
else:                   
    print('input 1 en input 2 hebben evenveel characters')