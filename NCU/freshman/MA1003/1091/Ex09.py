a , b = eval(input( " > "))
ans = 0
for i in range( a , b + 1 ) :
    
    ans += i
    
print( a, "+" , a + 1 , "+" , "..." , "+" , b , "=" , ans )