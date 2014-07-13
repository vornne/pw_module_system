<?php
require("server_response.php");
fix_headers();

class pw_start_server extends pw_server_response
{
  public function format_reply()
  {
    $warband_server_id = $this->get_warband_server_id_from_input_password();

    $server_name = filter_input(INPUT_GET, "server-name", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW);
    $scene_name = filter_input(INPUT_GET, "scene-name", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW);
    if (is_null($server_name) || is_null($scene_name)) exit_code(pw_config::server_connect_error);

    $stmt = $this->db->prepare("UPDATE warband_servers SET name = ?, scene_name = ? WHERE id = ?");
    $stmt->execute(array($server_name, $scene_name, $warband_server_id));

    return pw_config::success . "|-1";
  }
}

$start_server = new pw_start_server();
$start_server->print_reply();
?>
