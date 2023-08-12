def substitute(a, n, b, x) :
    # print(x, b, a)
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1) :
        sum = 0
        for j in range(i, n) :
            sum = sum + a[i][j] * x[j]

        x[n - 1] = (b[n - 1] - sum) / a[n - 1][n - 1]

    return

def gauss(a, b, n, x, tol, er) :
    s = []

    for i in range(0, n) :
        temp = a[i][0]
        for j in range(1, 3) :
            if a[i][j] > temp :
                temp = a[i][j]
        s.append(temp)
    
    for k in range(0, n - 1) :
        p = k
        big = abs(a[k][k] / s[k])

        for ii in range(k + 1, n) :
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

        if abs(a[k][k]) / s[k] < tol :
            er = -1
            break

        for i in range(k + 1, n) :
            factor = a[i][k] / a[k][k]
            for j in range(k + 1, n) :
                a[i][j] = a[i][j] - factor * a[k][j]
            
            b[i] = b[i] - factor * b[k]

            if abs(a[n - 1][n - 1]) / s[n - 1] < tol:
                er = -1
    if er != -1 :
        substitute(a, n, b, x) 

    return

A = [[1, 2, -1], [5, 2, 2], [-3, 5, -1]]
B = [2, 9, 1]
X = [0, 0, 0]
gauss(A, B, 3, X, 0, 0)
print(X)