# PPL Final Note

Static Scoping: Static scoping is thus named because the scope of a variable can be statically determined, that is, piror to execution. -> subprograms can be nested.

all scopes are associated with program units.

Hidden declaration

```c
void sub() {
    int count;          // hidden

    while (...) {
        int count;      // only funtion in while loop
        count++;
            :
    }
        :               // the first count show up
}
```

Scope rules
C++ allows variable definitions to appear anywhere in functions. 
When a definition appears at a position other than at the beginning of a function, but not within a block, that variable's scope is from its definition statement to the end of the function. 
Note that in C, all data declarations in a function but not in blocks within the function MUST appear at the beginning of the function.
