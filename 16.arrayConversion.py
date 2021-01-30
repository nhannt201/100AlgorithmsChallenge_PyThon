#Code by Nhan Nguyen
#Available on github.com/nhannt201

def arrLe(arr):
    new_arr = []
    for x in range(len(arr)-1):
        if x % 2 == 0:
            new_arr.append(arr[x] + arr[x+1])
        else:
            continue
    if len(new_arr) > 1:
        return  arrChan(new_arr)
    else:
        return new_arr

def arrChan(arr):
    arr_rs = []
    for y in range(len(arr)-1):
        if y % 2 == 0:
           arr_rs.append(arr[y] * arr[y+1])
        else:
            continue
    if len(arr_rs) > 1:
        return  arrLe(arr_rs)
    else:
        return arr_rs

def arrayConversion(arr):
    for x in range(len(arr)-1):
        arrs = []
        if x % 2 == 0:
            arrs = arrLe(arr)
        else:
            arrs = arrChan(arr)

    return arrs
                
   
inputArray = [1, 2, 3, 4, 5, 6, 7, 8]
print(arrayConversion(inputArray))
