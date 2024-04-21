# Material 07 - Database Design and Normalization <!-- omit in toc -->

## Normalization

What Normalization is for?

> [!NOTE]
> is to make sure that each database table carries only the attributes that actually describe What is needed.

### Definition

Normalization is the process of structuring relational database schema such that most ambiguity is removed. The stages of normalization are referred to as normal forms and progress from the least restrictive (First Normal Form) through the most restrictive (Fifth Normal Form). Generally, most database designers do not attempt to implement anything higher than Third Normal Form or Boyce-Codd Normal Form. 

#### A simpler explanation to normalization

There are two goals of the normalization process:
- eliminate redundant data (for example, storing the same data in more than one table) and 
- ensure data dependencies make sense (only storing related data in a table). Both of these are worthy goals as they reduce the amount of space a database consumes and ensure that data is logically stored.

### Normal forms

- The database community has developed a series of guidelines for ensuring that databases are normalized. These are referred to as normal forms and are numbered from one (the lowest form of normalization, referred to as first normal form or 1NF) through five (fifth normal form or 5NF).
- In practical applications, you'll often see 1NF, 2NF, and 3NF along with the occasional 4NF. Fifth normal form is very rarely seen and won't be discussed in this article.

#### First normal form (1NF) sets the very basic rules for an organized database:

- Eliminate duplicative columns from the same table. 
- Create separate tables for each group of related data and identify each row with a unique column or set of columns (the primary key). 

#### Second normal form (2NF) further addresses the concept of removing duplicative data

- Meet all the requirements of the first normal form. 
- Remove subsets of data that apply to multiple rows of a table and place them in separate tables. 
- Create relationships between these new tables and their predecessors through the use of foreign keys. 

#### Third normal form (3NF) goes one large step further

- Meet all the requirements of the second normal form. 
- Remove columns that are not dependent upon the primary key. 

#### Finally, fourth normal form (4NF) has one additional requirement

- Meet all the requirements of the third normal form. 
- A relation is in 4NF if it has no multi-valued dependencies. 

### An classic example

- a table within a human resources database that stores the manager-subordinate relationship.
- For the purposes of our example, we'll impose the business rule that each manager may have one or more subordinates while each subordinate may have only one manager. 

#### An intuitive table

| Manager | Subordinate1 | Subordinate2 | Subordinate3 | Subordinate4 |
|---------|--------------|--------------|--------------|--------------|
| Bob     | Jim          | Mary         | Beth         |              |
| Mary    | Mike         | Jason        | Carol        | Mark         |
| Jim     | Alan         |              |              |              |

```cpp
class ManagerRelation {
    string manager;
    string sub[255];
};

main() {
    sub[0] = "beth";
    sub[1] = "mary";
}
```

Why it is not even 1st NF?

- recall the first rule imposed by 1NF: eliminate duplicative columns from the same table.? Clearly, the Subordinate1-Subordinate4 columns are duplicative.
- Jim only has one subordinate, the Subordinate2-Subordinate4 columns are simply wasted storage space 
- Furthermore, Mary already has 4 subordinates ?what happens if she takes on another employee?  The whole table structure would require modification. 

#### A second bright idea

Let's try something like this: 

| Manager | Subordinates |
|---------|--------------|
| Bob     | Jim, Mary, Beth |
| Mary    | Mike, Jason, Carol, Mark |
| Jim     | Alan |

```cpp
class MangemantRelation {
    string manager;
    string subordinates;
};
```

- Manager Subordinates Bob Jim, Mary, Beth Mary Mike, Jason, Carol, Mark Jim Alan This solution is closer, but it also falls short of the mark
- The subordinates column is still duplicative and non-atomic. What happens when we need to add or remove a subordinate?? We need to read and write the entire contents of the table.? That not a big deal in this situation, but what if one manager had one hundred employees??Also, it complicates the process of selecting data from the database in future queries. 

#### Here is a table that satisfies the first rule of 1NF: 

| Manager | Subordinate |
|---------|-------------|
| Bob     | Jim         |
| Bob     | Mary        |
| Bob     | Beth        |
| Mary    | Mike        |
| Mary    | Jason       |
| Mary    | Carol       |
| Mary    | Mark        |
| Jim     | Alan        |

#### Not finished yet

- Now, what about the second rule: identify each row with a unique column or set of columns (the primary key)
- You might take a look at the table above and suggest the use of the subordinate column as a primary key. In fact, the subordinate column is a good candidate for a primary key due to the fact that our business rules specified that each subordinate may have only one manager.
- However, the data that we have chosen to store in our table makes this a less than ideal solution.? What happens if we hire another employee named Jim?  How do we store his manager-subordinate relationship in the database?? 

#### Finally, the 1st normal form

| Manager | Subordinate |
|---------|-------------|
| 182     | 143         |
| 182     | 201         |
| 182     | 123         |
| 201     | 156         |
| 201     | 041         |
| 201     | 187         |
| 201     | 196         |
| 143     | 202         |

```sql
table person
id name
182 Bob
201 Mary
```

### Towards to 2NF

#### Definition

In order to be in Second Normal Form, a relation In order to be in Second Normal Form, a relation must first fulfill the requirements to be in First Normal Form In order to be in Second Normal Form, a relation must first fulfill the requirements to be in First Normal Form. Additionally, each nonkey attribute In order to be in Second Normal Form, a relation must first fulfill the requirements to be in First Normal Form. Additionally, each nonkey attribute in the relation must be functionally dependent upon the primary key. 

