#Code by Nhan Nguyen
#Available on github.com/nhannt201
#Tham khao: https://codelearn.io/training/detail/3880
def arrayChange(a):
    d=0
    for i in range(1,len(a)):
        if a[i]<=a[i-1]:
            const=int(a[i])
            a[i]=a[i-1]+1
            d+=a[i]-const
    return d
                
   
                
                
   
inputArray = [1, 1, 1]
print(arrayChange(inputArray))
