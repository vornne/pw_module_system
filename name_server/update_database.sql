-- Update for PW_4_beta1
ALTER TABLE player_names ADD KEY (unique_id);
ALTER TABLE clan_players ADD UNIQUE KEY (clan_id, unique_id);
ALTER TABLE admin_permissions DROP KEY unique_id;
ALTER TABLE admin_permissions ADD UNIQUE KEY (server_id, unique_id);
ALTER TABLE admin_permissions ADD COLUMN animals BOOLEAN DEFAULT FALSE NOT NULL AFTER mute;

-- Update for PW_4_beta3
ALTER TABLE admin_permissions ADD COLUMN factions BOOLEAN DEFAULT FALSE NOT NULL AFTER animals;

-- Update for PW_4.5.0
CREATE TABLE sessions (
  id VARCHAR(32) NOT NULL,
  access_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  data TEXT,
  PRIMARY KEY (id)
);
