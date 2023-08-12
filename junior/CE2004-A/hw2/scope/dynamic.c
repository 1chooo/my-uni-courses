// Since dynamic scoping is very uncommon in
// the familiar languages, we consider the
// following pseudo code as our example. It
// prints 20 in a language that uses dynamic
// scoping.

int x = 10;

// Called by g()
int f()
{
return x;
}

// g() has its own variable
// named as x and calls f()
int g()
{
int x = 20;
return f();
}

main()
{
printf(g());
}
