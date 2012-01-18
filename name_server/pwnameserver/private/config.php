<?php
class pw_name_server_config
{
  const database_server_name = "localhost";
  const database_username = "pw_name_server";
  const database_password = "mcn345N2iH";
  const database_name = "pw_player_names";
  const max_names_per_player = 5;
  const admin_permissions_first_field_no = 3;
  const valid_separators = "-_ '";

  const password_error = -3;
  const database_error = -2;
  const input_error = -1;
  const success = 0;
  const name_used_error = 1;
  const clan_tag_error = 2;
  const name_invalid_error = 3;
  const not_registered_error = 4;

  public $connection;

  function connect_database()
  {
    $this->connection = mysql_connect(self::database_server_name, self::database_username, self::database_password);
    return ($this->connection && mysql_select_db(self::database_name, $this->connection));
  }

  function __destruct()
  {
    if ($this->connection) mysql_close($this->connection);
  }
}

function pw_database_error()
{
  error_log("PW database error: " . mysql_error());
  return pw_name_server_config::database_error;
}

function echo_database_error()
{
  echo('<div class="database_error">Database error: '.mysql_error().'</div>');
  return;
}
?>
