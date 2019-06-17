#count = 0
INF = float('inf')
def merge(A, left, mid, right):
    #global count
    # n1 = mid - left
    # n2 = right - mid
    L = A[left:mid] + [INF]
    R = A[mid:right] + [INF]
    """ここを変えたらだいぶ早くなった。
    # L = [0]*(n1+1)
    # R = [0]*(n2+1)
    # for i in range(n1):
    #     L[i] = A[left + i]
    # for i in range(n2):
    #     R[i] = A[mid+i]
    # L[n1] = float('inf')
    # R[n2] = float('inf')
    """
    i,  j = 0, 0
    for k in range(left, right):
        #count +=1
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1


def mergeSort(A, left, right):
    if left+1 < right:
        mid =  int((left+right)/2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)



#right は部分配列の末尾+1 の要素を指す。

#n = int(input())
A = list(map(int, input().split()))
n = len(A)
mergeSort(A, 0, n)
for i in range(n):
    if i>0:
        print(" ", end="")
    print(A[i], end="")
print()
# print(count)