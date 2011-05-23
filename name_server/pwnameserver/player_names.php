<?php
function check_player_name_actions()
{
  $id = filter_input(INPUT_POST, "id", FILTER_VALIDATE_INT, array("options"=>array("min_range"=>0)));
  if (is_null($id) || $id === false) return;
  if (isset($_POST["remove_name"]))
  {
    $result = mysql_query("DELETE FROM player_names WHERE id = '$id';");
    if (!$result) return echo_database_error();
  }
  else if (isset($_POST["set_permissions"]))
  {
    $result = mysql_query("SELECT unique_id FROM player_names WHERE id = '$id' LIMIT 1;");
    if (!$result) return echo_database_error();
    if (!$row = mysql_fetch_assoc($result)) return;
    $result = mysql_query("INSERT INTO admin_permissions (unique_id, server_id) VALUES ('$row[unique_id]', '$_SESSION[server_id]');");
    if (!$result) return echo_database_error();
    echo('<script type="text/javascript">window.location = "?page=admin_permissions"</script>');
  }
}

function show_player_names()
{
  check_player_name_actions();

  $current_uri = htmlspecialchars($_SERVER["REQUEST_URI"]);
  $desc = "";
  if (isset($_GET["order_by"]))
  {
    $order_by = explode("_", $_GET["order_by"]);
    if (count($order_by) <= 1) $desc = "_desc";
    $order_by = $order_by[0];
    $cleaned_uri = htmlspecialchars(preg_replace('/[&?]order_by=[^=&?]*/', '', $_SERVER["REQUEST_URI"]));
  }
  else
  {
    $cleaned_uri = $current_uri;
  }

  echo("<form action=\"$current_uri\" method=\"get\"><div class=\"database_actions\">");
  echo('<input type="hidden" name="page" value="player_names"/>');
  if (isset($order_by)) echo("<input type=\"hidden\" name=\"order_by\" value=\"$order_by\"/>");
  echo('<label for="filter_text">Filter by:</label>');
  echo('<input type="text" name="filter" id="filter_text"/>');
  echo('<input type="submit" name="by_uid" value="unique id"/>');
  echo('<input type="submit" name="by_name" value="name"/>');
  echo("</div></form>\n");

  $query = "SELECT player_names.id, unique_id, player_names.name AS player_name, last_used_time, warband_servers.name AS server_name
    FROM player_names LEFT JOIN warband_servers ON player_names.inserted_by_warband_server_id = warband_servers.id";
  if (isset($_GET["by_uid"]))
  {
    $filter_unique_id = filter_input(INPUT_GET, "filter", FILTER_VALIDATE_INT, array("options"=>array("min_range"=>1, "max_range"=>10000000)));
    if ($filter_unique_id) $query .= " WHERE player_names.unique_id = '$filter_unique_id'";
  }
  else if (isset($_GET["by_name"]))
  {
    $filter_name = filter_input(INPUT_GET, "filter", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW|FILTER_FLAG_STRIP_HIGH);
    if ($filter_name)
    {
      $filter_name = mysql_real_escape_string($filter_name);
      $query .= " WHERE player_names.name LIKE '%$filter_name%'";
    }
  }

  if (isset($order_by))
  {
    if ($order_by == "uid") $query .= " ORDER BY player_names.unique_id";
    else if ($order_by == "name") $query .= " ORDER BY player_names.name";
    else if ($order_by == "date") $query .= " ORDER BY player_names.last_used_time";
    else if ($order_by == "server") $query .= " ORDER BY player_names.inserted_by_warband_server_id";
    if ($desc == "") $query .= " DESC";
  }

  $query .= ";";
  $result = mysql_query($query);
  if (!$result) return echo_database_error();
  echo("<form action=\"$current_uri\" method=\"post\">");
  echo('<table class="database_view"><thead><tr><th/>');
  echo("<th><a href=\"$cleaned_uri&amp;order_by=uid$desc\">unique id</a></th>");
  echo("<th><a href=\"$cleaned_uri&amp;order_by=name$desc\">name</a></th>");
  echo("<th><a href=\"$cleaned_uri&amp;order_by=date$desc\">last used</a></th>");
  echo("<th><a href=\"$cleaned_uri&amp;order_by=server$desc\">created by server</a></th>");
  echo('</tr></thead><tbody>');
  while ($row = mysql_fetch_assoc($result))
  {
    $rb_id = "rb_$row[id]";
    echo("<tr><td><input type=\"radio\" name=\"id\" value=\"$row[id]\" id=\"$rb_id\"/></td>");
    echo("<td><label for=\"$rb_id\">$row[unique_id]</label></td>");
    $player_name = htmlspecialchars($row["player_name"]);
    echo("<td><label for=\"$rb_id\">$player_name</label></td>");
    echo("<td><label for=\"$rb_id\">$row[last_used_time]</label></td>");
    $server_name = htmlspecialchars($row["server_name"]);
    echo("<td><label for=\"$rb_id\">$server_name</label></td>");
    echo("</tr>\n");
  }
  echo("</tbody></table>\n");
  echo('<div class="database_actions">');
  echo('<input type="submit" name="remove_name" value="Remove name"/>');
  echo('<input type="submit" name="set_permissions" value="Set permissions"/>');
  echo("</div></form>\n");
}
?>
