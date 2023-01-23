# Lab09

* In the second program, the return of Str_length’s procedure is put in eax.
* We find that in repeat prefix, when ecx decrease to zero, ZF doesn’t be set,
Only when compare instrument equal to 0, ZF will be set.
If we want to check whether ecx == 0, we can use JECXZ.