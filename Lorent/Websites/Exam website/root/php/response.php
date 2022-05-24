<?php
    require("connect.php");
    $connection = mysql_connect(server, login, password);
    if (!$connection) {
        echo("Connection error to sql server");
        exit;
    }
    mysql_select_db(db);
    print "Connection success to DB";
    // Get info from form
    $name = $_POST["prenom"];
    $email = $_POST["email"];
    $review = $_POST["comment"];
    $rating = $_POST["rating"];
    $reviewTime = $_POST["dateTime"];

    // Insert values into sql
    if (isSet($_POST['add-comment'])) {
        $request = "INSERT INTO members(userName, email, comment, rating) VALUES('$name', '$email', '$review', '$rating')";
    }

    // Delete value from sql
    if (isSet($_POST['remove-comment'])) {
        $choice = "supprimer";
    }
    if ($choice = "supprimer") {
        $id = $_POST["id-comment"];
        $response = mysql_query("DELETE FROM `members` WHERE `id`=$id");
    }
    
    $result = mysql_query($request, $connection);
    if ($result) {
        echo "Connection success".$result;
    }
    else {
        echo "Request failed". mysql_error($connection);
    }

    header('Location: contact.php');
?>