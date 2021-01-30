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

#Cái dưới đây là sau khi đã tham khảo 1 code khác, nhìn chung test thấy kết quả không khác lắm
#Tham khảo: https://gist.github.com/wdospinal/a28ccd0c15a3befa7250a08672992d30

def arrLe(arr):
    new_arr = []
    for x in range(len(arr)-1):
         if x % 2 == 0:
            new_arr.append(arr[x] + arr[x+1])
    return new_arr

def arrChan(arr):
    arr_rs = []
    for y in range(len(arr)-1):
        if y % 2 == 0:
           arr_rs.append(arr[y] * arr[y+1])
    return arr_rs

def arrayRecursive(inputArray, state):
    if (len(inputArray)) == 1:
        return inputArray[0]
    else:
        if state:
            return arrayRecursive(arrLe(inputArray), False)
        else:
            return arrayRecursive(arrChan(inputArray), True)



def arrayConversion(arr):
    return arrayRecursive(inputArray, True)
                
   
inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arrayConversion(inputArray))

