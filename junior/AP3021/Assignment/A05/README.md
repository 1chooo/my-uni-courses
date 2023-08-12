### Pseudocode Gauss

``` c
SUB Gauss(a, b, n, x, tol, er)
    DIMENSION s(n)
    er = 0
    DOFOR i = 1, n
        si = ABS(a[i][1])
        DOFOR j = 2, n
            IF ABS(a[i][j]) > si THEN
                si = ABS(a[i][j])
        ENDDO
    ENDDO

    CALL Eliminate(a, s, n, b, tol, er)

    IF (er != -1) THEN
        CALL Substitute(a, n, b, x)
    ENDIF
END Gauss
```

### Pseudocode Elminate

``` c
SUB Eliminate(a, s, n, b, tol, er)
    DOFOR k = 1, n - 1
        CALL Pivot(a, b, s, n, k)

        IF ABS(a[k][k] / s[k]) < tol THEN
            er = 01
            EXIT DO
        END IF
    
        DOFOR i = k + 1, n
            factor = a[i][k] / a[k][k]
            DOFOR j = k + 1, n
                a[i][j] = a[i][j] - factor * a[k][j]
            ENDDO

            b[i] = b[i] - factor * bk
        ENDDO
    ENDDO

    IF ABS(a[n][n] / s[n]) < tol THEN
        er = -1
    ENDIF
END Eliminate
```

### Pseudocode Pivot

``` c
SUB Pivot(a, b, s, n, k)
    p = k
    big = ABS(a[k][k] / s[k])
    DOFOR ii = k + 1, n
        dummy = ABS(a[ii][k] / s[ii])
        IF dummy > big THEN
            big = dummy
            p = ii
        END IF
    ENDDO

    IF p != k THEN
        DOFOR jj = k, n
            dummy = a[p][jj]
            a[p][jj] = a[k][jj]
            a[k][jj] = dummy
        ENDDO

        dummy = b[p]
        b[p] = b[k]
        b[k] = summy
        dummy = s[p]
        s[p] = s[k]
        s[k] = dummy
    END IF
END Pivot
```

### Pseudocode Subsitute

``` c
SUB Substitute(a, n, b, x)
    x[n] = b[n] / a[n][n]

    DOFOR i = n - 1, 1, -1
        sum = 0
        DOFOR j = i + 1, n
            sum = sum + a[i][j] * x[j]
        ENDDO
        x[n] = (b[n] - sum) / a[n][n]
    ENDDO
END Substitute
```