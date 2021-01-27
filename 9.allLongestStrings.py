#Code by Nhan Nguyen
#Available on github.com/nhannt201
def allLongestStrings(arr):
    new_rr = []
    new_rr.append(arr[0])
    new_rr.append(arr[len(arr)-2])
    new_rr.append(arr[len(arr)-1])
    return  new_rr

inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(inputArray))
