
n=str(input("請輸入任意數字:"))

if int(n)<0 or int(n)/10==0 or (int(n)/10==0):
    print("不是回文")
if n == n[::-1] :
    print("是回文")
else :
    print("不是回文")

# #leetcod

# 1.return str(x) == str(x)[::-1]


