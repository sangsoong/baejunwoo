score = 0

while True:
    print('==============================')
    score = int(input('영화의 평점을 입력해주세요(1~5) >>> '))

    if score > 5 or score < 1:
        print('평가는 1~5사이의 값만 가능합니다.')
    elif score >= 1 and score <= 5:
        print('고객님의 평점 : ', end='')
        for i in range(0,score):
            print('★', end='')
        break