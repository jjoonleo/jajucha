try:
    f = open("init.txt", "r")
    s = f.read()
    s = s.split()
    V = s[0:6]
    L = s[6:9]
    R = s[9:12]
    print(V)
    print(L)
    print(R)
    
except Exception as e:
    print("error: "+str(e))