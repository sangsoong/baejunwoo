'''
반복문에서 break문과 continue문
break: 반복문을 즉시 탍출한다
continue: 반복문의 Head부분으로 처리를 이동시킨다
'''

# break: 현재 있는 while문을 탈출
i = 0
while True:
    print(i)
    if i >= 9: break
    i += 1
    
print()

# 특정 조건이 되었을때 현재 있는 반복문을 탈출
for i in range(500):
    if i >= 50: break
    print(i)

print()

# 특정 조건이 되었을 때 상층부로 이동
for n in range(100):
    if n%2 == 1: continue
    print(n)

print()

n = 0
while n < 10:
    n += 1
    if n%2 == 1: continue
    print(n)