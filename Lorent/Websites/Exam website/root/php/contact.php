<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!--Title-->
    <title>Contact Form</title>
    <!--Stylesheet-->
    <link rel="stylesheet" href="../src/css/style.css" />
    <!--Icons In Website-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" />
    <!--Website Icon-->
    <link rel="shortcut icon" href="../src/img/favicon.png" />
    <!--Imported Font Family-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    
</head>
<body>
    <nav class="navigation">
        <a href="../pages/index.html"><img draggable="flase" class="logo" src="../src/img/logo.png"/></a>

        <!--Menu-->
        <ul class="menu">
            <li><a href="../pages/index.html">Acceuil</a></li>
            <li><a href="../pages/index.html#categories">Catégories</a><li>
            <li><a href="contact.php">Contact</a></li>
        </ul>

        <div class="right-nav">
            <!--Login/register-->
            <a href="../index.html" class="login">
                <i class="fa-solid fa-user"></i>
            </a>
        </div>
    </nav>

    <div class="contact-box">
        <form action="response.php" class="form-spacing" method="POST" accept-charset="utf-8">
            <div class="left">
                <div class="rate">
                    <input type="radio" id="five" name="rating" value="5">
                    <label for="five"></label>
                    <input type="radio" id="four" name="rating" value="4">
                    <label for="four"></label>
                    <input type="radio" id="three" name="rating" value="3">
                    <label for="three"></label>
                    <input type="radio" id="two" name="rating" value="2">
                    <label for="two"></label>
                    <input type="radio" id="one" name="rating" value="1">
                    <label for="one"></label>
                </div>
            </div>

            <div class="contact-spacing"> 
                <input type="text" name="prenom" class="prenom input-field" placeholder="Votre Nom" required="required"/>
                <input type="email" name="email" class="email input-field" placeholder="Votre Email" required="required"/>
                <textarea name="comment" class="input-field textarea-feild" rows="8" cols="40" placeholder="Votre Message" required="required"></textarea>
                <input type="submit" name="add-comment" class="contact-btn" value="Envoyer">
            </div>
        </form>
    </div>
    
    <?php
        require("connect.php");
        $connection = mysql_connect(server, login, password);
        if (!$connection) {
            echo("Connection error to sql server");
            exit;
        }
        mysql_select_db(db);
        
        $response = mysql_query("SELECT * FROM members ORDER BY `id` DESC");
        // Shows values
        while ($lign=mysql_fetch_array($response)) {
            echo "<div class='comment-box'>";
            echo nl2br("{$lign['dateTime']}\n");
            // Shows users rating in stars
            for ($x = 0; $x <= $lign['rating'] - 1 and $x <= 4; $x++) {
                echo "★";
            }
            for ($x = 0; $x <= 4 - $lign['rating']; $x++) {
            echo "☆";
            }
            // Show values in sql on website
            echo nl2br("\nPseudo: {$lign['userName']}\nEmail: {$lign['email']}\nCommentaire: {$lign['comment']}\n");
            ?>
            <form action="response.php" method="POST">
                <input type='submit' name='remove-comment' class='contact-btn' value='Supprimer'>
                <input type='hidden' name='id-comment' class='contact-btn' value="<?php echo $lign['id'];?>">
            </form>
            <?php
            echo "</div>";
        }
    
        mysql_close();
    ?>
</body>
</html>