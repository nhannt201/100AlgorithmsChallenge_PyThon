#Code by Nhan Nguyen
#Available on github.com/nhannt201

def areSimilar(a, b):
    boolean = True
    arr_tam = [];
    for x in a:
        for y in b:
            if x == y:
                #boolean = True
                if x in arr_tam:
                    boolean = False
                else:
                    arr_tam.append(x)
    return boolean
                
                
   
a = [1, 2, 2]
b = [2, 1, 1]
print(areSimilar(a, b))
