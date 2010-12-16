<?php
  class pw_name_server_config
  {
    const db_connect_wrapper_filename = "databaseconnect.php";
    const db_name = "pw_player_names";
    const max_names_per_player = 5;

    const password_error = -3;
    const database_error = -2;
    const input_error = -1;
    const success = 0;
    const name_error = 1;
    const clan_tag_error = 2;
  }

  function pw_database_error()
  {
    error_log("pw database error: " . mysql_error());
    return pw_name_server_config::database_error;
  }

  function player_check_clan_tag($player_uid, $escaped_name)
  {
    $clan_tag_end = strpos($escaped_name, '_');
    if ($clan_tag_end !== false)
    {
      $clan_tag = substr($escaped_name, 0, $clan_tag_end);
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
      elseif (player_check_clan_tag($row["unique_id"], $escaped_name) == 2)
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
        return pw_name_server_config::name_error;
      }
    }
    else
    {
      $result = mysql_query("SELECT id FROM player_names WHERE unique_id = '$player_uid' ORDER BY last_used_time;");
      if (!$result) return pw_database_error();
      global $max_names_per_player;
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

  $server_password = filter_input(INPUT_GET, "password", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW);
  if (!$server_password) die((string)pw_name_server_config::input_error);

  require(pw_name_server_config::db_connect_wrapper_filename);
  $db_connection = pw_mysql_connect();
  if (!$db_connection) die ((string)pw_name_server_config::database_error);

  mysql_select_db(pw_name_server_config::db_name, $db_connection);

  $server_password = mysql_real_escape_string($server_password);
  $warband_server_id = warband_server_id($server_password);
  if ($warband_server_id === NULL) die((string)pw_name_server_config::password_error);

  $id_restrictions = array("options"=>array("min_range"=>1, "max_range"=>250));
  $player_id = filter_input(INPUT_GET, "id", FILTER_VALIDATE_INT, $id_restrictions);
  $id_restrictions = array("options"=>array("min_range"=>1, "max_range"=>10000000));
  $player_uid = filter_input(INPUT_GET, "uid", FILTER_VALIDATE_INT, $id_restrictions);
  $player_name = filter_input(INPUT_GET, "name", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW|FILTER_FLAG_STRIP_HIGH);
  if (!$player_id || !$player_uid || !$player_name) die((string)pw_name_server_config::input_error);

  $escaped_name = mysql_real_escape_string($player_name);
  $return_code = player_register_name($player_uid, $escaped_name, $warband_server_id);

  echo "$return_code|$player_id|$player_uid|$player_name";

  mysql_close($db_connection);
?>
