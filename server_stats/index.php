<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<link rel="stylesheet" type="text/css" href="main.css" />
<title>Persistent World Server Statistics</title>
</head>
<body>
<?php

$servers_list = array(
  array("localhost", 7240),
  );

require("display_server_stats.php");
$this_page = $_SERVER['SCRIPT_NAME'];
if (isset($_GET['type']) && $_GET['type'] == "full")
{
  echo("<p><a href=\"$this_page\">Change to short view.</a></p>");
  foreach ($servers_list as $server)
  {
    display_full_server_stats($server[0], $server[1]);
  }
}
else
{
  echo("<p><a href=\"$this_page?type=full\">Change to detailed view.</a></p>");
  echo("<table class=\"stats_list\"><tbody>");
  $errors_list = array();
  foreach ($servers_list as $server)
  {
    display_server_stats_row($server[0], $server[1], $errors_list);
  }
  echo("</tbody></table>");
  if ($errors_list)
  {
    echo("<p>");
    foreach ($errors_list as $error)
    {
      echo("$error<br/>");
    }
    echo("</p>");
  }
}
?>
</body>
</html>
