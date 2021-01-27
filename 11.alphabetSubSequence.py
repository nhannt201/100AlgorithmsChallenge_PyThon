#Code by Nhan Nguyen
#Available on github.com/nhannt201
       
alphabetChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

def alphabetSubsequence(string):
    vitri = 0
    len_or = len(string)
    dung = 0
    for x in string:
        for y in range(vitri, len(alphabetChar)):
            if x == alphabetChar[y]:
                vitri = y
                dung = dung + 1

    if dung == len(string):
        return True
    else:
        return False
                

print(alphabetSubsequence("bxz"))
