import heapq

#### 1. 최소 힙 (Min-Heap)
min_heap = [3, 1, 4, 1, 5, 9]
heapq.heapify(min_heap)  # 리스트를 최소 힙으로 변환
heapq.heappush(min_heap, 2)  # 요소 추가
smallest = heapq.heappop(min_heap)  # 최솟값 제거 및 반환

#### 2. 최대 힙 (Max-Heap)
# - 음수 부호를 사용하여 최대 힙을 구현
max_heap = [-x for x in [3, 1, 4, 1, 5, 9]]
heapq.heapify(max_heap)  # 리스트를 최대 힙으로 변환
heapq.heappush(max_heap, -2)  # 요소 추가
largest = -heapq.heappop(max_heap)  # 최댓값 제거 및 반환

#### 3. `nlargest`와 `nsmallest` 메서드
# - n개의 가장 큰/작은 요소를 찾아 반환
three_largest = heapq.nlargest(3, min_heap)  # [10, 9, 5]
three_smallest = heapq.nsmallest(3, min_heap)  # [1, 2, 3]

#### 4. 커스텀 객체를 이용한 힙
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age  # 나이 기준 오름차순

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
heapq.heapify(people)
heapq.heappush(people, Person("Diana", 28))
youngest = heapq.heappop(people)

#### 5. 람다를 이용한 힙
data = [
    ('apple', 3),
    ('banana', 2),
    ('cherry', 1),
    ('orange', 4),
]

heapq.heapify(data, key=lambda x: x[1]) # 두 번째 요소를 기준으로 정렬하는 최소 힙 생성
heapq.heappush(data, ('fig', 5)) # 힙에 새로운 요소 추가
smallest = heapq.heappop(data) # 힙에서 최소 요소 제거 및 반환