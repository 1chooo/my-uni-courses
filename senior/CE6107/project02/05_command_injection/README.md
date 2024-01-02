# 05. Command Injection

```php
<?php if (isset($_POST['json'])) : ?>
    <section class="has-text-left">
        <p>Result:</p>
        <pre><?php
        $blacklist = ['|', '&', ';', "\n", '?', '*', '$', 'cat', 'flag'];
        $is_input_safe = true;
        foreach ($blacklist as $bad_word)
            if (strstr($_POST['json'], $bad_word) !== false) $is_input_safe = false;

        if ($is_input_safe)
            system("echo '" . $_POST['json'] . "'| jq .bocchi");
        else
            echo '<img src="nanana.gif"/>';
        ?></pre>
    </section>
<?php endif; ?>
```

這段 PHP 代碼的主要功能是處理來自表單 POST 請求的資料，並對資料進行安全性檢查和處理。

1. **條件檢查：**
   這段代碼開始於 `<?php if (isset($_POST['json'])) : ?>`，它首先檢查是否有名為 'json' 的資料以 POST 方式提交到這個網頁。

2. **顯示結果區域：**
   如果有 'json' 資料提交，就會進入下一個部分，其中包含了以下內容：

   - **設置黑名單：**
     ```php
     $blacklist = ['|', '&', ';', "\n", '?', '*', '$', 'cat', 'flag'];
     ```
     這行程式碼定義了一個 `$blacklist` 陣列，其中包含了一些可能會被用來試圖操縱系統的特殊字符或字串，例如命令注入字符 (`|`, `&`, `;` 等) 和特定字詞 (`cat`, `flag` 等)。

   - **安全性檢查：**
     ```php
     $is_input_safe = true;
     foreach ($blacklist as $bad_word) {
         if (strstr($_POST['json'], $bad_word) !== false) {
             $is_input_safe = false;
         }
     }
     ```
     使用 `foreach` 迴圈遍歷黑名單，檢查提交的 'json' 資料是否包含黑名單中的任何字符或字串。如果發現任何不安全的字詞，則會將 `$is_input_safe` 設置為 `false`。

   - **安全性處理和輸出：**
     ```php
     if ($is_input_safe) {
         system("echo '" . $_POST['json'] . "'| jq .bocchi");
     } else {
         echo '<img src="nanana.gif"/>';
     }
     ```
     如果提交的 'json' 資料通過安全性檢查 (`$is_input_safe` 是 `true`)，則會執行一個系統命令使用 `system()`。這個命令使用 'jq' 工具（一個命令行下的 JSON 處理器）從提交的 JSON 資料中提取 'bocchi' 鍵的值，並在 `<pre>` 標籤中顯示它。

   - **處理不安全的輸入：**
     如果輸入被判定為不安全（包含黑名單中的內容），則會顯示一張圖片 (`nanana.gif`)，以預防性方式取代執行 'jq' 命令，這樣做可以防止處理不安全的輸入可能帶來的安全風險。


在命令注入（Command Injection）中，反引号（`` ` ``）或反撇号（`'`）通常用于执行 shell 命令的语法。这种语法允许将命令的输出嵌入到另一个命令中，或者在某些上下文中执行任意的操作系统命令。

在许多命令行环境中，反引号用于执行命令并返回结果。例如，在类Unix系统的shell中，你可以使用反引号来执行命令，如：

```bash
output=`ls -l`
```

在这个例子中，`ls -l` 命令的输出将被存储在 `output` 变量中。

在命令注入漏洞中，如果应用程序使用用户提供的输入并直接将其传递到命令解释器而没有适当的验证或过滤，攻击者可以插入恶意命令并执行。例如，假设一个应用程序使用了类似以下的代码：

```python
command = 'ping ' + user_input  # 潜在的命令注入漏洞
os.system(command)
```

如果 `user_input` 被恶意构造为 `'127.0.0.1; rm -rf /'`，那么由于缺乏适当的输入验证和过滤，`os.system` 将执行以下命令：

```bash
ping 127.0.0.1; rm -rf /
```

这将执行 `ping` 命令并立即删除文件系统上的所有内容（`rm -rf /` 是一个危险的命令，会删除整个文件系统）。

因此，反引号（`` ` ``）或反撇号（`'`）在命令注入中可能被利用来嵌入恶意命令，从而以应用程序的权限在系统上执行各种危险操作。防止命令注入的一种方法是始终对用户输入进行适当的验证、转义或过滤，以确保输入不会被误解为命令执行。

## Keyword繞過 [^1]

- String Concat
    - `A=fl;B=ag;cat $A$B`
- Empty Variable
    - `cat fl${x}ag`
    - `cat tes$(z)t/flag`
    
- Environment Variable
    - `$PATH => "/usr/local/….blablabla”`
        - `${PATH:0:1}   => '/'`
        - `${PATH:1:1}   => 'u'`
        - `${PATH:0:4}   => '/usr'`
    - `${PS2}` 
        - `>`
    - `${PS4}`
        - `+`
- Empty String
    - `cat fl""ag`
    - `cat fl''ag`
        - `cat "fl""ag"`

- 反斜線
    - `c\at fl\ag`


[^1]: [Command Injection#keyword 繞過](https://github.com/w181496/Web-CTF-Cheatsheet?tab=readme-ov-file#command-injection)

