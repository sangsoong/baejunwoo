str = input('이름과 점수를 쉼표로 구분하여 입력하세요 >>> ')
li = str.split(',')
li[0] = li[0].strip()
li[1] = li[1].strip()
print(f'이름은 {li[0]}이고, 점수는 {li[1]}점입니다.')