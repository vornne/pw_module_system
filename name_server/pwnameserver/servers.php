<?php
function show_servers($db)
{
  $stmt = $db->query("SELECT id, name, scene_name FROM warband_servers;");
  echo('<table class="database_view"><thead><tr><th>name</th><th>scene</th></tr></thead><tbody>');
  while ($row = $stmt->fetch(PDO::FETCH_OBJ))
  {
    if ($row->id == $_SESSION["server_id"]) $hilight = ' class="set"';
    else $hilight = '';
    $name = htmlspecialchars($row->name);
    $scene = htmlspecialchars($row->scene_name);
    echo("<tr><td$hilight>$name</td><td$hilight>$scene</td></tr>");
  }
  echo("</tbody></table>\n");
}
?>
