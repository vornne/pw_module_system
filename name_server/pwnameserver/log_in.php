<?php
function show_log_in()
{
  if (isset($_GET["page"]) && $_GET["page"] == "log_out") $action = ".";
  else $action = htmlspecialchars($_SERVER["REQUEST_URI"]);
  echo("<form action=\"$action\" method=\"post\"><table id=\"log_in_box\"><tbody>");
  echo('<tr><td>Server name:</td><td><input type="text" name="server_name"/></td></tr>');
  echo('<tr><td>Server password:</td><td><input type="password" name="server_password"/></td></tr>');
  echo('<tr><td></td><td><input type="submit" name="log_in" value="Log in"/></td></tr>');
  echo('</tbody></table></form>');
}

function check_log_in($db)
{
  if (isset($_POST["log_in"]))
  {
    $server_name = filter_input(INPUT_POST, "server_name", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW|FILTER_FLAG_STRIP_HIGH);
    $server_password = filter_input(INPUT_POST, "server_password", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW);
    if ($server_name && $server_password)
    {
      $stmt = $db->prepare("SELECT id, name FROM warband_servers WHERE name = ? AND password = SHA1(?)");
      $stmt->execute(array($server_name, $server_password));
      if ($row = $stmt->fetch(PDO::FETCH_OBJ))
      {
        session_regenerate_id(true);
        $_SESSION["server_id"] = $row->id;
        $_SESSION["server_name"] = $row->name;
        $_SESSION["time"] = time();
        return true;
      }
    }
    echo('<div class="database_error">Invalid server name or password.</div>');
  }
  else if (isset($_SESSION["server_id"], $_SESSION["server_name"], $_SESSION["time"]))
  {
    $current_time = time();
    if ($current_time - $_SESSION["time"] < 3600)
    {
      $_SESSION["time"] = $current_time;
      return true;
    }
    else session_destroy();
  }
  return false;
}
?>
