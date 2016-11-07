<?php
ob_start();
require("database.php");
$pw = new pw_db("", true);
require("session.php");
$session = new pw_session($pw->db);
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<link rel="stylesheet" type="text/css" href="main.css" />
<title>Persistent World name server administration</title>
</head>
<body>
<div id="header">
<h1>Persistent World name server administration</h1>
</div>
<div id="menu">
<hr/>
<a href="?page=player_names">Player names</a>
&nbsp;&nbsp;<a href="?page=admin_permissions">Admin permissions</a>
&nbsp;&nbsp;<a href="?page=servers">Servers</a>
&nbsp;&nbsp;<a href="?page=log_out">Log out</a>
<hr/>
</div>
<div id="page">

<?php
try
{
  require("log_in.php");
  if (!check_log_in($pw->db))
  {
    show_log_in();
  }
  else if (isset($_GET['page']))
  {
    switch ($_GET['page'])
    {
    case 'log_out':
      session_destroy();
      show_log_in($pw->db);
      break;
    case 'player_names':
      require("player_names.php");
      show_player_names($pw->db);
      break;
    case 'admin_permissions':
      require("admin_permissions.php");
      show_admin_permissions($pw->db);
      break;
    case 'servers':
      require("servers.php");
      show_servers($pw->db);
      break;
    default:
      echo('<div class="database_error">No such page.</div>');
    }
  }
}
catch (PDOException $e)
{
  $pw->log_error($e);
}
?>

</div>
</body>
</html>
