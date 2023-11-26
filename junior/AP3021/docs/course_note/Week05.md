# Week05

### plot

### Cramer's rule

### Naive Gauss

``` f90
do k = 1, n - 1
    do i = k + 1, n
        factor = a(i, k) / a(k, k)
        do j = k + 1, n
            a(i, j) = a(i, j) - factor * a(k, j)
        enddo
        b(i) = b(i) - factor * b(k)
    enddo
enddo
```

* ill-conditioned systems
  * small change in coefficients results in large scale.
  * wide range of the answers.
  * determinant close to zero.

* condition number
  * standardlize -> pick up the maximum element.

* Improve
  * use more significant figures
  * pick up the great pivot
    * avoid divide zero and round-off error
  * scaling
    * we not include scaling into the system.
### Flops