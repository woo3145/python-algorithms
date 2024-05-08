# merge_sort.py

def merge_sort(arr):
    """
    병합 정렬을 사용하여 리스트를 정렬

    시간 복잡도(Time Complexity): O(n log n)
    공간 복잡도(Space Complexity): O(n)
    """

    if len(arr) <= 1:
        return arr

    # 리스트를 중간으로 나누기
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 각 절반을 재귀적으로 정렬
    merge_sort(left_half)
    merge_sort(right_half)

    # 정렬된 두 부분 병합
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # 왼쪽 절반에 남은 요소를 병합
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # 오른쪽 절반에 남은 요소를 병합
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return arr

example_list = [38, 27, 43, 3, 9, 82, 10]
print("Original list:", example_list)
sorted_list = merge_sort(example_list)
print("Sorted list:", sorted_list)
