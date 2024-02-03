'''
비시퀀스와 for 반복문
'''

comp = {'현대', '기아', '쌍용', '벤츠'}
for s in comp:
    print(s)
    
di = {'flower':'꽃',
      'car':'차',
      'cup':'컵',
      'object':'객체'}
for s in di:    # key값을 반환한다
    print(f'{s}:{di[s]}', end='\t')    # key를 넣어 value값을 반환한다