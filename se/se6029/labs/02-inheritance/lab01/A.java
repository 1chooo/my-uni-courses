package lab01;

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


/*
 * Output:
 * foo from B
 * bar from C
 */
