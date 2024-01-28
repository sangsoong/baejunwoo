korean = int(input('국어 점수를 입력하세요 >>> '))
english = int(input('영어 점수를 입력하세요 >>> '))
math = int(input('수학 점수를 입력하세요 >>> '))

avg = (korean + english + math)/3

print('평균은 %.1f점이고, 결과는 '%avg, '합격입니다.' if avg >= 80 else '불합격입니다.')