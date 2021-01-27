#isPalin
def isPali(s):
    s = s.lower()
    if (s == s[::-1]):
        print("True")
    else:
        print("False")
     
s = "madAm"
isPali(s)
