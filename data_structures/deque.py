from collections import deque

#### 1. 스택 (Stack) - LIFO (Last In, First Out)
# - 요소 추가: append
# - 요소 제거: pop
stack = deque()
stack.append(1)  # push
stack.append(2)
stack.append(3)
stack.pop()  # pop, 3
# deque([1, 2])

#### 2. 큐 (Queue) - FIFO (First In, First Out)
# - 요소 추가: append
# - 요소 제거: popleft
queue = deque()
queue.append(1)  # enqueue
queue.append(2)
queue.append(3)
queue.popleft()  # dequeue, 1
#  deque([2, 3])

#### 3. 양방향 큐 (Deque) - Double-ended queue
# - 요소 추가: append, appendleft
# - 요소 제거: pop, popleft
deque_example = deque([1, 2, 3])
deque_example.append(4)  # 오른쪽에 추가
deque_example.appendleft(0)  # 왼쪽에 추가
deque_example.pop()  # 오른쪽에서 제거
deque_example.popleft()  # 왼쪽에서 제거
# deque([1, 2, 3])

#### 4. 기타 `collections.deque` 주요 메서드
# - clear(): 모든 요소 제거
deque_example.clear()

# - count(x): x의 등장 횟수 반환
deque_example.extend([1, 2, 2, 3, 3, 3])
count_2 = deque_example.count(2)  # 2의 등장 횟수는 2

# - extend(iterable): iterable의 모든 요소를 오른쪽에 추가
deque_example.extend([4, 5, 6])

# - extendleft(iterable): iterable의 모든 요소를 왼쪽에 추가
#   (주의: 순서가 뒤집혀 추가됨)
deque_example.extendleft([-1, -2, -3])

# - index(x[, start[, stop]]): x의 인덱스 반환
index_3 = deque_example.index(3)

# - insert(i, x): 인덱스 i에 x 삽입
deque_example.insert(2, 100)

# - reverse(): deque를 역순으로 변경
deque_example.reverse()

# - rotate(n): n만큼 회전 (양수: 오른쪽, 음수: 왼쪽)
deque_example.rotate(1)
deque_example.rotate(-2)