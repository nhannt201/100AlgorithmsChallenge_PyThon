#Code by Nhan Nguyen
#Available on github.com/nhannt201

def arrayMaximalAdjacentDifference(arr):
    max = arr[0]
    for x in range(0, len(arr)-1):
        if max < (abs(arr[x]-arr[x+1])):
            max = (abs(arr[x]-arr[x+1]))
    return max
                
inputArray = [2, 9, 1, 0]
print(arrayMaximalAdjacentDifference(inputArray))
