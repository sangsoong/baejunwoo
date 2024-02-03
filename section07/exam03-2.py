num = int(input('보관할 과일 개수를 입력하세요 >>> '))
basket = set()
while num:
    fr = input(f'{len(basket)+1}번째 과일을 입력하세요 >>> ')
    basket.add(fr)
    num -= 1
print(basket)