import MovieTypes.MovieType;

public class Movie {
    private MovieType movieType;
    private String name;

    public Movie(String name, MovieType movieType) {
        this.name = name;
        this.movieType = movieType;
    }

    public String getName() {
        return name;
    }

    public void setMovieType(MovieType newMovieType) {
        this.movieType = newMovieType;
    }

    public MovieType getMovieType() {
        return movieType;
    }
}
