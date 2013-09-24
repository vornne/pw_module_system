<?php
function show_admin_permissions($db)
{
  $count_stmt = $db->query("SELECT * FROM admin_permissions LIMIT 1");
  $field_count = $count_stmt->columnCount();

  foreach ($_POST as $key => $value)
  {
    if (substr_compare($key, "id_", 0, 3) == 0)
    {
      $id = filter_var($key, FILTER_SANITIZE_NUMBER_INT, array("options"=>array("min_range"=>0)));
      if (!isset($id) || !is_array($value) || count($value) <= 0) continue;
      $query = "UPDATE admin_permissions SET ";
      $valid = false;
      foreach ($value as $field_no)
      {
        if ($field_no[0] == 'n') $setting = '0';
        else $setting = '1';
        $field_no = filter_var($field_no, FILTER_SANITIZE_NUMBER_INT, array("options"=>array("min_range"=>0)));
        if (!isset($field_no) || $field_no >= $field_count) continue;
        $permission_name = $count_stmt->getColumnMeta($field_no)["name"];
        if ($valid) $query .= ", ";
        $query .= "$permission_name = '$setting'";
        $valid = true;
      }
      if (!$valid) continue;
      $query .= " WHERE id = ?";
      $stmt = $db->prepare($query);
      $stmt->execute(array($id));
    }
  }

  $stmt = $db->prepare("SELECT * FROM admin_permissions WHERE server_id = ?");
  $stmt->execute(array($_SESSION["server_id"]));
  $current_uri = htmlspecialchars($_SERVER["REQUEST_URI"]);
  echo("<form action=\"$current_uri\" method=\"post\">");
  echo('<table class="database_view"><thead><tr><th>unique id</th><th>recent<br/>name</th>');
  for ($i = pw_config::admin_permissions_first_field_no; $i < $field_count; ++$i)
  {
    $permission_name = str_replace("_", "<br/>", $count_stmt->getColumnMeta($i)["name"]);
    echo("<th>$permission_name</th>");
  }
  echo("</tr></thead>\n<tbody>");

  $unique_id = 0;
  $name_stmt = $db->prepare("SELECT name FROM player_names WHERE unique_id = :unique_id ORDER BY last_used_time DESC LIMIT 1");
  $name_stmt->bindParam(":unique_id", $unique_id);
  while ($row = $stmt->fetch(PDO::FETCH_BOTH))
  {
    $id = $row["id"];
    $unique_id = $row["unique_id"];
    $id_name = "id_$id"."[]";
    $admin_name = '';

    $name_stmt->execute();
    if ($name_row = $name_stmt->fetch(PDO::FETCH_ASSOC)) $admin_name = htmlspecialchars($name_row["name"]);
    echo("<tr><td><a href=\"?page=player_names&amp;filter=$unique_id&amp;by_uid\">$unique_id</a></td><td>$admin_name</td>");
    for ($i = pw_config::admin_permissions_first_field_no; $i < $field_count; ++$i)
    {
      if ($row[$i] != 0)
      {
        $set = ' class="set"';
        $n = 'n';
      }
      else
      {
        $set = '';
        $n = '';
      }
      echo("<td$set><input type=\"checkbox\" name=\"$id_name\" value=\"$n$i\"/></td>");
    }
    echo("</tr>\n");
  }
  echo("</tbody></table>\n");
  echo('<div class="database_actions"><input type="submit" name="apply" value="Apply changes"/></div>');
  echo("</form>\n");
}
?>
