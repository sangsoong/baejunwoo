def gift(wedding:dict, who:str, money:int):
    wedding[who] = money
    global total
    total += money

wedding = {}
total = 0

gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)

print(f'축의금 명단: {wedding}')
print(f'전체 축의금: {total}')