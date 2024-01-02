# 06. SQL Injection 1


## Try SQL Injection


"’ OR ‘’=‘’-- "

### 1. `ERR_CACHE_MISS` [^1]

username = `' or '1'='1`
password = `' or '1'='1`

```SQL
SELECT * FROM Users 
WHERE Name = '' or '1'='1' 
AND Pass = '' or '1'='1'
```

username = `hi' or 1=1--`
password = `hi' or 1=1--`


### Source Code Analysis

```php
<?php
isset($_GET['source']) and die(show_source(__FILE__, true));
?>

<?php
$host = 'isostagram_db';
$dbuser = 'MYSQL_USER';
$dbpassword = 'MYSQL_PASSWORD';
$dbname = 'ctf_users';
$link = mysqli_connect($host, $dbuser, $dbpassword, $dbname);

$loginStatus = NULL;
$username = $_POST['username'];
$password = $_POST['password'];

if (isset($username) && isset($password)) {
    error_log('POST: [' . $username . '] [' . $password . ']');
    if ($link) {
        $blacklist = array("ununionion", "union", "selselectect", "select", "where", "and", "or");
        $replace = array("", "", "", "", "","","");
        $username = str_ireplace($blacklist, $replace, $username);
        $password = str_ireplace($blacklist, $replace, $password);
        $sql = "SELECT * FROM users WHERE `username` = '$username' AND `password` = '$password';";
        $query = mysqli_query($link, $sql);
        @$fetchs = mysqli_fetch_all($query, MYSQLI_ASSOC);
        if (@count($fetchs) > 0) {
            foreach ($fetchs as $fetch) {
                if ($fetch["username"] === 'idtjohn88' && $fetch["password"] === $password) {
                    $loginStatus = True;
                    break;
                }
                $loginStatus = False;
            }
        } else {
            $loginStatus = False;
        }
    } else {
        $loginStatus = NULL;
    }
} else {
    $loginStatus = NULL;
}
?>
```

這段 PHP 代碼看起來是用於連接到一個名為 `ctf_users` 的資料庫並進行用戶身份驗證。讓我們逐步解釋其中的各個部分：

1. `isset($_GET['source']) and die(show_source(__FILE__, true));`
   - 這一行代碼檢查是否存在名為 `source` 的 GET 參數。如果存在，則使用 `show_source()` 函數以純文本形式顯示當前文件的內容。這可以用於顯示代碼的原始碼，通常用於除錯或測試目的。 

2. 連接到資料庫：
   ```php
   $host = 'isostagram_db';
   $dbuser = 'MYSQL_USER';
   $dbpassword = 'MYSQL_PASSWORD';
   $dbname = 'ctf_users';
   $link = mysqli_connect($host, $dbuser, $dbpassword, $dbname);
   ```
   - 定義了資料庫的連接信息，包括主機名 (`$host`)、用戶名 (`$dbuser`)、密碼 (`$dbpassword`) 和資料庫名 (`$dbname`)。
   - 使用 `mysqli_connect()` 函數嘗試建立與資料庫的連接，將連接結果存儲在 `$link` 變數中。

3. 從 POST 請求中獲取用戶名和密碼：
   ```php
   $username = $_POST['username'];
   $password = $_POST['password'];
   ```
   - 從 `$_POST` 中獲取用戶提交的用戶名和密碼，這意味著這段代碼期望這些資訊是通過 POST 方法提交的表單來進行處理的。

4. 用戶身份驗證：
   ```php
   if (isset($username) && isset($password)) {
       // ... 以下為用戶身份驗證的代碼 ...
   } else {
       $loginStatus = NULL;
   }
   ```
   - 在確保接收到用戶名和密碼之後，代碼開始進行用戶身份驗證的過程。

