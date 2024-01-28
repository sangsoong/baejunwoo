dan = 2
gop = 1
while dan <= 9:
    gop = 1
    while gop <= 9:
        print(f'{dan} * {gop} = {dan*gop}', end='\t')
        gop += 1
    dan += 1
    print()

print()    

dan = 2
gop = 1
while gop <= 9:
    dan = 2
    while dan <= 9:
        print(f'{dan} * {gop} = {dan*gop}', end='\t')
        dan += 1
    gop += 1
    print()