#### An Example

The relation is in First Normal Form, but not Second Normal Form: 

| Order # | Customer | Contact Person | Total |
|---------|----------|----------------|-------|
| 1       | Acme Widgets | John Doe | $134.23 |
| 2       | ABC Corporation | Fred Flintstone | $521.24 |
| 3       | Acme Widgets | John Doe | $1042.42 |
| 4       | Acme Widgets | John Doe | $928.53 |

```cpp
class order {
    int orderNo;
    Customer* customer;
    Person* contactPerson;
    int salePrice;
}

main() {
    Vector<Order *> allSalse;

    Order *o1 = new Order(1, "Acme Widgets", "John Doe", 134.23);
    allSalse.push(o1);

    Order *o2 = new Order(2, "ABC Corporation", "Fred Flintstone", 521.24);
    allSalse.push(o2);

    size of allSalse 1000000

    loop for all o which customer is "Acme Widgets"
    replace o.contactPerson.
}
```

> [!TIP]
> Remove subsets of data that apply to multiple rows of a table and place them in separate tables

#### Two tables to satisfy 2NF

**CustomerSalesRelation Table**

| Customer | Contact Person |
|----------|----------------|
| Acme Widgets | John Doe |
| ABC Corporation | Fred Flintstone |

**Order Table**

| Order # | Customer | Total |
|---------|----------|-------|
| 1       | Acme Widgets | $134.23 |
| 2       | ABC Corporation | $521.24 |
| 3       | Acme Widgets | $1042.42 |
| 4       | Acme Widgets | $928.53 |

- Customer: As a foriegn key to the Order table

```cpp
class CustomerContactRelation {
    Customer* customer;
    person* contactPerson;
}

main() {
    Vector<Order *> allSalse;

    Order *o1 = new Order(1, "Acme Widgets", 134.23);
    allSalse.push(o1);

    Order *o2 = new Order(2, "ABC Corporation", 521.24);
    allSalse.push(o2);

    size of allSalse 1000000

    Order o;
    Vector<CustomerContactRelation *>

    o.getCustomer();
}
```

> [!NOTE]
> - 如果今天在別的國度 Sales Person 是負責訂單，那目前的 Table 就對了，但是我們今天要討論的是 Sales Person 是負責 Custom 的，因此這樣的設計是不合規的。
> - DB 會 JOIN 但是 Objected-Oriented 不會

#### Comment
- The creation of two separate tables eliminates the dependency problem experienced in the previous case. 
- In the first table, contact person is dependent upon the primary key -- customer name.The second table only includes the information unique to each order.
- Someone interested in the contact person for each order could obtain this information by performing a `JOIN` operation 


### Towards to 3NF

#### Definition

In order to be in Third Normal Form, a relation In order to be in Third Normal Form, a relation must first fulfill the requirements to be in Second Normal Form In order to be in Third Normal Form, a relation must first fulfill the requirements to be in Second Normal Form.?Additionally, Every non-prime attribute of R is non-transitively dependent (i.e. directly dependent) on every candidate key of R.

> [!NOTE]
> A short explanation: No Dependencies on Non-Key Attributes

- In the relational modelIn the relational model of databases, a candidate key of a relation of a relation is a minimal superkey of a relation is a minimal superkey for that relation; that is, a set of attributes such that
- the relation does not have two distinct tuples (i.e. rows or records in common database language) with the same values for these attributes (which means that the set of attributes is a superkey)
- there is no proper subset of these attributes for which (1) holds (which means that the set is minimal).
- The constituent attributes are called prime attributes. Conversely, an attribute that does not occur in ANY candidate key is called a non-prime attribute.

#### An Example

| Company | City | State | ZIP |
|---------|------|-------|-----|
| Acme Widgets | New York | NY | 10169 |
| ABC Corporation | Miami | FL | 33196 |
| XYZ, Inc. | Columbia | MD | 21046 |

In this example, the city and state are dependent upon the ZIP code.?To place this table in 3NF, two separate tables would be created -- one containing the company name and ZIP code and the other containing city, state, ZIP code pairings.

#### To go or not to go higher?

- This may seem overly complex for daily applications and indeed it may be. Database designers should always keep in mind the tradeoffs between higher level normal forms and the resource issues that complexity creates. 
- For example, in the last slide, if the city name and state name shall never change in 1000 years, the only harm is the duplication of data. The impact of change is of 0 possibility. 







## Exercise

(20 marks) 假設你負責分析一個系統，此系統的資料包含了下面許多欄位  
Please analyze a system which contains the following attributes

```
S#:     零件供應商的編號 (Supplier no)
SNAME:  零件供應商的姓名 (supplier name)
CITY1   零件供應商的城市 (The city of a supplier) 
P#      零件編號  (part no.)
PNAME	零件名稱 (part name)
COLOR   零件色彩 (part color)
WEIGHT  零件重量  (part weight)
CITY2   零件所儲存的城市 (city where the parts are stored)
QTY     零件的存量 (The quantity of the parts)
```

In your analysis, you found that a part can be supplied by several suppliers. Please determine how many tables should be used and what is the content of each table.  
在你分析的過程中，你發現一個零件可能有多個供應商可以供應。請簡單說明這樣一個資料庫系統，你要用幾個表格，每個表格的屬性又為何？


零件是輪胎
Suppliers
| S# | SNAME | CITY1|

Parts
| P# | PNAME | COLOR | WEIGHT | CITY2 | QTY |

Parts_Suppliers
| P# | S# | QTY |