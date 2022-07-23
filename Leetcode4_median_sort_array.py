import array as arr

def findMedianSortedArrays(num1, num2):
    A, B = num1, num2
    length = len(A) + len(B)
    half = length // 2

    if len(A) > len(B):
        A, B = B, A

    l, r = 0, len(A) - 1

    while True:
        i = (l + r) // 2  # A index
        j = half - i - 2

        aleft = A[i] if i >= 0 else float("-infinity")
        bleft = B[j] if j >= 0 else float("-infinity")
        aright = A[i + 1] if i < len(A) - 1 else float("infinity")
        bright = B[j + 1] if i < len(B) - 1 else float("infinity")

        if aleft <= bright and bleft <= aright:
            if length % 2:
                return min(aright, bright)

            else:
                return (max(aleft, bleft) + min(aright, bright)) / 2
        elif aleft > bright:
            r = i - 1
        else:
            l = i + 1




arry1 = arr.array('i', [5, 7, 8, 15])
arry2 = arr.array('i', [1, 2, 9, 10, 9, 11])

print(findMedianSortedArrays(arry1, arry2))
