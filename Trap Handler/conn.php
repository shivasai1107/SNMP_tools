<html>
<?php
$hostname="localhost";
$username="root";
$password="Jyothi!123";
$database="shiva";
$port="3306";

$dbc= mysqli_connect($hostname,$username,$password,$database,$port);

if (!$dbc) {
 	die("Connection.failed:". mysqli_connect_error());
}
//echo "Connected Succesfully<br>";

$query="SELECT fqdn,newstatus FROM DATA";

$response=mysqli_query($dbc,$query);
?>

<table align="left" cellspacing="5" cellpadding="8" border="2">
<tr>
<td align="left"><b>FQDN</b></td>
<td align="left"><b>STATUS</b></td>
</tr>

<?php
//$row=mysqli_fetch_array($response,true);
while($row=mysqli_fetch_array($response)){
?>
	
	
<tr>
<td><?php echo $row['fqdn']; ?></td>
<td><?php echo $row['newstatus']; ?></td>
</tr>
<?php } ?>
</table>

</html>
