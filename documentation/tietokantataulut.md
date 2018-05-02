CREATE TABLE videogame ( id integer PRIMARY KEY, name varchar(144), genre varchar(50), releaseyear integer, developer_id integer FOREIGN KEY)

CREATE TABLE user (id integer PRIMARY KEY, name varchar(144), username varchar(144), password varchar(144))

CREATE TABLE gameinstance (id integer PRIMARY KEY, game_id integer FOREIGN KEY, user_id integer FOREIGN KEY)

CRETE TABLE developer (id integer PRIMARY KEY, name varchar(144), country varchar(144))