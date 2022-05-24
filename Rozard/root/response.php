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
    // Insert values into sql
    $request = "INSERT INTO members(userName, email, comment) VALUES('$name', '$email', '$review')";
    $result = mysql_query($request, $connection);
    if ($result) {
        echo "Connection success".$result;
    }
    else {
        echo "Request failed". mysql_error($connection);
    }

    header('Location: index.php');
?>