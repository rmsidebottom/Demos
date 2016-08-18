<?php
$host="localhost";
$user="root";
$pass="password";
$db="demo";

$con = mysqli_connect($host, $user, $pass, $db);
$username = $_POST["username"];
$password = $_POST["password"];
$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = mysqli_query($con, $query);
if (mysqli_num_rows($result) > 1) {
	echo "<h1>Successfully Logged in!</h1>";
	echo "<h1>You beat my game :(</h1>";
	echo "<h1>Your sql statement:</h1>";
	var_dump($query);
	while ($row = mysqli_fetch_array($result)){
		echo "<h3>Username: $row[0]</h3>";
		echo "<h3>Password: $row[1]</h3>";
	} 
} else if (mysqli_num_rows($result) == 1) {
	echo "<h1>Successfully Logged in!</h1>";
	echo "<h1>Do you want to play a game? Try and get more users and passwords.";
	echo "<h1>Your sql statement:</h1>";
	var_dump($query);
	while ($row = mysqli_fetch_array($result)){
		echo "<h3>Username: $row[0]</h3>";
		echo "<h3>Password: $row[1]</h3>";
	} 
} else {
	echo "<h1>Try again.</h1>";;
	echo "<h1>Your sql statement:</h1>";
	var_dump($query);
}
?>
