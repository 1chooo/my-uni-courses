# Chapter01 - Basic Concepts

1. Requirements
2. Analysis
3. Design
4. Refinement and coding
5. Verification

## **Intro to Algorithm**
1. Sort
2. Compare
3. Search
4. Recursive

## **Data Abstraction**

### Struct

It's the collections of the elements whose data types need not be the same. -> They are explicitly defined.

``` c
struct student {
    char last_name;
    int student_id;
    char grade;
}
```

### Abstract data type(ADT).

implementation-independent.
1. Creator/Constructor
2. Transformers
3. Observers/Reporters

**The symbol `::=` -> should be read as "is defined as".**

## **Performance analysis**

* Fixed space requirements. 
  * The component refers to space requirements that do not depend on the number and size of the program's inputs and outputs.
* Variable space requirements.
  * $S(P) = c +S_{p}(I)$


> $S_{abc}(I) = 0$
> ``` c
> /* Three inputs, this function has only fixed space requirements. */
> float abc(float a, float b, float c) {
>     return a + b + b * c + (a + b - c) / (a + b) + 4.00;
> }
> ```

``` c
/*  */
float sum(float list[], int n) {
    float tempSum = 0;
    int i;

    for (i = 0; i < n; i++) 
        tempSum += list[i];
    
    return tempSum;
}
```

### Time complexity

#### Magic square