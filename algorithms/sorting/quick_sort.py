def quick_sort(arr):
    """
    퀵 정렬
    
    시간 복잡도:
        - 최선: O(n log n)
        - 평균: O(n log n)
        - 최악: O(n^2) (피벗 선택이 좋지 않을 경우)
    
    공간 복잡도:
        - O(log n) (재귀 호출로 인한 스택 사용)
    """
    def partition(low, high, lst):
        # 마지막 요소를 피벗으로 선택
        pivot = lst[high]
        i = low - 1  # 작은 요소들의 인덱스

        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]  # 교환

        lst[i + 1], lst[high] = lst[high], lst[i + 1]  # 피벗을 올바른 위치로 이동
        return i + 1

    def quicksort_recursive(low, high, lst):
        if low < high:
            # 분할 인덱스
            pi = partition(low, high, lst)

            # 분할 인덱스 앞뒤로 재귀적으로 정렬
            quicksort_recursive(low, pi - 1, lst)
            quicksort_recursive(pi + 1, high, lst)

    sorted_arr = arr[:]
    quicksort_recursive(0, len(sorted_arr) - 1, sorted_arr)
    return sorted_arr


example_list = [10, 7, 8, 9, 1, 5]
print("Original list:", example_list)
sorted_list = quick_sort(example_list)
print("Sorted list:", sorted_list)
