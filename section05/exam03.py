num1= int(input('첫번째 정수를 입력하세요 >>> '))
num2 = int(input('두번째 정수를 입력하세요 >>> '))
num3 = int(input('세번째 정수를 입력하세요 >>> '))

largest = num1
if largest < num2:
    largest = num2
if largest < num3:
    largest = num3

print(f'가장 큰 수는 {largest}')