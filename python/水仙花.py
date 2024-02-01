A = 1
B = 0
C = 0
while A < 10:
    A = A+1
    while B < 10:
        B = B + 1
        while C < 10:
            C = C + 1
            if A**3+B**3+C**3 == A*100+B*10+C :
                print(A*100+B*10+C,end = ",")
