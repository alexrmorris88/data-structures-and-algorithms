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


if __name__ == "__main__":
    array = [ 1000, 10, 7, 8, 9, 1, 5, 100, 88, 33, 6, 11, 20, 30, 40 ]
    quick_sort(0, len(array) - 1, array)
    print(f'Sorted array: {array}')