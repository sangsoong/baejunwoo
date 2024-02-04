for dan in range(2,10):
    for gop in range(1, dan+1):
        if dan%2 == 0:
            continue
        print(f'{dan} x {gop} = {dan*gop}', end='\t')
    print()
    