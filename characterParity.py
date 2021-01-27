#characterParity
dauvao = input()

def chanle(dauvao):
    dauvao = int(dauvao)
    if (dauvao%2) == 0:
        print("so chan")
    else:
        print("so le")
    
if (dauvao.isnumeric() != True):
    print("Khong phai la so")
else:
    chanle(dauvao)

