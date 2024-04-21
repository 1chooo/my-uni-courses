# Material 07 Lab - Database Design and Normalization <!-- omit in toc -->

## Course 

### Lab 01

資料庫的 foreign key 是什麼意思?

> **My Answer:**
>
> 用來關聯其他 Table 的 key。某個欄位識別的欄位的 Primary Key。

### Lab 02

什麼是正規化 (Normalization) ?  請用一句話解釋。

> **My Answer:**
>
> 是把 database 結構化的過程，以達到要擴充只要改一個地方就好，底層不用動

把一堆資料彼此的相依性，欄位隸屬於哪個 Table 的過程就是正規化。

### Lab 03

請問在資料庫的實作中，如果沒有正規劃好，通常系統會有什麼問題?

> **My Answer:**
>
> 我們要 query 的時候，要撰寫很多的程式邏輯，才有辦法得到我們要的內容，另外要新增內容的時候，也會被原先的設計限制。

### Lab 04

正規化的 NF (Normal Form) 是一種非常精準的數學定義，放諸四海皆標準嗎?  是或不是?  如果不是為何? 請說明。

> **My Answer:**
>
> 不是，未必皆標準。
> 
> 因為在不同的生活經驗有可能會有不同的經驗，就如同老師上課的範例，如果今天銷售對應的從原本的顧客，變成訂單編號，那資料庫的 Table 設計就合理了！因此 Normal Form 的標準應該是能夠針對 Case 去做應應設計。

### Lab 07

Normalization 的結果越高，
- (A) 通常有什麼好處?
- (B) 通常有什麼壞處?

> **My Answer:**
> - (A) 好處是我們可以在未來的改動中，固定我們的底層邏輯，同時也可以避免掉需要撰寫大量程式邏輯來取用 DataBase 的內容。
> - (B) 在設計的時候需要耗費大量的開發成本。

- 任何的 query 都可以在 Table 之間用 Database 的關聯性來取得，而不需要撰寫大量的程式邏輯。
- 在查詢簡單的問題的時候，可能本來很相近的資料，因為設計的考量會被拆成兩個 Table，這樣就會變得很複雜。效率會變差

### Lab 08

DataBase 的 JOIN operation 是怎麼一回事? 請用你自己的文字來解釋。

> **My Answer:**
>
> 當我們今天要透過 foriegn key 去關聯其他 Table 的資訊的時候，我們可以用 Join 來實現。



## Take Home


### Homework - Lab 05 (三倍)

請打開投影片的最後一頁，並且完成該作業。我會在現場當個誠實又精準的客戶回答你的問題。

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

輪胎供應商管理系統

各種供應商

輪胎店

比如從米其林輪胎進口，有各種不同的規格跟標價，有些輪胎會在南港輪胎有個倉庫，也有些輪胎會在鎮馨輪胎會有倉庫。


Only for 大盤商要用的系統
1. 老師是大盤商，從國外進口輪胎，有各種不同的規格跟標價。輪胎就直接到供應商了！
   - 會知道輪胎在哪個倉庫，在哪個輪胎供應商，賣給哪個車行。
2. 會把輪胎給輪胎供應商，輪胎供應商會有自己的倉庫。
   - 有些輪胎會在南港輪胎、正新輪胎供應商，供應商有自己的倉庫。
3. 供應商的目的是要把輪胎賣給路邊的車行。


### Homework - Lab 06

當你完成投影片最後一頁的作業。請把你完成的 DB table 改寫成物件導向的 class。


### Homework - Lab 09

有一個老師，要出許多作業給學生，但是每個學生在每一次的作業要做的內容都不太一樣。如範例顯示，

學生 Jeff Smith 第一次作業做的是 Article Summary，第二次作業做的是 Poetry analysis。但是 Nancy Jones 第一次作業做的是 Article Summary，第二次作業做的是 Reaction Paper。

這位老師想要用個 DBMS 來管理這些作業。請幫這位老師正規化一下

| Name | Assignment 1 | Assignment 2 |
| ---- | ------------ | ------------ |
| Jeff Smith | Article Summary | Poetry analysis |
| Nancy Jones | Article Summary | Reaction Paper |
| Jane Scott | Article Summary | Poetry analysis |


### Homework - Lab 10

下面的例子，是一個未經正規化的表格。請先用你的 common sense 來理解裡面的名詞。

- A. (Insert Anomaly ) 請問我如果要新增一個 office number 到這個表格的時候，我會遇到什麼問題?
- B. (Deletion Anomaly) 請問如果 John Hunt 退休，我會遇到什麼問題
- C. 請把他正規化，解決上述的問題

**SalesStaff**
| EmployeeID | SalesPerson | SalesOffice | OfficeNumber | Customer1 | Customer2 | Customer3 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1003 | Mary Smith | Chicago | 312-555-1212 | Ford | GM |  |
| 1004 | John Hunt | New York | 212-555-1212 | Dell | HP | Apple |
| 1005 | Martin Hap | Chicago | 312-555-1212 | Boeing |  |  |

### Homework - Lab 11

以下是一個 `customer` 的class。常見學生以下的寫法

```cpp
Class Customer {
   int id ;
   string address ;
   int ProductID[100] ;  // 購買產品的 ID
   int ProductCompanyID[100]; // 購買產品所屬的公司 ID
   bool used[100] ; // 註記這個陣列的的元素是否已經被用來儲存
}
```


- A. 請先批評一番。
- B. 然後請改寫。






