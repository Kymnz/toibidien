m = [5, 6, 3, 1, 8, 7, 2, 4]
# k=2, x=3
# i=k-1=2-1=1, ds[1] =6 > x=3
#[5,, 6, 1, 8, 7, 2, 4], i=i-1=1-1=0,{ds[0]=5} > x=3
#[,5, 6, 1, 8, 7, 2, 4], i=0-1=-1,{ds[-1+1]=3}
#[3, 5, 6, 1, 8, 7, 2, 4]
# k = 3 , x = 1
# i = k - 1 = 3 - 1 = 2, ds[2] = 6 > x = 1
#[3,5,, 6,  8, 7, 2, 4], i = i -1= 2 -1 = 1, ds[1] =5 > x= 1
# [3,, 5, 6, 8, 7, 2, 4], i= 0, ds[0] = 3 > x=1
#[,,3, 5, 6, 8, 7, 2, 4], i= -1, ds[-1 +1]=
def chen(ds, x, k):#ds= tổng số nghiệm cần xét, x = giá trị tại vị trí k trong ds
    i = k - 1 #vị trí xét đầu tiên
    while (ds[i] > x) and (i >= 0): # tại ví trí i > x điều kiện i >= 0
        ds[i + 1] = ds[i] #dịch chuyển vị trí đang xét
        i = i - 1
    ds[i+1] = x # kết thúc vòng lặp khi không thỏa điều kiện
for j in range(1,len(m), 1): # từ 1 đến vị trí cuối cùng của m step =1
    chen(m, m[j], j)
print(m)