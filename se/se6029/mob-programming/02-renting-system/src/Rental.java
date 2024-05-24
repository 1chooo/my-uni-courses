import MovieTypes.MovieType;

public class Rental {

    private Customer customer;
    private Movie movie;
    private int rentedDays;

    private MovieType movieType;
    private float cost,   // price may change via time, but cost not
                  points;

    public Rental(Movie movie, Customer customer, int rentedDays) {

        this.customer = customer;
        this.movie = movie;
        this.rentedDays = rentedDays;

        movieType = movie.getMovieType();
        cost = movieType.getPrice(this.rentedDays);
        points = movieType.getMemberPoint();
    }

    public String getMovieName() {
        return movie.getName();
    }

    public float getCost() {
        return cost;
    }

    public float getPoints() {
        return points;
    }
}
