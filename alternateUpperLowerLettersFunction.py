def myfunc(mystring):
    mystring = list(mystring)
    end = len(mystring)
    for i in range(0,end,1):
        if i == 0:
            mystring[i] = mystring[i].upper()
        elif i == 1:
            mystring[i] = mystring[i].lower()
        elif i % 2 == 0:
            mystring[i] = mystring[i].upper()
        else:
            mystring[i] = mystring[i].lower()
    return "".join(mystring)