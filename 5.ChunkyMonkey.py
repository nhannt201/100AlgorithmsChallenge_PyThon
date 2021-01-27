#ChunkyMonkey
def reshape(lst, n):
    return [lst[:n], lst[(n+1):]]

print (reshape([1,2,3,4,5,6], 2))
