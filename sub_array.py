n = 4
arr = [1, 2, 3,4]
l = []
max_length = 0
obj = {}
for i in range(1 , n+1):
     obj[str(i)]=[]
for i in range(0,n):
    for j in range(i,n):
        a = arr[i:j+1]
        obj[str(len(a))].append(a)
print(obj) 