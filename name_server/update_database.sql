-- Update for PW_4_beta1
ALTER TABLE player_names ADD KEY (unique_id);
ALTER TABLE clan_players ADD UNIQUE KEY (clan_id, unique_id);
ALTER TABLE admin_permissions DROP KEY unique_id;
ALTER TABLE admin_permissions ADD UNIQUE KEY (server_id, unique_id);
ALTER TABLE admin_permissions ADD COLUMN animals BOOLEAN DEFAULT FALSE NOT NULL AFTER mute;

-- Update for PW_4_beta3
ALTER TABLE admin_permissions ADD COLUMN factions BOOLEAN DEFAULT FALSE NOT NULL AFTER animals;

-- Update for PW_4.5.0
--   Default database name was changed from 'pw_player_names' to 'persistent_world'; you can keep your existing
--   database name and change private/config.php, or otherwise dump and restore your database into the new name:
--     mysql -u root -p -e "CREATE DATABASE persistent_world"
--     mysqldump -u root -p pw_player_names > backup_pw.sql
--     cat backup_pw.sql | mysql -u root -p persistent_world
--     mysql -u root -p -e "GRANT ALL ON persistent_world.* TO 'pw_name_server'@'localhost' IDENTIFIED BY 'yourpassword'"
--   Then remove the old database after you have checked the new one:
--     mysql -u root -p -e "DROP DATABASE pw_player_names"
CREATE TABLE sessions (
  id VARCHAR(32) NOT NULL,
  access_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  data TEXT,
  PRIMARY KEY (id)
);
ALTER TABLE player_names MODIFY COLUMN unique_id INT(8) UNSIGNED NOT NULL;
ALTER TABLE clan_players MODIFY COLUMN unique_id INT(8) UNSIGNED NOT NULL;
ALTER TABLE admin_permissions MODIFY COLUMN unique_id INT(8) UNSIGNED NOT NULL;

ALTER TABLE warband_servers MODIFY COLUMN name VARCHAR(28) NOT NULL;
ALTER TABLE warband_servers ADD COLUMN scene_name VARCHAR(28) NOT NULL AFTER password;
CREATE TABLE stored_characters (
  id INT(5) UNSIGNED NOT NULL AUTO_INCREMENT,
  unique_id INT(8) UNSIGNED NOT NULL,
  time_stored TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  from_server_id INT(5) UNSIGNED NOT NULL,
  to_server_id INT(5) UNSIGNED NOT NULL,
  link_id INT(1) UNSIGNED NOT NULL,
  instance_id INT(5) UNSIGNED NOT NULL,
  gold INT(10) UNSIGNED NOT NULL,
  troop_id INT(5) NOT NULL,
  agent_troop_id INT(5) NOT NULL,
  weapon_1_item_id INT(5) NOT NULL,
  weapon_1_ammo INT(5) UNSIGNED NOT NULL,
  weapon_2_item_id INT(5) NOT NULL,
  weapon_2_ammo INT(5) UNSIGNED NOT NULL,
  weapon_3_item_id INT(5) NOT NULL,
  weapon_3_ammo INT(5) UNSIGNED NOT NULL,
  weapon_4_item_id INT(5) NOT NULL,
  weapon_4_ammo INT(5) UNSIGNED NOT NULL,
  head_item_id INT(5) NOT NULL,
  body_item_id INT(5) NOT NULL,
  foot_item_id INT(5) NOT NULL,
  hand_item_id INT(5) NOT NULL,
  horse_item_id INT(5) NOT NULL,
  hit_points INT(5) UNSIGNED NOT NULL,
  horse_hit_points INT(5) UNSIGNED NOT NULL,
  food INT(5) UNSIGNED NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (unique_id)
);
