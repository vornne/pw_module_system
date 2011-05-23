<?php
function show_admin_permissions()
{
  $count_result = mysql_query("SELECT * FROM admin_permissions LIMIT 1;");
  if (!$count_result) return;
  $field_count = mysql_num_fields($count_result);

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
        $permission_name = mysql_field_name($count_result, $field_no);
        if ($valid) $query .= ", ";
        $query .= "$permission_name = '$setting'";
        $valid = true;
      }
      if (!$valid) continue;
      $query .= " WHERE id = '$id';";
      $result = mysql_query($query);
    }
  }

  $result = mysql_query("SELECT * FROM admin_permissions WHERE server_id = '$_SESSION[server_id]';");
  if (!$result) return echo_database_error();
  $current_uri = htmlspecialchars($_SERVER["REQUEST_URI"]);
  echo("<form action=\"$current_uri\" method=\"post\">");
  echo('<table class="database_view"><thead><tr><th>unique id</th><th>recent<br/>name</th>');
  for ($i = pw_name_server_config::admin_permissions_first_field_no; $i < $field_count; ++$i)
  {
    $permission_name = str_replace("_", "<br/>", mysql_field_name($count_result, $i));
    echo("<th>$permission_name</th>");
  }
  echo("</tr></thead>\n<tbody>");

  while ($row = mysql_fetch_row($result))
  {
    $id = $row[0];
    $unique_id = $row[1];
    $id_name = "id_$id"."[]";
    $admin_name = '';
    $name_result = mysql_query("SELECT name FROM player_names WHERE unique_id = '$unique_id' ORDER BY last_used_time DESC LIMIT 1;");
    if ($name_result && $name_row = mysql_fetch_assoc($name_result)) $admin_name = htmlspecialchars($name_row["name"]);
    echo("<tr><td><a href=\"?page=player_names&amp;filter=$unique_id&amp;by_uid\">$unique_id</a></td><td>$admin_name</td>");
    for ($i = pw_name_server_config::admin_permissions_first_field_no; $i < $field_count; ++$i)
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
