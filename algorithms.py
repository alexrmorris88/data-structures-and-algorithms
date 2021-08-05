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

if __name__ == "__main__":
    x = [12, 11, 13, 15, 7, 5, 10, 1, 4, 3, 9]
    printList(x)
    MergeSort(x)
    printList(x)


