# Array

#### 1. 1차원 배열 생성
arr1 = [1, 2, 3, 4, 5]  # 기본적인 1차원 배열
arr2 = list(range(1, 6))  # range를 사용하여 배열 생성
arr3 = [0] * 5  # 초기값이 0인 배열 생성

#### 2. 2차원 배열 생성
arr_2d_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr_2d_2 = [[0] * 3 for _ in range(3)]  # 리스트 컴프리헨션을 이용한 2차원 배열 생성
arr_2d_3 = [[0] * 3] * 3  # ❌ 잘못된 방식 (얕은 복사로 인해 문제가 발생)

#### 3. 배열 복사
# - 얕은 복사 (Shallow Copy)
arr_copy_1 = arr1
arr_copy_1[0] = 10

# - 깊은 복사 (Deep Copy)
import copy

arr_copy_2 = copy.deepcopy(arr1)
arr_copy_2[0] = 100

# - 슬라이싱을 통한 복사
arr_copy_3 = arr1[:]
arr_copy_3[0] = 1000

# - 리스트 컴프리헨션을 통한 복사
arr_copy_4 = [x for x in arr1]
arr_copy_4[0] = 10000

#### 4. 배열 정렬
# - 기본 정렬
arr_sorted = sorted(arr1)

# - 역순 정렬
arr_sorted_reverse = sorted(arr1, reverse=True)

# - 정렬 기준을 변경 (예: 길이 기준 정렬)
str_arr = ['apple', 'banana', 'cherry', 'date']
sorted_by_length = sorted(str_arr, key=len)

# - 람다 함수를 사용한 정렬 (마지막 문자열로 정렬)
sorted_by_last_char = sorted(str_arr, key=lambda x: x[-1])

#### 5. 배열의 주요 연산
# - 요소 추가 (append, extend)
arr1.append(6)
arr1.extend([7, 8, 9])

# - 요소 삭제 (remove, pop, del)
arr1.remove(9)  # 값으로 삭제
arr1.pop(0)  # 인덱스로 삭제
del arr1[1:3]  # 슬라이싱으로 범위 삭제

# - 요소 찾기 (index)
try:
    index = arr1.index(7)
except ValueError:
    index = -1  # 요소가 없을 경우 예외 처리

# - 길이 확인 (len)
arr_length = len(arr1)

#### 6. 슬라이싱 (Slicing)
# - 전체 배열 복사
arr_slice_1 = arr1[:]

# - 일부 요소만 슬라이싱
arr_slice_2 = arr1[1:3]

# - 스텝 사용
arr_slice_3 = arr1[::2]

#### 7. 배열의 반복문 사용
# - 인덱스 없이 요소만 순회
for elem in arr1:
    pass

# - 인덱스와 함께 요소 순회 (enumerate)
for index, elem in enumerate(arr1):
    pass

# - 이중 반복문을 이용한 2차원 배열 순회
for row in arr_2d_1:
    for elem in row:
        pass

# - 리스트 컴프리헨션을 이용한 2차원 배열 순회
flattened = [elem for row in arr_2d_1 for elem in row]

#### 8. 기타 유용한 배열 관련 함수
# - 최소값과 최대값 찾기
min_value = min(arr1)
max_value = max(arr1)

# - 모든 요소의 합
total = sum(arr1)

# - 모든 요소가 조건을 만족하는지 확인 (all)
all_positive = all(x > 0 for x in arr1)
# - 조건을 만족 요소가 존재하는지 확인 (all)
any_negative = any(x < 0 for x in arr1)

# - 리스트를 문자열로 변환 (join)
joined_str = ', '.join(map(str, arr1))

# - 문자열을 리스트로 변환 (split)
str_data = "1, 2, 3, 4, 5"
str_to_list = list(map(int, str_data.split(', ')))

# - 요소의 빈도수 세기 (Counter)
from collections import Counter

frequency = Counter(arr1)

