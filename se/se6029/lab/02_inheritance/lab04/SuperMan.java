package lab04;

class SuperMan {
    @SuppressWarnings("unused")
    private int a;

    protected SuperMan(int a) {
        this.a = a;
    }
}

// ...

class SubMan extends SuperMan {
    public SubMan(int a) {
        super(a);
    }

    public SubMan() {
        // this.a = 5;
        super(5);
    }
}