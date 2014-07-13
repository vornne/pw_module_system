<?php
require("server_response.php");
fix_headers();

class pw_store_player extends pw_server_response
{
  public function format_reply()
  {
    $from_server_id = $this->get_warband_server_id_from_input_password();

    $stmt = $this->db->prepare(
      "REPLACE INTO stored_characters (unique_id, from_server_id, to_server_id, link_id, instance_id, gold, troop_id, agent_troop_id,
      weapon_1_item_id, weapon_1_ammo, weapon_2_item_id, weapon_2_ammo, weapon_3_item_id, weapon_3_ammo, weapon_4_item_id, weapon_4_ammo,
      head_item_id, body_item_id, foot_item_id, hand_item_id, horse_item_id, hit_points, horse_hit_points, food)
      VALUES (:unique_id, :from_server_id, :to_server_id, :link_id, :instance_id, :gold, :troop_id, :agent_troop_id,
      :weapon_1_item_id, :weapon_1_ammo, :weapon_2_item_id, :weapon_2_ammo, :weapon_3_item_id, :weapon_3_ammo, :weapon_4_item_id, :weapon_4_ammo,
      :head_item_id, :body_item_id, :foot_item_id, :hand_item_id, :horse_item_id, :hit_points, :horse_hit_points, :food)");

    $player_id = $this->assert_valid_id_input("id", $this->pid_restrictions);
    $player_uid = $this->assert_valid_id_input("uid", $this->uid_restrictions);
    $stmt->bindValue(":unique_id", $player_uid);
    $stmt->bindValue(":from_server_id", $from_server_id);
    $to_server_id = $this->assert_valid_id_input("to-server", $this->var_restrictions);
    $stmt->bindValue(":to_server_id", $to_server_id);
    $stmt->bindValue(":link_id", $this->assert_valid_id_input("link", $this->var_restrictions));
    $stmt->bindValue(":instance_id", $this->assert_valid_id_input("inst", $this->uid_restrictions));
    $stmt->bindValue(":gold", $this->assert_valid_id_input("gold", $this->gold_restrictions));
    $stmt->bindValue(":troop_id", $this->assert_valid_id_input("troop", $this->id_restrictions));
    $stmt->bindValue(":agent_troop_id", $this->assert_valid_id_input("agent-troop", $this->id_restrictions));
    $stmt->bindValue(":weapon_1_item_id", $this->assert_valid_id_input("wpn1", $this->id_restrictions));
    $stmt->bindValue(":weapon_1_ammo", $this->assert_valid_id_input("ammo1", $this->pct_restrictions));
    $stmt->bindValue(":weapon_2_item_id", $this->assert_valid_id_input("wpn2", $this->id_restrictions));
    $stmt->bindValue(":weapon_2_ammo", $this->assert_valid_id_input("ammo2", $this->pct_restrictions));
    $stmt->bindValue(":weapon_3_item_id", $this->assert_valid_id_input("wpn3", $this->id_restrictions));
    $stmt->bindValue(":weapon_3_ammo", $this->assert_valid_id_input("ammo3", $this->pct_restrictions));
    $stmt->bindValue(":weapon_4_item_id", $this->assert_valid_id_input("wpn4", $this->id_restrictions));
    $stmt->bindValue(":weapon_4_ammo", $this->assert_valid_id_input("ammo4", $this->pct_restrictions));
    $stmt->bindValue(":head_item_id", $this->assert_valid_id_input("head", $this->id_restrictions));
    $stmt->bindValue(":body_item_id", $this->assert_valid_id_input("body", $this->id_restrictions));
    $stmt->bindValue(":foot_item_id", $this->assert_valid_id_input("foot", $this->id_restrictions));
    $stmt->bindValue(":hand_item_id", $this->assert_valid_id_input("hand", $this->id_restrictions));
    $stmt->bindValue(":horse_item_id", $this->assert_valid_id_input("horse", $this->id_restrictions));
    $stmt->bindValue(":hit_points", $this->assert_valid_id_input("hp", $this->pct_restrictions));
    $stmt->bindValue(":horse_hit_points", $this->assert_valid_id_input("horse-hp", $this->pct_restrictions));
    $stmt->bindValue(":food", $this->assert_valid_id_input("food", $this->pct_restrictions));

    $return_code = pw_config::saved_on_same_server;
    $server_scene_names = "";
    if ($to_server_id > 0)
    {
      $server_stmt = $this->db->prepare("SELECT name, scene_name FROM warband_servers where id = ?");
      $server_stmt->execute(array($to_server_id));
      if ($row = $server_stmt->fetch(PDO::FETCH_OBJ))
      {
        $server_scene_names = "|" . $row->name . "|" . $row->scene_name;
        $return_code = pw_config::saved_transfer_server;
      }
      else
      {
        $to_server_id = $from_server_id;
      }
    }
    else
    {
      $to_server_id = $from_server_id;
    }

    $stmt->execute();

    return "$return_code|$player_id|$player_uid$server_scene_names";
  }

}

$store_player = new pw_store_player();
$store_player->print_reply();
?>
