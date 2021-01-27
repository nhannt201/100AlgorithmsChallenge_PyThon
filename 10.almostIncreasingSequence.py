#Code by Nhan Nguyen
#Available on github.com/nhannt201

#Cách 1 - Dùng tạm
def almostIncreasingSequence(arr):
    boolean = False
    #check lan 1
    if (arr[0] < arr[1]):
        boolean = True
        #check lan 2
        #so sanh arr[1] vs arr[x]
        if arr[0] < arr[2]:
            boolean = True
            #check lan 2
            #so sanh arr[1] vs arr[x]
            if len(arr) > 3:
                if arr[0] < arr[3]:
                    boolean = True
                else:
                    boolean = False
    else:
        boolean = False

    return boolean
    
            

sequence = [1, 3, 2, 1]
print(almostIncreasingSequence(sequence))

#Cách 2: Ổn - Đã thử nhiều case hơn
#Theo cách này thì so sánh 2 số liên tiếp    

def almostIncreasingSequence(arr):
    boolean = False
    up = 0
    down = 0
    for x in range(len(arr)):
        if x == len(arr) - 1:
            break
        else:
            if arr[x] < arr[x+1] or arr[x] == arr[x+1]:
                up = up + 1
            else:
                down = down + 1

    if up == 1 and down == 1:
        boolean = True
    elif up > down and down < 2:
        if len(arr) > 4:
            boolean = check3so(arr)
        else:
            boolean = True
        
    else:
        boolean = False
        
    return boolean #str(up) + " " + str(down)
    
            

sequence = [1, 5, 2, 4, 2 ,8, 9, 12, 15]
print(almostIncreasingSequence(sequence))
