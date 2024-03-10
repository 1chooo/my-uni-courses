# Material 02 - Inheritance

### Lab 01

求下列 JAVA 程式的執行結果。

```java
public class A {

   public static void main(String[] args) {
       C c = new C();
       c.foo();
       c.bar();
   }

   public void foo() {
       System.out.println("foo from A");
   }

   public void bar() {
       System.out.println("bar from A");
   }
}

class B extends A {
   @Override
   public void foo() {
       System.out.println("foo from B");
   }
}

class C extends B {
   @Override
   public void bar() {
       System.out.println("bar from C");
   }
}
```

### Lab 02


Fix the following program, and make it OO.

```java
import java.util.ArrayList;

public class EmployeeCensus extends ArrayList<Employee> {
   public void addEmployee(Employee employee) {
       add(employee);
   }

   public void removeEmployee(Employee employee) {
       remove(employee);
   }
}

class Employee {
   // not important
}
```

### Lab 03

求下列 JAVA 程式的執行結果。

```java
public class X {
   public static void main(String[] args) {
       X x = new X();
       Y y =new Y();
       x.doSomething();
       y.doSomething();
   }
   
   public void doSomething(){
       this.print();
   }
   
   public void print(){
       System.out.println("XXX");
   }
}

class Y extends X{
   @Override
   public void print(){
       System.out.println("YYY");
   }
}
```

### Lab 04


The following code is Java. There are some compilation errors in the code.
How can you fix it to pass compilation?
You can only change the code without deleting any lines of the code. 

```java
1. class SuperMan{
2.     private int a;
3.     protected SuperMan(int a){this.a = a;}
4. }
...
11. class SubMan extends SuperMan{
12.     public SubMan(int a){super(a);}
13.     public SubMan(){this.a = 5;}
14. }
```


### Lab 16

OK, 現在你應該知道繼承不能被濫用。你也知道以下的程式碼該怎麼改。  
不過其實一直還有一個更神秘的問題，那就是以下濫用繼承的程式碼為什麼不好，它會有什麼問題？也就是說，你可能以前繼承就是這樣寫，但是你好像也沒有發生過什麼問題不是嗎？

![](./imgs/lab16.png)

> [!TIP]
> (此題會深刻思考題，比重等同其他題目的3倍) 請仔細回答。




