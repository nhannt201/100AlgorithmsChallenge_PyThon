#Code by Nhan Nguyen
#Available on github.com/nhannt201

def arrayPreviousLess(arr):
    new_arr = [-1]
    for x in range(0, len(arr)-1):
        if arr[x] < arr[x+1]:
            new_arr.append(arr[x])
        else:
            new_arr.append(-1)
    return new_arr
                
inputArray = [3, 5, 2, 4, 5]
print(arrayPreviousLess(inputArray))
