time = int(input('변환할 초를 입력하세요 >>> '))
hour = time//3600
min = (time%3600)//60
sec = (time%3600)%60

print(f'변환결과는 {hour}시간 {min}분 {sec}초 입니다.')