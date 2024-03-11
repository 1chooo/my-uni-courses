<?php
isset($_GET['source']) and die(show_source(__FILE__, true));
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bocchi Search Tool</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">
</head>

<body>
    <section class="section">
        <div class="container">
            <div class="column is-6 is-offset-3 has-text-centered">
                <div class="box">
                    <h1 class="title">Bocchi Search Tool</h1>
                    <p>A tool help you find bocchi in json !</p>
                    <img src="Bocchi.gif"/>
                    <br>
                    <form method="POST">
                        <div class="field">
                            <div class="control">
                                <input class="input" type="text" name="json" placeholder='{"tenshi": "Ijichi Nijika", "bocchi": "Goto Hitori"}' id="hostname" value="<?= $_POST['json'] ?? '' ?>">
                            </div>
                        </div>
                        <button class="button is-block is-info is-fullwidth">
                            Search bocchi!
                        </button>
                    </form>
                    <br>
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
                    <hr>
                    <a href="/?source">Source Code</a>
                </div>
            </div>
        </div>
    </section>
</body>

</html>