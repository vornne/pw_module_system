<?php
header_remove();
function set_content_length($output)
{
  header("Content-Length: ".strlen($output));
  return $output;
}
ob_start("set_content_length");

require("private/config.php");

function player_check_clan_tag($player_uid, $escaped_name)
{
  $clan_tag = strtok($escaped_name, "\\".pw_name_server_config::valid_separators);
  if ($clan_tag !== false)
  {
    $result = mysql_query("SELECT clan_id FROM clan_tags WHERE tag = '$clan_tag';");
    if (!$result) return pw_database_error();
    if ($row = mysql_fetch_assoc($result))
    {
      $result = mysql_query("SELECT id FROM clan_players WHERE clan_id = '$row[clan_id]' AND unique_id = '$player_uid';");
      if (!$result) return pw_database_error();
      if (mysql_num_rows($result) == 0)
      {
        return pw_name_server_config::clan_tag_error;
      }
    }
  }
  return 0;
}

function player_register_name($player_uid, $escaped_name, $warband_server_id)
{
  $return_code = player_check_clan_tag($player_uid, $escaped_name);
  if ($return_code > 0) return $return_code;

  $result = mysql_query("SELECT id, unique_id FROM player_names WHERE name = '$escaped_name';");
  if (!$result) return pw_database_error();
  if ($row = mysql_fetch_assoc($result))
  {
    if ($row["unique_id"] == $player_uid)
    {
      $result = mysql_query("UPDATE player_names SET last_used_time = CURRENT_TIMESTAMP() WHERE id = '$row[id]';");
      if (!$result) return pw_database_error();
    }
    elseif (player_check_clan_tag($row["unique_id"], $escaped_name) == pw_name_server_config::clan_tag_error)
    {
      $result = mysql_query("UPDATE player_names SET unique_id = '$player_uid' WHERE id = '$row[id]';");
      if (!$result) return pw_database_error();
      $result = mysql_query("SELECT id FROM player_names WHERE unique_id = '$player_uid' ORDER BY last_used_time;");
      if (!$result) return pw_database_error();
      $extra_player_names = mysql_num_rows($result) - pw_name_server_config::max_names_per_player;
      if ($extra_player_names > 0)
      {
        $result = mysql_query("DELETE FROM player_names WHERE unique_id = '$player_uid' ORDER BY last_used_time LIMIT $extra_player_names;");
        if (!$result) return pw_database_error();
      }
    }
    else
    {
      return pw_name_server_config::name_used_error;
    }
  }
  else
  {
    $result = mysql_query("SELECT id FROM player_names WHERE unique_id = '$player_uid' ORDER BY last_used_time;");
    if (!$result) return pw_database_error();
    if (mysql_num_rows($result) >= pw_name_server_config::max_names_per_player)
    {
      $row =  mysql_fetch_assoc($result);
      $result = mysql_query("UPDATE player_names SET name = '$escaped_name' WHERE id = '$row[id]';");
      if (!$result) return pw_database_error();
    }
    else
    {
      $result = mysql_query("INSERT INTO player_names (unique_id, name, inserted_by_warband_server_id) VALUES ('$player_uid', '$escaped_name', '$warband_server_id');");
      if (!$result) return pw_database_error();
    }
  }
  return pw_name_server_config::success;
}

function warband_server_id($server_password)
{
  $result = mysql_query("SELECT id FROM warband_servers WHERE password = SHA1('$server_password');");
  if (!$result)
  {
    pw_database_error();
  }
  elseif ($row = mysql_fetch_assoc($result))
  {
    return $row["id"];
  }
  return NULL;
}

function player_get_admin_permissions($player_uid, $warband_server_id)
{
  $permissions = 0;
  $result = mysql_query("SELECT * FROM admin_permissions WHERE unique_id = '$player_uid' AND server_id = '$warband_server_id';");
  if (!$result)
  {
    pw_database_error();
    return $permissions;
  }
  while ($row = mysql_fetch_row($result))
  {
    $bit = 0;
    $count = count($row);
    for ($i = pw_name_server_config::admin_permissions_first_field_no; $i < $count; ++$i)
    {
      if ($row[$i] != 0)
      {
        $permissions += 1 << $bit;
      }
      ++$bit;
    }
  }
  return $permissions;
}

function exit_code($code)
{
  exit("$code");
}

$server_password = filter_input(INPUT_GET, "password", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW);
if (!$server_password) exit_code(pw_name_server_config::input_error);

$config = new pw_name_server_config();
if (!$config->connect_database()) exit_code(pw_name_server_config::database_error);

$server_password = mysql_real_escape_string($server_password);
$warband_server_id = warband_server_id($server_password);
if (is_null($warband_server_id)) exit_code(pw_name_server_config::password_error);

$id_restrictions = array("options"=>array("min_range"=>0, "max_range"=>250));
$player_id = filter_input(INPUT_GET, "id", FILTER_VALIDATE_INT, $id_restrictions);
if ($player_id == 0) exit_code(pw_name_server_config::success);
$id_restrictions = array("options"=>array("min_range"=>1, "max_range"=>10000000));
$player_uid = filter_input(INPUT_GET, "uid", FILTER_VALIDATE_INT, $id_restrictions);
if (is_null($player_id) || is_null($player_uid) || !filter_has_var(INPUT_GET, "name")) exit_code(pw_name_server_config::input_error);

$return_code = pw_name_server_config::name_invalid_error;
$permissions = -1;
$name_restrictions = array("options"=>array("regexp"=>"/^[a-z0-9]([".pw_name_server_config::valid_separators."]?[a-z0-9])*$/i"));
$player_name = filter_input(INPUT_GET, "name", FILTER_VALIDATE_REGEXP, $name_restrictions);
if ($player_name)
{
  $escaped_name = mysql_real_escape_string($player_name);
  $return_code = player_register_name($player_uid, $escaped_name, $warband_server_id);

  if (filter_has_var(INPUT_GET, "admin"))
  {
    $permissions = player_get_admin_permissions($player_uid, $warband_server_id);
  }
}
else
{
  $player_name = preg_replace("/\|/", "/", $_GET["name"]);
  if (!$player_name) $player_name = "NULL";
}
if (is_numeric($player_name)) $player_name = "_" . $player_name;

echo "$return_code|$player_id|$player_uid|$player_name|$permissions";
?>
