a = [8, 1, 3, 6, 9, 2]
n = len(a)
def bubble_sort(a, n):
    for i in range(0, n-1):
        for j in range(0, n - 1 -i): # - 1 để tránh phần tử bị tràn ra ngoài vd 6 pt lap lai 5 lan,- i sau khi chon duoc phan tu lon thi bo qua phan tử đó
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] # cth đổi chỗ a[j] và a[j+1]
bubble_sort(a, n)
for i in range(n):
    print(a[i], end = " ")