<?php
function show_servers()
{
  $result = mysql_query("SELECT id, name FROM warband_servers;");
  if (!$result) return echo_database_error();
  echo('<table class="database_view"><thead><tr><th>name</th></tr></thead><tbody>');
  while ($row = mysql_fetch_assoc($result))
  {
    if ($row["id"] == $_SESSION["server_id"]) $hilight = ' class="set"';
    else $hilight = '';
    $server_name = htmlspecialchars($row["name"]);
    echo("<tr><td$hilight>$server_name</td></tr>");
  }
  echo("</tbody></table>\n");
}
?>
