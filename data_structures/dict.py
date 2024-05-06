# 해시테이블 (Dictionary)

# dict 생성
my_dict = {"apple": 10, "banana": 20, "orange": 30}

# 키 리스트 가져오기
key_list = list(my_dict.keys())
print("Key List:", key_list)  # 출력: ['apple', 'banana', 'orange']

# 값 리스트 가져오기
value_list = list(my_dict.values())
print("Value List:", value_list)  # 출력: [10, 20, 30]

# 키로 값 가져오기
my_dict.get('apple')

# 키로 값 삭제하기
del my_dict['apple']
    
# defaultdict
# 기존 dict은 없는 KeyError 에러 발생
# defaultdict은 없는 키 접근 시 default 값이 반환/사용
from collections import defaultdict

graph = defaultdict(list) 
