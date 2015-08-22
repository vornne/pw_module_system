<?php
require_once("private/config.php");

function exit_code($code)
{
  exit("$code");
}

class pw_db
{
  public $db;
  public $echo_errors;

  public function __construct($failure_exit_code=Null, $echo_errors=False)
  {
    $this->echo_errors = $echo_errors;
    try
    {
      $this->db = new PDO('mysql:host=' . pw_config::database_server_name . ';dbname=' . pw_config::database_name,
        pw_config::database_username, pw_config::database_password, array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_PERSISTENT => true));
    }
    catch (PDOException $e)
    {
      $this->log_error($e);
      if (!is_null($failure_exit_code)) exit_code($failure_exit_code);
    }
  }

  public function log_error($exception)
  {
    if ($this->echo_errors)
    {
      echo('<div class="database_error">Database error: ' . htmlspecialchars($exception->getMessage()) . '</div>');
    }
    error_log('PW database error: ' . $exception->getMessage() . "; at " . $exception->getFile() . ":" . $exception->getLine());
  }

}

?>
