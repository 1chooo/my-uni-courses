def print_2d_matrix(a) :

    for i in range(3) :
        for j in range(3) :
            print("%5.7f"%a[i][j], end = " ")
        print()
    print()

    return

def pivot(a, b, s, n, k) :

    p = k
    big = abs(a[k][k] / s[k])

    for ii in range(k, n) :
        dummy = abs(a[ii][k]) / s[ii]

        if dummy > big :
            big = dummy
            p = ii
    
    if p != k :
        for jj in range(k, n) :
            dummy = a[p][jj]
            a[p][jj] = a[k][jj]
            a[k][jj] = dummy

        dummy = b[p]
        b[p] = b[k]
        b[k] = dummy
        dummy = s[p]
        s[p] = s[k]
        s[k] = dummy
    
    return

def eliminate(a, s, n, b, tol, er) :

    for k in range(0, n) :
        pivot(a, b, s, n, k)
        print_2d_matrix(a)

        if (abs(a[k][k] / s[k]) < tol) :
            er = -1

            return

        for i in range(k + 1, n) :
            factor = a[i][k] / a[k][k]

            for j in range(k, n) :
                a[i][j] = a[i][j] - factor * a[k][j]
            
            a[i][2] = a[i][2] - factor * a[k][2]
    
    return

def gauss(a, b, n, x, tol, er) :

    s = [[], [], []]
    er = 0

    for i in range(0, 3) :
        s[i] = abs(a[i][0])

        for j in range(1, n) :
            if (abs(a[i][j]) > s[i]) :
                s[i] = abs(a[i][j])
    
    print_2d_matrix(a)
    eliminate(a, s, n, b, tol, er)


A = [[15, -3, -1], [-3, 18, -6], [-4, -1, 12]]
B = [3300, 1200, 2400]
s = [[], [], []]
x = []

gauss(A, B, 3, x, 1, 1)

print(A)
print(B)
print(s)