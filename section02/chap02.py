'''
Collection:
    list
    tuple
    set
    dictionary
'''

# ============================== list ==============================

# 빈 리스트 생성
empty_list = []

# 리스트 생성 및 초기화
t_list = [1,2,3,4,5]
print(t_list, type(t_list))

# 데이터 추가
t_list.append(6)
print(t_list)

# 데이터 삽입
t_list.insert(3, 34)
print(t_list)

# 데이터 삭제
t_list.pop()        # 마지막 인덱스 데이터 삭제
print(t_list)
t_list.remove(34)   # 특정 데이터 삭제
print(t_list)

print("------------------------------")
# ============================== tuple ==============================

# 빈 튜플 생성
empty_tuple = tuple()

# 리스트를 튜플로 보호
t_tuple = tuple(t_list)     # empty_tuple.anything() 추가, 수정, 삭제 불가
print(t_tuple, type(t_tuple))

print("------------------------------")
# ============================== set ==============================

# 세트 생성 및 초기화
t_set = {1,2,3,4,5,}            # empty_set[n] 인덱싱 없음
print(t_set, type(t_set))

print("------------------------------")
# ============================== dictionary ==============================

# 빈 딕셔너리 생성
empty_dict = dict()

# 딕셔너리 생성 및 초기화
# Key : Value의 쌍(Couple)으로 데이터 관리
t_dict = {
    "apple" : "사과",
    "watermelon" : "수박",
    "tomato" : "토마토"
}
print(t_dict, type(t_dict))

# 데이터 추가
t_dict["orange"] = "오렌지"
t_dict.setdefault("pineapple", "파인애플")
print(t_dict)

# 데이터 수정
t_dict["apple"] = "애플"
t_dict.update(watermelon = "워터멜론")
print(t_dict)

# Key 대입
print(t_dict["tomato"])

print("------------------------------")