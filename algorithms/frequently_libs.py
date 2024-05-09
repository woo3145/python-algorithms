
# 순열 & 조합

from itertools import permutations, combinations, product, combinations_with_replacement

# (순열) permutation
# n개의 데이터를 뽑아 만들 수 있는 모든 경우(순열)를 반환
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
data = ['A', 'B', 'C']
print(list(permutations(data, 3)))

# (조합) combinations
# n개의 데이터를 뽑아 순서를 고려하지 않고 나오는 모든 경우(조합)를 반환
# [('A', 'B', 'C')]
print(list(combinations(data, 3)))

# (중복 순열) product
# n개의 데이터를 뽑아 만들 수 있는 모든 경우를 반환(중복 허용)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
print(list(product(data, repeat=2)))

# (중복 조합) combinations_with_replacement
# n개의 데이터를 뽑아 순서를 고려하지 않고 나오는 모든 경우(조합)을 반환(중복허용)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(list(combinations_with_replacement(data, 2)))


#### 이진 탐색

from bisect import bisect_left, bisect_right

# *정렬된 데이터* 내에서 이진탐색 수행
arr = [1, 2, 2, 3, 3, 3, 4, 6, 6, 6]
# bisect_left: x가 들어갈 가장 왼쪽 인덱스 반환 (찾으면 젤 왼쪽 인덱스 / 없으면 이전 값의 다음 인덱스)
print(bisect_left(arr, 3)) # 3
print(bisect_left(arr, 5)) # 7
# bisect_right: x가 들어갈 가장 오른쪽 인덱스 반환 (찾으면 해당 값의 바로 오른쪽 인덱스 + 범위를 넘어갈 수 있음 )
print(bisect_right(arr, 3)) # 6
print(bisect_right(arr, 6)) # 10

#### 수학

from math import factorial, sqrt, gcd, pi, e

# factorial - x!반환
print('3! =', factorial(3)) # 1 x 2 x 3

# sqrt - 제곱근 반환
print('root 4 =', sqrt(4)) # 2

# gcd - 최대공약수 반환
print('gcd(4, 52) = ', gcd(4, 52)) # 4

# pi - 파이값
print(pi) # 3.141592653589793
# e - 자연상수
print(e) # 2.718281828459045

#### 그외 deque, priority_queue 참고