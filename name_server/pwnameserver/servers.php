<?php
function show_servers($db)
{
  $stmt = $db->query("SELECT id, name FROM warband_servers;");
  echo('<table class="database_view"><thead><tr><th>name</th></tr></thead><tbody>');
  while ($row = $stmt->fetch(PDO::FETCH_OBJ))
  {
    if ($row->id == $_SESSION["server_id"]) $hilight = ' class="set"';
    else $hilight = '';
    $server_name = htmlspecialchars($row->name);
    echo("<tr><td$hilight>$server_name</td></tr>");
  }
  echo("</tbody></table>\n");
}
?>
