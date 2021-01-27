#Code by Nhan Nguyen
#Available on github.com/nhannt201
       
def alternatingSums(arr):
    sums = [0, 0]
    for  i in range(len(arr)):
        sums[i % 2] += arr[i]

    return sums

a = [50, 60, 60, 45, 70]
print(alternatingSums(a))
