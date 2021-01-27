#Code by Nhan Nguyen
#Available on github.com/nhannt201
def findX(arr):
    tichlon = arr[0]*arr[1]
    for x in range(len(arr)):
        if (x == ((len(arr)) - 1)):
            break
        else:
            if ((arr[x]*arr[x+1]) > tichlon):
                tichlon = arr[x]*arr[x+1]
    print(tichlon)

inputArray = []
print("So phan tu cua mang: ", end="")
total = int(input())
while total < 2: #Một mảng các số nguyên có chứa ít nhất hai phần tử
    print("So phan tu cua mang: ", end="")
    total = int(input())
else:
    count = 0;
    while count <= total:
        print("Nhap phan tu [" + str(count) + "] = ", end="")
        inputArray.append(int(input()))
        count = count + 1
    else:
        print("Phan tu lien ke co tich lon nhat la:")
        findX(inputArray)
