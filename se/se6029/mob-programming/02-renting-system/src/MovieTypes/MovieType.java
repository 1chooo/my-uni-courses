package MovieTypes;

public class MovieType {
    protected float price, memberPoint, delayedPrice;
    protected int defaultRentedDay;

    public MovieType() {
    }

    public float getPrice(int day) {
        float totalPrice = price;
        
		if (day > defaultRentedDay) {
			day -= defaultRentedDay;
			totalPrice += delayedPrice * day;
		}
		return totalPrice;
    }

    public float getMemberPoint() {
        return memberPoint;
    }
}
