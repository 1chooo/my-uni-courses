# Chapter Two

### Euler Pseudocode

``` f90
FUNCTION Euler(dt, ti, tf, yi)

t = ti
y = yi
h = dt

DO
    if t + dt > tf then
        h = tf -t
    endif
    dydt = dy(t, y)
    y = y + dydt * h
    t = t + h
    if t >= tf exit
ENDDO

Euler = y

END Euler
```