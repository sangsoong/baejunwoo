input = int(input('자판기에 넣을 금액을 입력하세요 >>> '))

def vending_machine(money:int):
    count = money//700
    for i in range(count + 1):
        rest = money - (700 * i)
        print(f'음료수 = {i}개, 잔돈 = {rest}원')
    
vending_machine(input)