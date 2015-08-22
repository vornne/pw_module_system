A simple name server for Warband servers running the Persistent World module.

To install, you need a web server with PHP and the PDO extension set up with
MySQL support; I use Linux and Apache (LAMP) so the instructions will be
tailored to that. Lines starting with "$" represent commands to run in the
shell prompt, and lines starting with "mysql>" represent queries to run in the
mysql command line tool.

First, copy the pwnameserver directory to your web server's document root;
then edit private/config.php, setting the desired the host name, user name,
password, and table name for the database; the password should be changed, but
all the other values can be left as they are.

Then you need to set up the mysql database: connect as your mysql admin user:

$ mysql --user=root --password

Create the database and grant access (values must match what you set in
private/config.php):

mysql> CREATE DATABASE persistent_world;
mysql> GRANT ALL ON persistent_world.* TO 'pw_name_server'@'localhost' IDENTIFIED BY 'mcn345N2iH';
mysql> QUIT;

Load the database schema:

$ mysql --user=pw_name_server --password=mcn345N2iH
mysql> SOURCE create_database.sql;

And then you can add some data based on the examples, editing the
test_values.sql file according to your needs first:

mysql> SOURCE test_values.sql;

Or input the data by hand: for example, to add and name some warband servers:

mysql> INSERT INTO warband_servers (name, password) VALUES ("My server", SHA1("MyPassword"));
mysql> INSERT INTO warband_servers (name, password) VALUES ("Other server", SHA1("OtherPassword"));

To add a new clan:

mysql> INSERT INTO clans (name) VALUES ("MyClan");

To add clan tags, you need to get the id of the clan; saving it to the variable
"@clan_id" is optional, you could just query the id and use the number directly.
The tags are not case sensitive.

mysql> SELECT (@clan_id:=id) FROM clans WHERE name = "MyClan";
mysql> INSERT INTO clan_tags (clan_id, tag) VALUES (@clan_id, "MC");
mysql> INSERT INTO clan_tags (clan_id, tag) VALUES (@clan_id, "MyC");

Then add players to the clan: the player's "unique_id" is what the module system
operation "player_get_unique_id" returns, what is shown in the server log when a
player joins, and the number used for permanent bans:

INSERT INTO clan_players (clan_id, unique_id) VALUES (@clan_id, 123456);
INSERT INTO clan_players (clan_id, unique_id) VALUES (@clan_id, 987654);

Now to setup the Warband servers, you need to open strings.txt, scroll near the
end of the file, and you should see a line starting with "str_name_server":
change this to the host name of the name server, including subdirectories; note
that the URL used must not include underscores, as the warband engine converts
these to spaces. In this example, the warband server will try connect to
"http://www.example.com/subdir/checkplayer.php":

str_name_server www.example.com/subdir

Then change the line "str_name_server_password" to the password you set up for
this server in the database, earlier:

str_name_server_password MyPassword

Make sure you don't add any extra lines or spaces to strings.txt, just replace
the existing values.

If the database is already set up from a previous version, you can copy the
relevant lines from update_database.sql to the mysql command line tool, rather
than regenerating the database from scratch and losing all your data.