5. 用戶輸入的資料過濾：
   ```php
   $blacklist = array("ununionion", "union", "selselectect", "select", "where", "and", "or");
   $replace = array("", "", "", "", "","","");
   $username = str_ireplace($blacklist, $replace, $username);
   $password = str_ireplace($blacklist, $replace, $password);
   ```
   - 這裡使用 `str_ireplace()` 函數來檢查用戶輸入的用戶名和密碼中是否包含某些 SQL 關鍵字（如 `union`、`select` 等），並將它們替換為空字符串。

6. 執行 SQL 查詢：
   ```php
   $sql = "SELECT * FROM users WHERE `username` = '$username' AND `password` = '$password';";
   $query = mysqli_query($link, $sql);
   @$fetchs = mysqli_fetch_all($query, MYSQLI_ASSOC);
   ```
   - 創建一個 SQL 查詢，通過用戶名和密碼來選擇 `users` 表中的數據。
   - 使用 `mysqli_query()` 函數向資料庫發送 SQL 查詢。
   - 使用 `mysqli_fetch_all()` 函數來獲取查詢結果中的所有行，以關聯數組的形式存儲在 `$fetchs` 變數中。

7. 檢查用戶是否通過驗證：
   ```php
   if (@count($fetchs) > 0) {
       // ... 以下為進一步的驗證過程 ...
   } else {
       $loginStatus = False;
   }
   ```
   - 如果查詢結果行數大於 0，表示有用戶記錄匹配輸入的用戶名和密碼，代碼會進一步檢查這些記錄以確定用戶身份。

8. 最後，根據驗證結果設置 `$loginStatus` 變數，用於表示用戶的登錄狀態。

需要注意的是，這段代碼存在一些潛在的安全風險，例如直接將用戶輸入的數據插入 SQL 查詢中，容易受到 SQL 注入攻擊。最好使用 prepared statements 或其他方法來避免這種風險。

```php
if (@count($fetchs) > 0) {
    foreach ($fetchs as $fetch) {
        if ($fetch["username"] === 'idtjohn88' && $fetch["password"] === $password) {
            $loginStatus = True;
            break;
        }
        $loginStatus = False;
    }
} else {
    $loginStatus = False;
}
```

這段程式碼主要是用於檢查從資料庫檢索出來的用戶資料是否符合預期的條件，並最終設置 `$loginStatus` 變數以表示用戶的登錄狀態。

讓我們一步步解釋這段程式碼的運行：

1. `if (@count($fetchs) > 0) { ... } else { ... }`
   - 此條件語句檢查 `$fetchs` 陣列中是否有資料。如果 `$fetchs` 中有資料（`count($fetchs)` 大於 0），代表從資料庫中找到了符合條件的用戶記錄。

2. `foreach ($fetchs as $fetch) { ... }`
   - 在找到符合條件的用戶記錄時，程式碼使用 `foreach` 迴圈遍歷 `$fetchs` 中的每一條記錄。

3. `if ($fetch["username"] === 'idtjohn88' && $fetch["password"] === $password) { ... }`
   - 在迴圈中，程式碼檢查每條記錄的 `username` 和 `password` 是否與預期的值匹配。
   - 如果 `username` 是 'idtjohn88' 而且 `password` 與從 POST 請求中接收到的密碼相符，代表找到了目標用戶的資料，程式碼將 `$loginStatus` 設置為 `True`，表示成功登錄。

4. `else { $loginStatus = False; }`
   - 如果在迴圈中沒有找到符合條件的用戶記錄，則將 `$loginStatus` 設置為 `False`，表示登錄失敗。

需要注意的是，當 `username` 是 'idtjohn88' 且 `password` 符合 POST 請求中接收到的密碼時，`$loginStatus` 會被設置為 `True`。然而，這段程式碼中存在一些潛在的問題，例如直接比較密碼是否相符，這可能暴露密碼在資料庫中的存儲方式。安全最佳實踐應該是對密碼採取安全的儲存和比較方法，例如使用哈希函數來儲存密碼並進行比較。此外，這段程式碼也應該避免直接將用戶輸入的資料插入 SQL 查詢中，以防止 SQL 注入攻擊。


[^1]: https://ithelp.ithome.com.tw/articles/10323634?sc=rss.iron