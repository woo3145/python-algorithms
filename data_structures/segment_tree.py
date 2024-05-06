# 세그먼트 트리(Segment Tree)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.tree[self.n:] = arr[:]
        self.build()

    def f(self, a, b):
        return a + b

    def build(self):
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.f(self.tree[i << 1], self.tree[i << 1 | 1])

    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1: # 왼쪽 구간이 오른쪽 자식이면 연산
                res = self.f(res, self.tree[l])
                l += 1
            if not r & 1: ## 오른쪽 구간이 왼쪽 자식이면 연산
                res = self.f(res, self.tree[r])
                r -= 1
            ## 부모노드로 이동
            l >>= 1 
            r >>= 1
        return res

    def update(self, idx, val):
        i = self.n + idx
        self.tree[i] = val
        while i >= 1:
            i >>= 1
            self.tree[i] = self.f(self.tree[i << 1], self.tree[i << 1 | 1])

arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print(st.query(1, 3))  # 출력: 15 (인덱스 1부터 3까지의 합)
st.update(2, 10)
print(st.query(1, 3))  # 출력: 20 (인덱스 1부터 3까지의 합, 5를 10으로 변경하여 합이 변경됨)
