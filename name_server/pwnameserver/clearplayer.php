<?php
require("server_response.php");
fix_headers();

class pw_clear_player extends pw_server_response
{
  public function format_reply()
  {
    $server_id = $this->get_warband_server_id_from_input_password();

    $player_id = $this->assert_valid_id_input("id", $this->pid_restrictions);
    $player_uid = $this->assert_valid_id_input("uid", $this->uid_restrictions);

    $stmt = $this->db->prepare("DELETE FROM stored_characters WHERE unique_id = ?");
    $stmt->execute(array($player_uid));

    return pw_config::character_data_cleared . "|$player_id|$player_uid";
  }

}

$clear_player = new pw_clear_player();
$clear_player->print_reply();
?>
