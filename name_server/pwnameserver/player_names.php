<?php
function check_player_name_actions($db)
{
  if (!filter_has_var(INPUT_POST, "ids")) return;
  $ids = $_POST["ids"];
  if (!is_array($ids)) return;
  $remove_names = filter_has_var(INPUT_POST, "remove_names");
  $set_permissions = filter_has_var(INPUT_POST, "set_permissions");
  foreach ($ids as $id)
  {
    $id = filter_var($id, FILTER_VALIDATE_INT, array("options"=>array("min_range"=>0)));
    if ($remove_names)
    {
      $stmt = $db->prepare("DELETE FROM player_names WHERE id = ?");
      $stmt->execute(array($id));
    }
    else if ($set_permissions)
    {
      $stmt = $db->prepare("SELECT unique_id FROM player_names WHERE id = ?  LIMIT 1");
      $stmt->execute(array($id));
      if (!$row = $stmt->fetch(PDO::FETCH_OBJ)) return;
      $stmt = $db->prepare("INSERT INTO admin_permissions (unique_id, server_id) VALUES (?, ?) ON DUPLICATE KEY UPDATE server_id = server_id");
      $stmt->execute(array($row->unique_id, $_SESSION["server_id"]));
    }
  }
  if ($set_permissions)
  {
    echo('<script type="text/javascript">window.location = "?page=admin_permissions"</script>');
  }
}

function show_player_names($db)
{
  check_player_name_actions($db);

  $current_uri_no_start = htmlspecialchars(preg_replace('/&start=[^=&]*/', '', $_SERVER["REQUEST_URI"]));
  echo("<form action=\"$current_uri_no_start\" method=\"get\"><div class=\"database_actions\">");
  echo('<input type="hidden" name="page" value="player_names"/>');
  if (isset($order_by)) echo("<input type=\"hidden\" name=\"order_by\" value=\"$order_by\"/>");
  echo('<label for="filter_text">Filter by:</label>');
  echo('<input type="text" name="filter" id="filter_text"/>');
  echo('<input type="submit" name="by_uid" value="unique id"/>');
  echo('<input type="submit" name="by_name" value="name"/>');
  echo("</div></form>\n");

  $params = array();
  $query = "SELECT player_names.id, unique_id, player_names.name AS player_name, last_used_time, warband_servers.name AS server_name
    FROM player_names LEFT JOIN warband_servers ON player_names.inserted_by_warband_server_id = warband_servers.id";
  if (isset($_GET["by_uid"]))
  {
    $filter_unique_id = filter_input(INPUT_GET, "filter", FILTER_VALIDATE_INT, array("options"=>array("min_range"=>1, "max_range"=>100000000)));
    if ($filter_unique_id)
    {
      $query .= " WHERE player_names.unique_id = :filter_unique_id";
      $params[":filter_unique_id"] = $filter_unique_id;
    }
  }
  else if (isset($_GET["by_name"]))
  {
    $filter_name = filter_input(INPUT_GET, "filter", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW|FILTER_FLAG_STRIP_HIGH);
    if ($filter_name)
    {
      $query .= " WHERE player_names.name LIKE :filter_name";
      $params[":filter_name"] = "%$filter_name%";
    }
  }

  $desc = "";
  if (isset($_GET["order_by"]))
  {
    $order_words = explode("_", $_GET["order_by"]);
    $order_by = $order_words[0];
    if ($order_by == "uid") $query .= " ORDER BY player_names.unique_id";
    else if ($order_by == "name") $query .= " ORDER BY player_names.name";
    else if ($order_by == "date") $query .= " ORDER BY player_names.last_used_time";
    else if ($order_by == "server") $query .= " ORDER BY player_names.inserted_by_warband_server_id";
    if (count($order_words) <= 1)
    {
      $desc = "_desc";
    }
    else
    {
      $query .= " DESC";
    }
  }
  $current_uri_no_order = htmlspecialchars(preg_replace('/&(order_by|start)=[^=&]*/', '', $_SERVER["REQUEST_URI"]));

  $filter_start = filter_input(INPUT_GET, "start", FILTER_VALIDATE_INT, array("options"=>array("min_range"=>0)));
  if ($filter_start)
  {
    $query .= " LIMIT $filter_start, " . pw_config::player_names_per_page;
  }
  else
  {
    $query .= " LIMIT " . pw_config::player_names_per_page;
  }

  $current_uri = htmlspecialchars($_SERVER["REQUEST_URI"]);

  $stmt = $db->prepare($query);
  $stmt->execute($params);

  $page_links = '<div class="database_actions">';
  if ($filter_start && $filter_start > 0)
  {
    $prev_page_start = max($filter_start - pw_config::player_names_per_page, 0);
    $page_links .= "<a href=\"$current_uri_no_start&amp;start=$prev_page_start\">Previous page</a>&nbsp;";
  }
  if ($stmt->rowCount() >= pw_config::player_names_per_page)
  {
    $next_page_start = $filter_start + pw_config::player_names_per_page;
    $page_links .= "<a href=\"$current_uri_no_start&amp;start=$next_page_start\">Next page</a>&nbsp;";
  }
  $page_links .= '</div>';
  echo($page_links);

  echo("<form action=\"$current_uri\" method=\"post\">");
  echo('<table class="database_view"><thead><tr><th/>');
  echo("<th><a href=\"$current_uri_no_order&amp;order_by=uid$desc\">unique id</a></th>");
  echo("<th><a href=\"$current_uri_no_order&amp;order_by=name$desc\">name</a></th>");
  echo("<th><a href=\"$current_uri_no_order&amp;order_by=date$desc\">last used</a></th>");
  echo("<th><a href=\"$current_uri_no_order&amp;order_by=server$desc\">created by server</a></th>");
  echo('</tr></thead><tbody>');
  while ($row = $stmt->fetch(PDO::FETCH_ASSOC))
  {
    $cb_id = "cb_$row[id]";
    echo("<tr><td><input type=\"checkbox\" name=\"ids[]\" value=\"$row[id]\" id=\"$cb_id\"/></td>");
    echo("<td><label for=\"$cb_id\">$row[unique_id]</label></td>");
    $player_name = htmlspecialchars($row["player_name"]);
    echo("<td><label for=\"$cb_id\">$player_name</label></td>");
    echo("<td><label for=\"$cb_id\">$row[last_used_time]</label></td>");
    $server_name = htmlspecialchars($row["server_name"]);
    echo("<td><label for=\"$cb_id\">$server_name</label></td>");
    echo("</tr>\n");
  }
  echo("</tbody></table>\n");
  echo($page_links);
  echo('<div class="database_actions">');
  echo('<input type="submit" name="remove_names" value="Remove names"/>');
  echo('<input type="submit" name="set_permissions" value="Set permissions"/>');
  echo("</div></form>\n");
}
?>
