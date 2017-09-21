<html>
<body>

<form action="fum.php" method="get">
<p>
IP:<input type="text" name="IP" />
</p>
<p>
Port:<input type="text" name="Port" />
</p>
<p>
Community:<input type="text" name="Community" />
</p>
<p>
    <input type="submit" value="submit" />
</p>
</form>

<?php
$ip=$_GET["IP"];
$port1=$_GET["Port"];
$community=$_GET["Community"];
$servername="localhost";
$username="root";
$password="Jyothi!123";
$database="shiva";
$port="3306";
$conn= mysqli_connect($servername,$username,$password,$database,$port);
if (!$conn){
	die("connection failed:".mysqli_connect_error());
}

$sql="CREATE TABLE IF NOT EXISTS manager(
IP VARCHAR(255) NOT NULL,
Port VARCHAR(255) NOT NULL,
Community VARCHAR(255) NOT NULL
)";

if (mysqli_query($conn, $sql)) {
	$cl="TRUNCATE manager";
	$clear=mysqli_query($conn,$cl);
	$data="INSERT INTO manager (IP, Port, Community)
	VALUES ('$ip','$port1','$community')";
	if ($conn->query($data) === TRUE){
	//	echo "RECORDED";
	} else {
		echo "Error". $conn->error;
	}
} else {
	echo "ERROR". mysqli_error($conn);
}

?>

</body>
</html>
