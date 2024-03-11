Problem 1.a This statement is a poorly phrased version of Fermat's last theorem. We know that we can find n > 2 for which ‚the equation holds. Fermat scribbled a note on a text margin indicating that he had found the solution for n = 2. Unfortunately, the proof died with him. Because the statement is phrased as a question‚ rather than a clearly defined algorithm, it lacks definiteness.

Problem 1.b This statement violates not only the rules of mathematics, but the criterion of effectiveness. We can compute only those things that are feasible, and division by zero is mathematically undefined.


1-3-1

ADT NaturalNumber is objects:
an ordered subrange of the integers starting at zero and ending at the maximum integer (INT_MAX) on the computer functions: for all x, y ∈ NaturalNumber; TRUE, FALSE ∈ Boolean and where +, −, <, and == are the usual integer operations 

NaturalNumber Zero( )	::= 0

Boolean IsZero(x)	::= if (x) return FALSE
     return TRUE
Boolean Equal(x, y)	::= if (x == y) return TRUE
    return FALSE
NaturalNumber Successor(x)	::= if (x == INT_MAX) return x
     return x + 1
NaturalNumber Add(x, y)	::= if ((x + y) < INT_MAX) return x + y
     if ((x + y) == INT_MAX) return x + y
    return INT_MAX
NaturalNumber Subtract(x, y)	::= if (x < y) return 0
     return x − y
NaturalNumber Predecessor(x)	::= if (x < 0) return ERROR
     if (x == 0) return 0
     return x - 1
Boolean IsGreater(x, y)	:= if ((x-y)) < 0) return ERROR
     if ((x-y)) == 0) return FALSE
     return TRUE
NaturalNumber mult(x, y)	
::= if (x < 0) return ERROR
     if (y < 0) return ERROR
     if (y == 1) return x
     return x + mult(x, y-1)
NaturalNumber div(x, y)	
::= if (x < 0) return ERROR
     if (y < 0) return ERROR
     if (y == 0) return ERROR
     if (y == 1) return 1
     return x - div(x, y-1)

end NaturalNumber

1-3-2

ADT Set is objects:
a subrange of the integers starting at (INT_MIN) and ending at the
maximum integer (INT_MAX) on the computer functions: for
all x, y ∈ Set; TRUE, FALSE ∈ Boolean and the Boolean operations defined in Problem 4 are available (not, and, or,...)
and where ==, Ø, +, head(s), tail(s) are the usual set operations,
where == return TRUE if tw set elements are the same, and TRUE otherwise.
Ø is the empty set.
+ adds and element to a set.
head(s) extracts the first member in the set.
tail(s) extracts a list of all other elements in the set. An empty set contains no tail. A set with only one element has the emtpy set has it tail.

Set Create(s)	::= Ø
Boolean IsEmpty(s)	::= if (s ==Ø ) return TRUE
     return FALSE
Boolean IsIn(x, s)	::= if (IsEmpty(s)) return FALSE
     if (x == head(s) return TRUE
    return IsIn(x, Tail(s))
Set Insert(x,s)	::= if (IsEmpty(s)) return x + s
     if (IsIn(a,s)) return s
    return x + s
Set Remove(x, s)	::= if (x == head(s)) return tail(s)
     return Remove(x, tail(s))
Set Union(x, s1, s2)	::= if IsEmpty(s1) return s2
     if IsIn(head(s1), s2)) return Union(x, tail(s1), s2)
     return head(s1) + Union(x, tail(s1), s2)
set Intersection(x, s1,s2)	::= if IsEmpty(s1) return Ø
     if IsIn(head(s1), s2)) return head(s1) + Intersection(x, tail(s1), s2)
     return Intersection(x, tail(s1), s2)
Boolean Difference(s1,s2)	::= if IsEmpty(s1) return Ø
     if IsIn(head(s1), s2)) return Difference(x, tail(s1), s2)
     return head(s1) + Difference(x, tail(s1), s2)
end Set

1-3-3

ADT Bag is objects:
a subrange of the integers starting at (INT_MIN) and ending at the
maximum integer (INT_MAX) on the computer functions: for
all x, y ∈ Bag; TRUE, FALSE ∈ Boolean and the Boolean operations defined in Problem 4 are available (not, and, or,...)
and where ==, Ø, +, head(s), tail(s) are the usual Bag operations,
where == return TRUE if tw set elements are the same, and TRUE otherwise.
Ø is the empty Bag.
+ adds and element to a Bag.
head(s) extracts the first member in the Bag.
tail(s) extracts a list of all other elements in the Bag. An empty bag contains no tail. A bag with only one element has the emtpy bag has it tail.

Bag Create(b)	::= Ø
Boolean IsEmpty(b)	::= if (b ==Ø ) return TRUE
     return FALSE
Boolean IsIn(x, b)	::= if (IsEmpty(b)) return FALSE
     if (x == head(b) return TRUE
    return IsIn(x, Tail(b))
Bag Insert(x,s)	::= if (IsEmpty(b)) return b
    return x + b
Bag Remove(x, s)	::= if (IsEmpty(b)) return b
      if (x == head(b)) return tail(b)
     return Remove(x, tail(b))
end bag

1-3-4

ADT Boolean is objects:
TRUE, FALSE ∈ Boolean and the Boolean== the usual boolean operation.
where == return TRUE if tw set elements are the same, and TRUE otherwise.
Boolean not(x)	::= if (x) return TRUE
   return FALSE
Boolean and(x,y)	::= if(not(x)) return FALSE
    if (not(y)) return FALSE
    return TRUE
Boolean or(x, s)	::= if(x) return TRUE
    if (y) return TRUE
    return FALSE
Boolean xor(x, s)	
::= if(and(not(x), not(y))) return FALSE
    if (and(x, y)) return FALSE
    return TRUE

Boolean implies(x, s)	::= if (and(x, y)) return TRUE
    if (and(not(x),not(y))) return TRUE
    return FALSE
Boolean equivalent(x, s)	::= if(and(not(x), not(y))) return TRUE
    if (and(x, y)) return TRUE
    return FALSE
end Set