package lab03;

public class X {
    public static void main(String[] args) {
        X x = new X();
        Y y = new Y();
        x.doSomething();
        y.doSomething();
    }

    public void doSomething() {
        this.print();
    }

    public void print() {
        System.out.println("XXX");
    }
}

class Y extends X {
    @Override
    public void print() {
        System.out.println("YYY");
    }
}
