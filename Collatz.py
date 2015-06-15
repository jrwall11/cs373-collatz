#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

myDict = {1 : 1}
# assert type(myDict) is dict 

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_cyclelen
# ------------

def collatz_cyclelen(n) :
    """
    calculate cycle length and insert into global cache
    """
    global myDict
    assert n >= 1
    v = 0
    original = n
    while n > 1 :
        if n in myDict :
            myDict[original] = myDict[n] + v
            #print (original)
            #print (myDict[n] + v)
            return myDict[n] + v
        else :
            if n % 2 == 0 :
                n //= 2
                v += 1
            else :
                n = n + (n >> 1) + 1
                v += 2
    v += 1
    #print (original)
    #print (v)
    myDict[original] = v
    return v


# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    global myDict
    temp = 0
    # declare maxcycle and return maxcycle as answer
    maxcycle = 1 
    for x in range(i, j):
        temp = collatz_cyclelen(x)
        #print(temp)
        if maxcycle < temp :
            maxcycle = temp
    #print (myDict)
    return maxcycle

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
