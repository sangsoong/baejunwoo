'''
내장 함수 : 파이썬 기본 패키지에 이미 포함되어서 제공되는 유틸리티 함수


메소드: 객체가 제공하는 기능
ex) .append(), .add(), .remove()
함수:  파이썬이 제공하는 기능
ex) print(), input(), int(), float(), len()
'''

print(chr(97))      # 유니코드 -> 문자
print(ord('한'))    # 문자 -> 유니코드

val = eval('3*4')
print(val)

li = [10, 20, 30, 40, 50]
for tp in enumerate(li):
    print(tp)
    
li = [5, 4, 3, 2, 8, 1, 9]
print(sorted(li))
print(sorted(li, reverse=1))
print(li)

li1 = ['현대', '기아', '싸용']
li2 = [1, 2, 3]
for comp in zip(li1, li2):
    print(comp)