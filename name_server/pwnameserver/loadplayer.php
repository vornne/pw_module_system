<?php
require("server_response.php");
fix_headers();

class pw_load_player extends pw_server_response
{
  public function format_reply()
  {
    $server_id = $this->get_warband_server_id_from_input_password();

    $player_id = $this->assert_valid_id_input("id", $this->pid_restrictions);
    $player_uid = $this->assert_valid_id_input("uid", $this->uid_restrictions);

    $return_values = array(pw_config::load_character_data, $player_id, $player_uid);

    $stmt = $this->db->prepare("DELETE FROM stored_characters WHERE time_stored < DATE_SUB(NOW(), INTERVAL 1 WEEK)");
    $stmt->execute();

    $stmt = $this->db->prepare("SELECT * FROM stored_characters WHERE unique_id = ?");
    $stmt->execute(array($player_uid));
    if ($ch = $stmt->fetch(PDO::FETCH_OBJ))
    {
      if ($server_id == $ch->from_server_id || $server_id == $ch->to_server_id)
      {
        array_push($return_values, $ch->from_server_id, $ch->link_id,
          ($ch->from_server_id == $server_id ? $ch->instance_id : -1),
          $ch->gold, $ch->troop_id, $ch->agent_troop_id,
          $ch->weapon_1_item_id, $ch->weapon_1_ammo, $ch->weapon_2_item_id, $ch->weapon_2_ammo,
          $ch->weapon_3_item_id, $ch->weapon_3_ammo, $ch->weapon_4_item_id, $ch->weapon_4_ammo,
          $ch->head_item_id, $ch->body_item_id, $ch->foot_item_id, $ch->hand_item_id, $ch->horse_item_id,
          $ch->hit_points, $ch->horse_hit_points, $ch->food);
      }
      else
      {
        $return_values[] = -1;
      }
    }
    else
    {
      $return_values[] = -1;
    }

    return implode("|", $return_values);
  }

}

$load_player = new pw_load_player();
$load_player->print_reply();
?>
