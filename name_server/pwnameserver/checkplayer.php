<?php
require("server_response.php");
fix_headers();

class pw_check_player extends pw_server_response
{
  public function player_check_clan_tag($player_uid, $player_name)
  {
    $clan_tag = strtok($player_name, "\\".pw_config::valid_separators);
    if ($clan_tag == false) return 0;
    $stmt = $this->db->prepare("SELECT clan_id FROM clan_tags WHERE tag = ?");
    $stmt->execute(array($clan_tag));
    if (!($clan_id = $stmt->fetchColumn())) return 0;
    $stmt = $this->db->prepare("SELECT COUNT(*) FROM clan_players WHERE clan_id = ? AND unique_id = ?");
    $stmt->execute(array($clan_id, $player_uid));
    if ($stmt->fetchColumn() == 0) return pw_config::clan_tag_error;
    return 0;
  }

  public function player_register_name($player_uid, $player_name, $warband_server_id)
  {
    $return_code = $this->player_check_clan_tag($player_uid, $player_name);
    if ($return_code != 0) return $return_code;

    $stmt = $this->db->prepare("SELECT id, unique_id FROM player_names WHERE name = ?");
    $stmt->execute(array($player_name));
    if ($row = $stmt->fetch(PDO::FETCH_OBJ))
    {
      if ($row->unique_id == $player_uid)
      {
        $stmt = $this->db->prepare("UPDATE player_names SET last_used_time = CURRENT_TIMESTAMP() WHERE id = ?");
        $stmt->execute(array($row->id));
      }
      elseif ($this->player_check_clan_tag($row->unique_id, $player_name) == pw_config::clan_tag_error)
      {
        $stmt = $this->db->prepare("UPDATE player_names SET unique_id = ? WHERE id = ?");
        $stmt->execute(array($player_uid, $row->id));
        $stmt = $this->db->prepare("SELECT COUNT(*) FROM player_names WHERE unique_id = ? ORDER BY last_used_time");
        $stmt->execute(array($player_uid));
        $extra_names = $stmt->fetchColumn() - pw_config::max_names_per_player;
        if ($extra_names > 0)
        {
          $stmt = $this->db->prepare("DELETE FROM player_names WHERE unique_id = ? ORDER BY last_used_time LIMIT $extra_names");
          $stmt->execute(array($player_uid));
        }
      }
      else
      {
        return pw_config::name_used_error;
      }
    }
    else
    {
      $stmt = $this->db->prepare("SELECT id FROM player_names WHERE unique_id = ? ORDER BY last_used_time");
      $stmt->execute(array($player_uid));
      if ($stmt->rowCount() >= pw_config::max_names_per_player) // not guaranteed portable across all database types
      {
        $row = $stmt->fetch(PDO::FETCH_OBJ);
        $stmt = $this->db->prepare("UPDATE player_names SET name = :name, last_used_time = CURRENT_TIMESTAMP(), inserted_by_warband_server_id = :server WHERE id = :id");
        $stmt->execute(array(":name" => $player_name, ":server" => $warband_server_id, ":id" => $row->id));
      }
      else
      {
        $stmt = $this->db->prepare("INSERT INTO player_names (unique_id, name, inserted_by_warband_server_id) VALUES (:uid, :name, :server)");
        $stmt->execute(array(":uid" => $player_uid, ":name" => $player_name, ":server" => $warband_server_id));
      }
    }
    return pw_config::success;
  }

  public function player_get_admin_permissions($player_uid, $warband_server_id)
  {
    $stmt = $this->db->prepare("SELECT * FROM admin_permissions WHERE unique_id = ? AND server_id = ?");
    $stmt->execute(array($player_uid, $warband_server_id));
    $permissions = 0;
    if ($row = $stmt->fetch(PDO::FETCH_NUM))
    {
      $bit = 0;
      $count = count($row);
      for ($i = pw_config::admin_permissions_first_field_no; $i < $count; ++$i)
      {
        if ($row[$i] != 0)
        {
          $permissions |= (1 << $bit);
        }
        ++$bit;
      }
    }
    return $permissions;
  }

  public function format_reply()
  {
    $warband_server_id = $this->get_warband_server_id_from_input_password();

    $player_id = filter_input(INPUT_GET, "id", FILTER_VALIDATE_INT, $this->pid_restrictions);
    if ($player_id == 0) exit_code(pw_config::success);
    $player_uid = filter_input(INPUT_GET, "uid", FILTER_VALIDATE_INT, $this->uid_restrictions);
    if (is_null($player_id) || is_null($player_uid) || !filter_has_var(INPUT_GET, "name")) exit_code(pw_config::input_error);

    $return_code = pw_config::name_invalid_error;
    $permissions = -1;
    $name_restrictions = array("options"=>array("regexp"=>"/^[a-z0-9]([".pw_config::valid_separators."]?[a-z0-9])*$/i"));
    $player_name = filter_input(INPUT_GET, "name", FILTER_VALIDATE_REGEXP, $name_restrictions);
    if ($player_name)
    {
      $return_code = $this->player_register_name($player_uid, $player_name, $warband_server_id);

      if (filter_has_var(INPUT_GET, "admin"))
      {
        $permissions = $this->player_get_admin_permissions($player_uid, $warband_server_id);
      }
    }
    else
    {
      $player_name = preg_replace("/\|/", "/", $_GET["name"]);
      if (!$player_name) $player_name = "NULL";
    }
    if (is_numeric($player_name)) $player_name = "_" . $player_name;

    return "$return_code|$player_id|$player_uid|$player_name|$permissions";
  }

}

$check_player = new pw_check_player();
$check_player->print_reply();
?>
