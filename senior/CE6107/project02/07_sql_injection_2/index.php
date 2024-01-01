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
<!DOCTYPE html>
<html>
<!-- https://codepen.io/AliYmn/pen/zYYeaOJ -->
<!-- You can get source code at /?source -->

<head>
    <meta charset="utf-8" />
    <title>Isostagram</title>
    <link rel="shortcut icon" href="data:image/x-icon;," type="image/x-icon">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/rainbow.css" rel="stylesheet">
    <link href="css/ig.css" rel="stylesheet">
</head>

<body>
    <?php
    if ($loginStatus === True) {
    ?>
    <div class="text-center d-flex justify-content-start flex-column" style="height: 6vh">
        <br>
        <p class="rainbow" style="font-size: 3em;">
            <?php echo $_ENV["FLAG"], '<br>'; ?>
        </p>
    </div>
    <img src="img/kita.png" alt="kita" style="display:block; margin:auto;">
    <?php
    } else {
    ?>

    <body>
        <span id="root">
            <section class="section-all">
                <!-- 1-Role Main -->
                <main class="main" role="main">
                    <div class="wrapper">
                        <article class="article">
                            <div class="content">
                                <div class="phone-box">
                                    <img src="img/phone.png" alt="phone">
                                </div>
                            </div>
                            <div class="content">
                                <div class="login-box">
                                    <div class="header">
                                        <img class="logo" src="img/Isostagram.png" alt="Isostagram">
                                    </div><!-- Header end -->
                                    <div class="form-wrap">
                                        <form class="form" method="POST" action="/" id="form">
                                            <div class="input-box">
                                                <input type="text" id="name" aria-describedby=""
                                                    placeholder="電話番号、ユーザーネーム、メールアドレス" aria-required="true"
                                                    maxlength="70" autocapitalize="off" autocorrect="off"
                                                    name="username" value="" required>
                                            </div>
                                            <div class="input-box">
                                                <input type="password" name="password" id="password" placeholder="パスワード"
                                                    aria-describedby="" maxlength="70" aria-required="true"
                                                    autocapitalize="off" autocorrect="off" required>
                                            </div>
                                            <?php if ($loginStatus === False) { ?>
                                            <div style="margin: 0 40px; padding: 5px" class="alert alert-danger d-flex align-items-center">
                                                パスワードが間違っています。パスワードをご確認ください。
                                            </div>
                                            <?php } ?>
                                            <span class="button-box">
                                                <button class="btn" type="submit" name="submit">ログイン</button>
                                            </span>
                                            <a class="forgot" href="">パスワードを忘れた場合</a>
                                        </form>
                                    </div> <!-- Form-wrap end -->
                                </div> <!-- Login-box end -->
                                <div class="login-box">
                                    <p class="text" style="font-weight:bold">アカウントをお持ちでないですか？<a href="#">登録する</a></p>
                                </div> <!-- Signup-box end -->
                                <div class="app">
                                    <p>ダウンロード</p>
                                    <div class="app-img">
                                        <a target="_blank"
                                            href="https://play.google.com/store/apps/details?id=com.instagram.android">
                                            <img src="https://static.cdninstagram.com/rsrc.php/v3/yY/r/Wg4QXUge1nK.png">
                                        </a>
                                        <a target="_blank"
                                            href="ms-windows-store://pdp/?productid=9nblggh5l9xt&referrer=appbadge&source=www.instagram.com&mode=mini&pos=0%2C0%2C2560%2C1380">
                                            <img src="https://static.cdninstagram.com/rsrc.php/v3/y3/r/nHo7nDh0Dzp.png">
                                        </a>
                                    </div> <!-- App-img end-->
                                </div> <!-- App end -->
                            </div> <!-- Content end -->
                        </article>
                    </div> <!-- Wrapper end -->
                </main>
                <!-- 2-Role Footer -->
                <footer class="footer" role="contentinfo">
                    <div class="footer-container">
                        <nav class="footer-nav" role="navigation">
                            <ul>
                                <li><a href="https://adl.tw/">ADL</a></li>
                                <li><a href="">基本データ</a></li>
                                <li><a href="">ブログ</a></li>
                                <li><a href="">求人</a></li>
                                <li><a href="">ヘルプ</a></li>
                                <li><a href="">API</a></li>
                                <li><a href="">プライバシー</a></li>
                                <li><a href="">利用規約</a></li>
                                <li><a href="">人気アカウント</a></li>
                                <li><a href="">ハッシュタグ</a></li>
                                <li><a href="">所在地</a></li>
                                <li><a href="">Isostagram Lite</a></li>
                                <li><a href="">連絡先のアップロードとユーザー以外</a></li>
                            </ul>
                        </nav>
                        <div class="footer-nav">
                            <ul>
                                <li>
                                    <span class="language">日本語<span
                                            style="display: inline-block; transform: rotate(180deg);"><svg
                                                aria-label="下向きシェブロンアイコン" class="_ab6-" color="#8e8e8e" fill="#8e8e8e"
                                                height="12" role="img" viewBox="0 0 24 24" width="12">
                                                <path
                                                    d="M21 17.502a.997.997 0 0 1-.707-.293L12 8.913l-8.293 8.296a1 1 0 1 1-1.414-1.414l9-9.004a1.03 1.03 0 0 1 1.414 0l9 9.004A1 1 0 0 1 21 17.502Z">
                                                </path>
                                            </svg></span>
                                        <select name="language" class="select" onchange="la(this.value)">
                                            <option value="#">日本語</option>
                                            <option value="#">日本語</option>
                                            <option value="#">日本語</option>
                                            <option value="#">日本語</option>
                                            <option value="#">日本語</option>
                                        </select>
                                    </span>
                                </li>
                                <li>
                                    <div class="footer-logo">&copy; 2022 Isostagram from ADL</div>
                                </li>
                            </ul>
                        </div>
                    </div> <!-- Footer container end -->
                </footer>
            </section>
        </span> <!-- Root -->
        <!-- Select Link -->
        <script type="text/javascript">
            function la(src) {
                window.location = src;
            }
        </script>
    </body>
    <?php
    }
    ?>
    <script src="js/jquery-slim.min.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
</body>

</html>