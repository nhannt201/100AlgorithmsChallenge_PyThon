#Code by Nhan Nguyen
#Available on github.com/nhannt201
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
##            for x in range(len(arr)):
##                if x == 0 and x == 1:
##                    continue
##                else:
##                    if x == len(arr) - 1:
##                        break
##                    else:
##                        if arr[x] > arr[x+1]:
##                             boolean = False
    else:
        boolean = False

    return boolean
    
            

sequence = [1, 3, 2, 1]
print(almostIncreasingSequence(sequence))
