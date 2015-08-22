<?php

function get_ghost_mode($v)
{
  if ($v == 0) return "free";
  else return "locked to any player";
}

function get_control_block_direction($v)
{
  if ($v == 0) return "automatic";
  else return "by mouse movement";
}

function get_combat_speed($v)
{
  if ($v == 0) return "slowest";
  elseif ($v == 1) return "slow";
  elseif ($v == 2) return "medium";
  elseif ($v == 3) return "fast";
  else return "fastest";
}

function get_time_limit($minutes)
{
  $time_array = array();
  if ($minutes > 1440)
  {
    $days = (int)($minutes / 1440);
    $minutes %= 1440;
    if ($days > 0)
    {
      $days_str = "$days day";
      if ($days != 1) $days_str .= "s";
      array_push($time_array, $days_str);
    }
  }
  if ($minutes > 60)
  {
    $hours = (int)($minutes / 60);
    $minutes %= 60;
    if ($hours > 0)
    {
      $hours_str = "$hours hour";
      if ($hours != 1) $hours_str .= "s";
      array_push($time_array, $hours_str);
    }
  }
  if ($minutes > 0)
  {
    $minutes_str = "$minutes minute";
    if ($minutes != 1) $minutes_str .= "s";
  }
  return join(", ", $time_array);
}

function get_victory_condition($v)
{
  if ($v == 0) return "none";
  else return "hold all castles for $v minutes";
}

function get_weather_control($v)
{
  if ($v == 2) return "dynamic";
  elseif ($v == 1) return "always raining";
  else return "always fine";
}

function get_respawn_health($v)
{
  if ($v == 0) return "partial based on troop type";
  else return "full";
}

function get_server_xml(&$xml, $address, $port)
{
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, "http://$address");
  curl_setopt($ch, CURLOPT_PORT, $port);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 1);
  $data = curl_exec($ch);
  if (curl_errno($ch) != 0)
  {
    curl_close($ch);
    return "Server $address did not successfully reply on port $port.";
  }
  curl_close($ch);
  $xml = new SimpleXMLElement($data);
  return Null;
}

function display_full_server_stats($address, $port, $display_errors = true)
{
  $error = get_server_xml($xml, $address, $port);
  if (!is_null($error))
  {
    if ($display_errors == true)
    {
      echo("<p>$error</p>");
    }
    return;
  }
  $name = $xml->Name;
  echo("<table class=\"stats_box\"><tbody><tr class=\"name\"><td>Name:</td><td>$name</td></tr>");
  $version = $xml->ModuleName;
  echo("<tr class=\"r0\"><td>Version:</td><td>$version</td></tr>");
  $scene = $xml->MapName;
  echo("<tr class=\"r1\"><td>Scene:</td><td>$scene</td></tr>");
  $players = $xml->NumberOfActivePlayers;
  echo("<tr class=\"r0\"><td>Current players:</td><td>$players</td></tr>");
  $max_players = $xml->MaxNumberOfPlayers;
  echo("<tr class=\"r1\"><td>Maximum players:</td><td>$max_players</td></tr>");
  $has_password = strtolower($xml->HasPassword);
  echo("<tr class=\"r0\"><td>Has password:</td><td>$has_password</td></tr>");
  $ghost_mode = get_ghost_mode($xml->ModuleSetting0);
  echo("<tr class=\"r1\"><td>Spectator camera:</td><td>$ghost_mode</td></tr>");
  $control_block_direction = get_control_block_direction($xml->ModuleSetting1);
  echo("<tr class=\"r0\"><td>Control block direction:</td><td>$control_block_direction</td></tr>");
  $combat_speed = get_combat_speed($xml->ModuleSetting2);
  echo("<tr class=\"r1\"><td>Combat speed:</td><td>$combat_speed</td></tr>");
  $time_limit = get_time_limit($xml->ModuleSetting3);
  echo("<tr class=\"r0\"><td>Game time limit:</td><td>$time_limit</td></tr>");
  $respawn_period = $xml->ModuleSetting4;
  echo("<tr class=\"r1\"><td>Respawn period:</td><td>$respawn_period seconds</td></tr>");
  $starting_gold = $xml->ModuleSetting5;
  echo("<tr class=\"r0\"><td>Starting gold:</td><td>$starting_gold%</td></tr>");
  $combat_gold = $xml->ModuleSetting6;
  echo("<tr class=\"r1\"><td>Combat gold bonus:</td><td>$combat_gold%</td></tr>");
  $factions = $xml->ModuleSetting7;
  echo("<tr class=\"r0\"><td>Number of factions:</td><td>$factions</td></tr>");
  $victory_condition = get_victory_condition($xml->ModuleSetting8);
  echo("<tr class=\"r1\"><td>Victory condition:</td><td>$victory_condition</td></tr>");
  $weather_control = get_weather_control($xml->ModuleSetting9);
  echo("<tr class=\"r0\"><td>Weather:</td><td>$weather_control</td></tr>");
  $respawn_health = get_respawn_health($xml->ModuleSetting10);
  echo("<tr class=\"r1\"><td>Respawn health:</td><td>$respawn_health</td></tr>");
  $herd_animals = $xml->ModuleSetting11;
  echo("<tr class=\"r0\"><td>Herd animal limit:</td><td>$herd_animals</td></tr>");
  echo('</tbody></table>');
}

function display_server_stats_row($address, $port, &$errors_list = Null)
{
  $error = get_server_xml($xml, $address, $port);
  if (!is_null($error))
  {
    if (!is_null($errors_list))
    {
      array_push($errors_list, $error);
    }
    return;
  }
  $name = $xml->Name;
  $scene = $xml->MapName;
  $players = $xml->NumberOfActivePlayers;
  $max_players = $xml->MaxNumberOfPlayers;
  if ($xml->HasPassword == "Yes") $locked = "locked";
  else $locked = "";
  echo("<tr><td>$name</td><td>$scene</td><td style=\"text-align:center\">$players / $max_players</td><td>$locked</td></tr>");
}

?>
