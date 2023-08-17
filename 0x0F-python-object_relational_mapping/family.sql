-- Family sql test

CREATE DATABASE IF NOT EXISTS family_db;
USE family_db;

CREATE TABLE IF NOT EXISTS family_members (
	id INT NOT NULL AUTO_INCREMENT,
	Father VARCHAR(30) DEFAULT "None",
	Mother VARCHAR(30) DEFAULT "None",
	Siz VARCHAR(30) DEFAULT "None",
	Bro VARCHAR(30) DEFAULT "None",
	PRIMARY KEY (id)
);

INSERT INTO family_members (Father) VALUES ("Paul Njenga"), ("James Ruga"), ("David Wainaina");
INSERT INTO family_members (Mother) VALUES ("Hannah Waceke"), ("Mama Maxi"), ("Beatrice Wanjiku");
INSERT INTO family_members (Siz) VALUES ("Mercy Muthoni"), (""), ("Lucy Wangari");
INSERT INTO family_members (Bro) VALUES ("__init__"), ("Joseph Njuguna"), ("Maxwell ...");

