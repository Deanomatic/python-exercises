delete from Artist;
delete from Album;
delete from Genre;
delete from Song;

drop table if exists Artist;
drop table if exists Album;
drop table if exists Genre;
drop table if exists Song;


create table Artist (
	ArtistId integer not null primary key autoincrement,
	GenreId integer not null,
	Artist_name text not null,
	foreign key (GenreId) references Genre(GenreId)
);



create table Album (
	AlbumId integer not null primary key autoincrement,
	Album_name text not null,
	ArtistId integer not null,
	Release_date date not null,
	foreign key (ArtistId) references Artist (ArtistId)
);

create table Song (
	SongId integer not null primary key autoincrement,
	GenreId integer not null,
	Song_length integer not null,
	ArtistId integer not null,
	AlbumId integer not null,
	Song_name text not null,
	foreign key (ArtistId) references Artist(ArtistId),
	foreign key (GenreId) references Genre (GenreId),
	foreign key (AlbumId) references Album (AlbumId)
);

create table Genre (
	GenreId integer not null primary key,
	Genre_name text not null
);
--Adding artists to table
insert into Artist values (null, 1, 'Needtobreathe');
insert into Artist values (null, 5, 'John Mayer');
insert into Artist values (null, 3, 'Led Zeppelin');
insert into Artist values (null, 4, 'Brad Paisley');
insert into Artist values (null, 2, 'The Avett Brothers');

--Adding albums to table
insert into Album values (null, 'The Reckoning', 1, '7-15-16' );
insert into Album values (null, 'I and Love and you', 2, '7-15-10' );
insert into Album values (null, 'Led Zeppelin', 3, '7-15-16' );
insert into Album values (null, 'Mud on the Tires', 4, '7-15-23' );
insert into Album values (null, 'Continuum', 5, '7-15-06' );

--Adding songs to table
insert into Song values (null, 1, 180, 1, 1, 'Drive all Night');
insert into Song values (null, 4, 180, 4, 4, 'Im Still a Guy');
insert into Song values (null, 3, 180, 3, 3, 'Dazed and Confused');
insert into Song values (null, 2, 180, 2, 2, 'Kick drum Heart');
insert into Song values (null, 5, 180, 5, 5, 'Gravity');

--Adding genres to table
insert into Genre values (null, 'Crossover');
insert into Genre values (null, 'Indie Folk');
insert into Genre values (null, 'Classic Rock');
insert into Genre values (null, 'Country');
insert into Genre values (null, 'Blues');

