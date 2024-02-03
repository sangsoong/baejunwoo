num = int(input('보관할 과일 개수를 입력하세요 >>> '))
basket = []
for i in range(num):
    fr = input(f'{i+1}번째 과일을 입력하세요 >>> ')
    basket.append(fr)
print(basket)