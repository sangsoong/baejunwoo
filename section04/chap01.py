'''
연산자와 우선순위
'''

# 산술연산자 : +, -, *, /, //, %, **
# 대입연산자 : +=, -=, *=, /=, //=, %=, **=

# 비교연산자 : <, >, <=, >=, ==, !=, and, or
print(5>10)
print(5<10)

res1 = 5 == 10
res2 = 5 <= 10
print(res1, res2)

result1 = res1 and res2
result2 = res1 or res2
print(result1, result2)

age = int(input('나이를 입력하세요 >>> '))
print('청소년인가? :', ((10 < age) and (age < 18)))

# 비트연산자 : &, |, ^, ~, <<, >>, >>>
'''
and연산
  0011
& 0101
______
  0001
  
or연산
  0011
| 0101
______
  0111
  
eor(exclusive or)연산
  0011
^ 0101
______
  0110
  
not연산
~ 0101
______
  1010
  
shift연산
1. <<
result = 19 << 2
0001 0011 -> 0100 1100
print(result) -> 

2. >>
result = -104 >> 1
1001 1000 -> 1100 1100 : 부호 보존
print(result) ->

3. >>>
result = -104 >>> 1
1001 1000 -> 0100 1100 : 부호 무시
print(result) ->
'''

result = -104 >> 1
print(result)