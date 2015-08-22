<?php
require_once("private/config.php");
require_once("database.php");

function set_content_length($output)
{
  header("Content-Length: ".strlen($output));
  return $output;
}

function fix_headers()
{
  header_remove();
  ob_start("set_content_length");
}

class pw_server_response extends pw_db
{
  public $pid_restrictions;
  public $uid_restrictions;
  public $var_restrictions;
  public $id_restrictions;
  public $gold_restrictions;
  public $pct_restrictions;

  public function __construct()
  {
    parent::__construct(pw_config::database_error);

    $this->pid_restrictions = array("options"=>array("min_range"=>1, "max_range"=>250));
    $this->uid_restrictions = array("options"=>array("min_range"=>1, "max_range"=>100000000));
    $this->var_restrictions = array("options"=>array("min_range"=>0, "max_range"=>127));
    $this->id_restrictions = array("options"=>array("min_range"=>-1, "max_range"=>100000));
    $this->gold_restrictions = array("options"=>array("min_range"=>0, "max_range"=>999999999));
    $this->pct_restrictions = array("options"=>array("min_range"=>0, "max_range"=>100));
  }

  public function get_warband_server_id_from_input_password()
  {
    $server_password = filter_input(INPUT_GET, "password", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW);
    if (!$server_password) exit_code(pw_config::input_error . "|password: $server_password");

    $stmt = $this->db->prepare("SELECT id FROM warband_servers WHERE password = SHA1(?)");
    $stmt->execute(array($server_password));
    if ($row = $stmt->fetch(PDO::FETCH_OBJ))
    {
      return $row->id;
    }
    else
    {
      exit_code(pw_config::password_error);
    }
  }

  public function assert_valid_id_input($name, $restrictions)
  {
    $value = filter_input(INPUT_GET, $name, FILTER_VALIDATE_INT, $restrictions);
    if (is_null($value))
    {
      exit(pw_config::input_error . "|$name");
    }
    return $value;
  }

  public function print_reply()
  {
    try
    {
      echo $this->format_reply();
    }
    catch (PDOException $e)
    {
      $this->log_error($e);
      exit_code(pw_config::database_error);
    }
  }

}

?>
