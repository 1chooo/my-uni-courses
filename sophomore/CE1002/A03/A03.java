import java.util.Vector;

class Book {
  public String name;
  public String ISBN;
  public Vector<String> content;

  public Book(String name, String ISBN, Vector<String> content) {
    this.name = name;
    this.ISBN = ISBN;
    this.content = content;
  }

  public String getName() {
    return name;
  }
  public String getISBN() {
    return ISBN;
  }
  public String getContent(int PAGE) {
    if (PAGE >= content.size()) {
      return "Error";
    } else {
      return content.get(PAGE);
    }
  }
  public void addPage(String SENTENCE) {
    content.add(SENTENCE);
  }
}

class BookShelf {
  public Vector<Book> shelf = new Vector<>();

  public BookShelf() {}
  public void addBook(Book MYBook) {
    shelf.add(MYBook);
  }
  public void showBookShelf() {
    for (int i = 0; i < shelf.size(); i++) {
      System.out.println(i + " " + shelf.get(i).getName() + " " + shelf.get(i).getISBN());
    }
  }
}

public class A03 {
  //Book1 information
  static public String N1 = "book1";
  static public String iSBN1 = "978-3-14-131238-2";
  static public Vector<String> CONTENT1 = new Vector<>();

  //Book2 information
  static public String N2 = "book2";
  static public String iSBN2 = "278-33-4-133238-0";
  static public Vector<String> CONTENT2 = new Vector<>();

  public static void main(String[] args)
  {
    CONTENT1.add("book1p1");
    CONTENT1.add("book1p2");
    CONTENT1.add("book1p3");

    CONTENT2.add("book2p1");
    CONTENT2.add("book2p2");

    Book myBook1 = new Book(N1,iSBN1,CONTENT1);
    Book myBook2 = new Book(N2,iSBN2,CONTENT2);

    //Testing
    System.out.println(myBook1.getName()+" "+myBook1.getISBN());
    System.out.println(myBook2.getName()+" "+myBook2.getISBN());
    System.out.println(myBook1.getContent(0)+" "+myBook1.getContent(3));
    myBook1.addPage("book1p4");
    System.out.println(myBook1.getContent(0)+" "+myBook1.getContent(3));

    BookShelf myBookShelf = new BookShelf();
    myBookShelf.addBook(myBook1);
    myBookShelf.addBook(myBook1);
    myBookShelf.addBook(myBook2);
    myBookShelf.showBookShelf();
  }
}