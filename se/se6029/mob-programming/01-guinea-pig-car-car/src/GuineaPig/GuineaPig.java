// GuineaPig/GuineaPig.java

package GuineaPig;

public class GuineaPig {
    protected String name;
    protected int foodCount;

    public GuineaPig() {
        this("GuineaPig");
    }

    public GuineaPig(String name) {
        this.name = name;
        this.foodCount = 0;
    }

    public void noise() {
        System.out.println(this.name + "PuiPui.");
    }

    public void eat(String food) {
        System.out.println(this.name + " eat " + food);
    }

    public void pupu() {
        System.out.println(this.name + " pupu.");
        this.foodCount = 0;
    }

    public String getName() {
        return this.name;
    }
}
