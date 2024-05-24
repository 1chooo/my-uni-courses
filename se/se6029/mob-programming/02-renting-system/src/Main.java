import MovieTypes.MovieType;
import MovieTypes.NewRelease;
import MovieTypes.Regular;

import java.util.HashMap;
import java.util.Map;

import MovieTypes.Children;

public class Main {
    // Array to store movies & customer
    static Map<String, Movie> movies = new HashMap<String, Movie>();
    static Map<String, Customer> customers = new HashMap<String, Customer>();

    static final MovieType
        NEW_RELEASE = new NewRelease(),
        REGULAR = new Regular(),
        CHILDREN = new Children();

    public static void main(String[] args) {
        
        movies.put("我的名字", new Movie("我的名字", NEW_RELEASE));
        movies.put("K-O", new Movie("K-O", REGULAR));
        movies.put("涼宮春日的", new Movie("涼宮春日的", REGULAR));
        movies.put("GIVEN", new Movie("GIVEN", CHILDREN));


        String[] names = new String[] {
                "倫倫", "六花醬", "K昂", "史家瑩"
        };
        for(String s: names) {
            customers.put(s, new Customer(s));
        }

        // Customer rent Movie

        // 倫倫: GIVEN/8天
        customers.get("倫倫").rent(movies.get("GIVEN"), 8);
        // 倫倫: 我的名字/7天
        customers.get("倫倫").rent(movies.get("我的名字"), 7);
        // 六花醬: 我的名字/8天
        customers.get("六花醬").rent(movies.get("我的名字"), 8);
        // 六花醬: K-O/7天
        customers.get("六花醬").rent(movies.get("K-O"), 7);
        // 六花醬: 涼宮春日的/8天
        customers.get("六花醬").rent(movies.get("涼宮春日的"), 8);
        // K昂: K-O/7天
        customers.get("K昂").rent(movies.get("K-O"), 7);
        // 史家瑩: GIVEN/8天
        customers.get("史家瑩").rent(movies.get("GIVEN"), 8);

        // print member point & spend of the customers
        for(String s : names) {
            customers.get(s).statement();
            System.out.println();
        }


        // Pretend pass two months
        movies.get("我的名字").setMovieType(REGULAR);

    }
}
