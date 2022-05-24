<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site dynamique</title>
</head>
<body>
    <form action="response.php" method="post" accept-charset="utf-8">
        <fieldset>
            <legend>Avez vous un commentaire?</legend>  
            <p>
                <label for="rating">Appreciation</label>
                <input type="radio" name="rating"value="1" /> 1 
                <input type="radio" name="rating" value="2" /> 2
                <input type="radio" name="rating" value="3" /> 3 
                <input type="radio" name="rating" value="4" /> 4 
                <input type="radio" name="rating" value="5" /> 5
            </br>
                <label for="text">Quelle est votre prenom:</label>
                <input type="text" name="prenom" class="prenom" required="required"/>
            </br>
                <label for="email">Quelle est votre email:</label>
                <input type="email" name="email" class="email" required="required"/>
            </p>
            <p>
                <label for="comment">Commentaire </label>
                <textarea name="comment" rows="8" cols="40" required="required"></textarea>
            </p>
            <p><input name="confirm" type="submit" value="Confirmer"></p>
        </fieldset>
    </form>
    <?php
        require("connect.php");
        $connection = mysql_connect(server, login, password);
        if (!$connection) {
            echo("Connection error to sql server");
            exit;
        }
        mysql_select_db(db);
        
        $response = mysql_query("SELECT * FROM members ORDER BY `members`.`id` DESC");
        // Show values in sql on website
        while ($lign=mysql_fetch_array($response)) {
            echo nl2br("\nPseudo: {$lign['userName']}\nEmail: {$lign['email']}\nCommentaire: {$lign['comment']}\n\n");
        }
        mysql_close();
    ?>
</body>
</html>