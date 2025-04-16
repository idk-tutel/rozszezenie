def find(n, arr):
    #LOGIKA
    i = 0
    def cos():
        while(len(arr)!=1):
            if arr[len(arr)//2] >= n:
                arr = arr[(len(arr)//2):]
                i += (len(arr)//2)-2
            else:
                arr = arr[:(len(arr)//2)]
        return i


arr = [1, 5, 7, 8, 10 ,14, 17, 19, 27, 29, 34, 35,36,39,43,46,58,59,60,64,69,72,74,76,77,81,84,87,89,94,99]
print(arr)

print(arr[3:])

print(arr[:4])
print(find(77, arr))