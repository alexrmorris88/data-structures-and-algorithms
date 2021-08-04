# =============================================================================
# Bubble Sort Algorithm
# =============================================================================


def BubbleSort(x):
    n = len(x)

    for i in range(n):
        for j in range(0, n - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]


x = [22, 4, 1, 500, 7, 9, 2000, 5]

BubbleSort(x)

for i in range(len(x)):
    print(x[i], end=" ")