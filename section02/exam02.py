# 입력받기
name = input('이름을 입력하세요 >>> ')
age = input('나이를 입력하세요 >>> ')
role = input('역할을 입력하세요 >>> ')

# 딕셔너리 생성
entity1 = dict()
entity1['name'] = name
entity1['age'] = int(age)
entity1['role'] = role

name = input('이름을 입력하세요 >>> ')
age = input('나이를 입력하세요 >>> ')
role = input('역할을 입력하세요 >>> ')

entity2 = dict()
entity2['name'] = name
entity2['age'] = int(age)
entity2['role'] = role

name = input('이름을 입력하세요 >>> ')
age = input('나이를 입력하세요 >>> ')
role = input('역할을 입력하세요 >>> ')

entity3 = dict()
entity3['name'] = name
entity3['age'] = int(age)
entity3['role'] = role

entities = []
entities.append(entity1)
entities.append(entity2)
entities.append(entity3)

name = input('마을 이름을 입력하세요 >>> ')

neighbor = {}
neighbor['name'] = name
neighbor['family'] = entities

#출력
print(neighbor)