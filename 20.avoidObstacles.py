#Code by Nhan Nguyen
#Available on github.com/nhannt201
#Tham khao: https://sites.google.com/site/tranquangtanqt1990/learn-code/codefights/arcade/1-intro/level-5_4-avoidobstacles

def avoidObstacles(arr):
    for x in range(1, 40):
        count = 0
        for y in range(len(arr)-1):
            if(arr[y] % x == 0):
                break
            count = count + 1
            if count >= len(arr)-1:
                return x
                
inputArray =  [5, 3, 6, 7, 9]
print(avoidObstacles(inputArray))
