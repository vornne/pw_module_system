USE persistent_world;

INSERT INTO warband_servers (name, password) VALUES ("Test server", SHA1("WD915Kyi18"));

INSERT INTO player_names (unique_id, name) VALUES (390403, "Laszlo");
INSERT INTO player_names (unique_id, name) VALUES (390403, "KoS_Laszlo");
INSERT INTO player_names (unique_id, name) VALUES (408812, "Vornne");
INSERT INTO player_names (unique_id, name) VALUES (390710, "Joss");

INSERT INTO clans (name) VALUES ("Developers");
SELECT (@clan_id:=id) FROM clans WHERE name = "Developers";
INSERT INTO clan_tags (clan_id, tag) VALUES (@clan_id, "DEV");
INSERT INTO clan_tags (clan_id, tag) VALUES (@clan_id, "Developer");
INSERT INTO clan_players (clan_id, unique_id) VALUES (@clan_id, 390403);
INSERT INTO clan_players (clan_id, unique_id) VALUES (@clan_id, 390710);
INSERT INTO clan_players (clan_id, unique_id) VALUES (@clan_id, 408812);

INSERT INTO clans (name) VALUES ("Knights of the South");
SELECT (@clan_id:=id) FROM clans WHERE name = "Knights of the South";
INSERT INTO clan_tags (clan_id, tag) VALUES (@clan_id, "KoS");
INSERT INTO clan_players (clan_id, unique_id) VALUES (@clan_id, 390403);
