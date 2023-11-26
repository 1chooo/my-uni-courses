# %% [markdown]
# # [2022 Fall] Assignment5-4
# 
# > Course: AP3021

# %% [markdown]
# ## Q5-4
# 
# Develop, debug, and test a program in either a high-level language or macro langrage of your choice to solve a system of equations with Gauss elimination with partial pivoting. Base the program on the pseudocode from Fig. 9.6. Test the program using the following system (which has an answer of $𝑥_1 = 𝑥_2 = 𝑥_3 = 1$) (Python)
# 
# 
# $x_1 +2x_2 –x_3 =2$
# 
# $5x_1 +2x_2 +2x_3 =9$
# 
# $-3x_1 +5x_2 –x_3 =1$

# %% [markdown]
# ### Pseudocode Gauss
# 
# ``` c
# SUB Gauss(a, b, n, x, tol, er)
#     DIMENSION s(n)
#     er = 0
#     DOFOR i = 1, n
#         si = ABS(a[i][1])
#         DOFOR j = 2, n
#             IF ABS(a[i][j]) > si THEN
#                 si = ABS(a[i][j])
#         ENDDO
#     ENDDO
# 
#     CALL Eliminate(a, s, n, b, tol, er)
# 
#     IF (er != -1) THEN
#         CALL Substitute(a, n, b, x)
#     ENDIF
# END Gauss
# ```
# 
# ### Pseudocode Elminate
# 
# ``` c
# SUB Eliminate(a, s, n, b, tol, er)
#     DOFOR k = 1, n - 1
#         CALL Pivot(a, b, s, n, k)
# 
#         IF ABS(a[k][k] / s[k]) < tol THEN
#             er = 01
#             EXIT DO
#         END IF
#     
#         DOFOR i = k + 1, n
#             factor = a[i][k] / a[k][k]
#             DOFOR j = k + 1, n
#                 a[i][j] = a[i][j] - factor * a[k][j]
#             ENDDO
# 
#             b[i] = b[i] - factor * bk
#         ENDDO
#     ENDDO
# 
#     IF ABS(a[n][n] / s[n]) < tol THEN
#         er = -1
#     ENDIF
# END Eliminate
# ```
# 
# ### Pseudocode Pivot
# 
# ``` c
# SUB Pivot(a, b, s, n, k)
#     p = k
#     big = ABS(a[k][k] / s[k])
#     DOFOR ii = k + 1, n
#         dummy = ABS(a[ii][k] / s[ii])
#         IF dummy > big THEN
#             big = dummy
#             p = ii
#         END IF
#     ENDDO
# 
#     IF p != k THEN
#         DOFOR jj = k, n
#             dummy = a[p][jj]
#             a[p][jj] = a[k][jj]
#             a[k][jj] = dummy
#         ENDDO
# 
#         dummy = b[p]
#         b[p] = b[k]
#         b[k] = summy
#         dummy = s[p]
#         s[p] = s[k]
#         s[k] = dummy
#     END IF
# END Pivot
# ```
# 
# ### Pseudocode Subsitute
# 
# ``` c
# SUB Substitute(a, n, b, x)
#     x[n] = b[n] / a[n][n]
# 
#     DOFOR i = n - 1, 1, -1
#         sum = 0
#         DOFOR j = i + 1, n
#             sum = sum + a[i][j] * x[j]
#         ENDDO
#         x[n] = (b[n] - sum) / a[n][n]
#     ENDDO
# END Substitute
# ```

# %%
#9.18
import numpy as np

def pivot(a, b):                 
    p = np.array((a), float)
    q = np.array((b), float)
    n = len(q)

    for i in range(0, n - 1) :
        if abs(p[i, 1]) == 0 : 
            for k in range(i + 1, n) :
                if abs((p[k, i])) > abs(p[i, i]) :
                    p[[i, k]] = p[[k, i]] 
                    q[[i, k]] = q[[k, i]]
                    break
        for j in range(i + 1, n):
            f = p[j][i] / p[i][i] 
            p[j,:] = p[j,:] - f * p[i,:]
            q[j] = q[j] -f * q[i]

    return p, q


def back_substituted(a, b) : 
    n = b.size
    x = np.zeros(n)

    x[n - 1] = b[n - 1] / a[n - 1,n - 1]

    for i in range(n - 2, -1, -1) :
        sum1 = 0

        for j in range(i + 1, n) :
            sum1 = sum1 + a[i, j] * x[j]
        x[i] = (b[i] - sum1) / a[i, i]

    return x


xx = np.array([[ 1, 2, -1], 
               [ 5, 2,  2], 
               [-3, 5, -1]])
t = np.array([2, 9, 1])
a, b = pivot(xx, t)
x = back_substituted(a, b)

print('[x1, x2, x3] =', x)

# %%
import numpy as np

def print_2d_matrix(data) :

    for i in range(data.shape[0]) :
        for j in range(data.shape[1]) :
            print("%5.7f"%data[i][j], end = " ")
        print()
    print()

    return

def substitute(data, n, b, x) :
    
    for i in range(n, 0, -1) :
        sum = 0

        for j in range(i, n) :
            sum = sum + data[i - 1][j] * x[i]
        
        x[i - 1] = (b[i - 1] - sum) / data[i - 1][i - 1]
    
    print(x)

    return


def pivot(data, b, s, n, k) :

    p = k
    big = abs(data[k][k] / s[k])

    for ii in range(k, n) :
        dummy = abs(data[ii][k] / s[ii])

        if dummy > big :
            big = dummy
            p = ii

    if p != k :
        for jj in range(k, n) :
            dummy = data[p][jj]
            data[p][jj] = data[k][jj]
            data[k][jj] = dummy

        dummy = data[p][n]
        data[p][n] = data[k][n]
        data[k][n] = dummy
        dummy = s[p]
        s[p] = s[k]
        s[k] = dummy

    return


def eliminate(data, s, n, b, tol, er) :
    for k in range(n - 1) :
        pivot(data, b, s, n, k)
        print_2d_matrix(data)

        if abs(data[k][k] / s[k]) < tol :
            er = -1

            return

        for i in range(k + 1, n) :
            factor = data[i][k] / data[k][k]

            for j in range(k, n) :
                data[i][j] = data[i][j] - factor * data[k][j]
            
            data[i][n] = data[i][n] - factor * data[k][n]
            print_2d_matrix(data)
    
    return


def gauss() :

    er = 1
    tol = 1
    data = np.array([[ 1, 2, -1, 2], 
                     [ 5, 2,  2, 9],
                     [-3, 5, -1, 1]], dtype="float")
    n = data.shape[0]
    b = np.zeros(n)
    s = np.zeros(n)
    x = np.zeros(n)

    for i in range(n) :
        s[i] = abs(data[i][0])

        for j in range(1, n) :
            if abs(data[i][j] > s[i]) :
                s[i] = abs(data[i][j])
    
    print_2d_matrix(data)
    eliminate(data, s, n, b, tol, er)

    if er != -1 :
        b = data[:, n]
        substitute(data, n, b, x)

    return

gauss()


