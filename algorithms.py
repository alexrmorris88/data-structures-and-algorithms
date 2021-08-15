# =============================================================================
# Bubble Sort Algorithm
# =============================================================================


def BubbleSort(x):
    n = len(x)

    for i in range(n):
        for j in range(0, n - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]


# x = [22, 4, 1, 500, 7, 9, 2000, 5]
#
# BubbleSort(x)
#
# for i in range(len(x)):
#     print(x[i], end=" ")


# =============================================================================
# Merge Sort Algorithm
# =============================================================================


def MergeSort(x):
    if len(x) > 1:
        mid = len(x) // 2
        L = x[:mid]
        R = x[mid:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                x[k] = L[i]
                i += 1
                k += 1
            else:
                x[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            x[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            x[k] = R[j]
            j += 1
            k += 1


def printList(x):
    for i in range(len(x)):
        print(x[i], end=" ")
    print()

# if __name__ == "__main__":
#     x = [12, 11, 13, 15, 7, 5, 10, 1, 4, 3, 9]
#     printList(x)
#     MergeSort(x)
#     printList(x)


# =============================================================================
# Quick Sort Algorithm
# =============================================================================


def MergeSort(x):
    if len(x) > 1:
        mid = len(x) // 2
        L = x[:mid]
        R = x[mid:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                x[k] = L[i]
                i += 1
                k += 1
            else:
                x[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            x[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            x[k] = R[j]
            j += 1
            k += 1

def printList(x):
    for i in range(len(x)):
        print(x[i], end=" ")
    print()


# if __name__ == "__main__":
#     x = [12, 11, 13, 15, 7, 5, 10, 1, 4, 3, 9]
#     printList(x)
#     MergeSort(x)
#     printList(x)



# =============================================================================
# Quick Sort Algorithm
# =============================================================================


def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if(start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


def quick_sort(start, end, array):

    if (start < end):

        p = partition(start, end, array)

        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


# if __name__ == "__main__":
#     array = [ 1000, 10, 7, 8, 9, 1, 5, 100, 88, 33, 6, 11, 20, 30, 40 ]
#     quick_sort(0, len(array) - 1, array)
#     print(f'Sorted array: {array}')


# =============================================================================
# Heap Sort Algorithm
# =============================================================================


def heapify(arr, n, i):
    largest = i
    L = 2 * i + 1
    R = 2 * i + 2

    if L < n and arr[largest] < arr[L]:
        largest = L

    if R < n and arr[largest] < arr[R]:
        largest = R

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# if __name__ == "__main__":
#     arr = [12, 11, 13, 5, 6, 7]
#     heapSort(arr)
#     for i in range(len(arr)):
#         print(arr[i], end=" ")


# =============================================================================
# Finding a Peak - Stright Forward Approach
# =============================================================================


def findPeak(array, n):
    if(n == 1):
        return 0
    if(array[0] >= array[1]):
        return 0
    if(array[n - 1] >= array[n - 2]):
        return n - 1

    for i in range(1, n - 1):
        if(array[i] >= array[i - 1] and array[i] >= array[i + 1]):
            return i


if __name__ == "__main__":
    array = [ 1, 3, 5, 66, 9, 5, 77, 2, 10, 100, 90]
    n = len(array)
    print(f"The peak is {findPeak(array, n)}")











