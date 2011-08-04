-- Update for PW_4_beta1
ALTER TABLE player_names ADD KEY (unique_id);
ALTER TABLE clan_players ADD UNIQUE KEY (clan_id, unique_id);
ALTER TABLE admin_permissions DROP KEY unique_id;
ALTER TABLE admin_permissions ADD UNIQUE KEY (server_id, unique_id);
