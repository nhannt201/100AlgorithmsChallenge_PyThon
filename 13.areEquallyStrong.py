#Code by Nhan Nguyen
#Available on github.com/nhannt201
       
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    boolean = False;
    #Truong hop hai ben bang nhau
    if yourLeft == friendsLeft and yourRight == friendsRight:
        boolean = True
    #Truong hop bang cheo nhau
    elif yourLeft == friendsRight and yourRight == friendsLeft:
        boolean = True
    #Truong hop tong hai tay cua hai nguoi bang nhau
    elif (yourLeft + yourRight) == (friendsLeft + friendsRight):
        boolean = True
    else:
        boolean = False
    return boolean
        
yourLeft = 10
yourRight = 15
friendsLeft = 15
friendsRight = 9

print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))
