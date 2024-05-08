def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 내부 루프에서 교환이 일어나지 않으면 정렬이 완료된 것으로 간주
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
    

example_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", example_list)
sorted_list = bubble_sort(example_list)
print("Sorted list:", sorted_list)