#Code by Nhan Nguyen
#Available on github.com/nhannt201

def arrayMaxConsecutiveSum(arr, k):
    sum_arr = []
    #cach 1, minh thay de hieu voi minh hon :')
    for x in range(0, len(arr)-1):
        begin = x
        end = begin + k
        sum_arr.append(sum(arr[begin:end]))
    return sum_arr
    #Cach 2
    #return [sum(i) for i in zip(*(inputArray[i:] for i in range(k)))]
                
inputArray = [2, 3, 5, 1, 6]
print(arrayMaxConsecutiveSum(inputArray, 2))
