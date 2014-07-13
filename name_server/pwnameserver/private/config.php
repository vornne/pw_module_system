<?php
class pw_config
{
  const database_server_name = "localhost";
  const database_username = "pw_name_server";
  const database_password = "mcn345N2iH";
  const database_name = "persistent_world";
  const max_names_per_player = 5;
  const admin_permissions_first_field_no = 3;
  const valid_separators = "-_ '";
  const player_names_per_page = 100;

  const server_connect_error = -4;
  const password_error = -3;
  const database_error = -2;
  const input_error = -1;
  const success = 0;
  const name_used_error = 1;
  const clan_tag_error = 2;
  const name_invalid_error = 3;
  const not_registered_error = 4;

  const saved_on_same_server = 20;
  const saved_transfer_server = 21;
  const load_character_data = 22;
  const character_data_cleared = 23;
}

?>
