for num in range(1, 1001):
    output = ''
    units = num%10
    tens = num//10
    hundreds = num//100
    
    if units!=0 and units%3==0: # 일의자리 0아니고 3의배수
        output = '짝'
    if tens!=0 and tens%3==0: # 십의자리 0아니고 3의배수
        output += '짝'
    if hundreds!=0 and hundreds%3==0: # 십의자리 0아니고 3의배수
        output += '짝'
    
    print(output if output else num, end='\t')
    
    if num%10 == 0:
        print()