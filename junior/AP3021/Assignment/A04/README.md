# Assignment4

``` f90
FUNCTION Bisect(xl, xu, es, imax, xr, iter, ea) 
    iter = 0
    DO
        xrold = xr
        xr = (xl + xu) ∕ 2 iter = iter + 1
        IF xr ≠ 0 THEN
            ea = ABS((xr − xrold) ∕ xr) * 100 
        END IF
        test = f(xl) * f(xr) 
        IF test < 0 THEN
            xu = xr
        ELSE IF test > 0 THEN
            xl = xr 
        ELSE
            ea = 0 
        END IF
        IF ea < es OR iter ≥ imax 
            EXIT 
    END DO
    Bisect = xr 
END Bisect
```

``` f90
FUNCTION Bisect(xl, xu, es, imax, xr, iter, ea) iter = 0
    fl = f(xl)
    DO
        xrold = xr
        xr = (xl + xu) ∕ 2 
        fr = f(xr)
        iter = iter + 1
        IF xr ≠ 0 THEN
            ea = ABS((xr − xrold) ∕ xr) * 100 
        END IF
        test = fl * fr 
        IF test < 0 THEN
            xu = xr
        ELSE IF test > 0 THEN
            xl = xr
            fl = fr 
        ELSE
            ea = 0 
        END IF
        IF ea < es OR iter ≥ imax 
            EXIT 
    END DO
    Bisect = xr 
END Bisect
```

``` f90
FUNCTION ModFalsePos(xl, xu, es, imax, xr, iter, ea) 
    iter = 0
    fl = f(xl) fu = f(xu) 
    DO
        xrold = xr
        xr = xu − fu * (xl − xu) ∕ (fl − fu) 
        fr = f(xr)
        iter = iter + 1
        IF xr <> 0 THEN
            ea = Abs((xr − xrold) ∕ xr) * 100 
        END IF
        test = fl * fr 
        IF test < 0 THEN
            xu = xr
            fu = f(xu)
            iu = 0
            il = il + 1
            IF il ≥ 2 THEN 
                fl = fl ∕ 2
        ELSE IF test > 0 THEN 
            xl = xr
            fl = f(xl)
            il = 0
            iu = iu + 1
            IF iu ≥ 2 THEN 
                fu = fu ∕ 2
            END IF
        ELSE
            ea = 0
        END IF
        IF ea < es OR iter ≥ imax 
            THEN EXIT
        END IF 
    END DO
    ModFalsePos = xr 
END MODFALSEPOS
```