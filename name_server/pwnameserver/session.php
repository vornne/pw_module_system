<?php
class pw_session
{
  public $db;

  public function __construct($db)
  {
    $this->db = $db;
    session_set_save_handler(array($this, "open"), array($this, "close"), array($this, "read"), array($this, "write"),
      array($this, "destroy"), array($this, "gc"));
    register_shutdown_function("session_write_close");
    session_start();
  }

  public function open()
  {
    if ($this->db) return true;
    return false;
  }

  public function close()
  {
    return true;
  }

  public function read($id)
  {
    try
    {
      $stmt = $this->db->prepare("SELECT data FROM sessions WHERE id = ?");
      $stmt->execute(array($id));
      if ($row = $stmt->fetch(PDO::FETCH_OBJ))
      {
        return $row->data;
      }
      else
      {
        return "";
      }
    }
    catch (PDOException $e)
    {
      return "";
    }
  }

  public function write($id, $data)
  {
    try
    {
      $access_time = time();
      $stmt = $this->db->prepare("REPLACE INTO sessions (id, access_time, data) VALUES (?, FROM_UNIXTIME(?), ?)");
      $stmt->execute(array($id, $access_time, $data));
      return true;
    }
    catch (PDOException $e)
    {
      return false;
    }
  }

  public function destroy($id)
  {
    try
    {
      $stmt = $this->db->prepare("DELETE FROM sessions WHERE id = ?");
      $stmt->execute(array($id));
      $this->gc();
      return true;
    }
    catch (PDOException $e)
    {
      return false;
    }
  }

  public function gc()
  {
    try
    {
      $expired_time = time() - 3600;
      $stmt = $this->db->prepare("DELETE FROM sessions WHERE access_time < FROM_UNIXTIME(?)");
      $stmt->execute(array($expired_time));
      return true;
    }
    catch (PDOException $e)
    {
      return false;
    }
  }

};

?>
