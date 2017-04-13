select * from Genre
--Added Artist to artist table
insert into artist values (null, 'Welshly Arms', 2013);

--Added Album to album table
insert into Album values (null, 'Covers EP', '2014', 2451, 'Good label', 28, 3);
insert into Album values (null, 'Welshley Arms', '2016', 2471, 'Good label', 28, 3);

--Added songs to songs table
insert into Song values (null, "Ain't Supposed to Rain", 400, '2016', 3, 28, 24);
insert into Song values (null, "The Touch", 400, '2016', 3, 28, 24);

select Song.Title, Album.Title, Artist.ArtistName
from Song
left join Artist on Song.ArtistId = Artist.ArtistId
left join Album on Album.GenreId = Song.GenreId
where Album.Title = "Welshley Arms"

select count(Song.Title), Album.Title
from Song, Album
where Album.AlbumId = Song.AlbumId
group by Album.AlbumId

select count(Song.Title), Artist.ArtistName
from Song, Artist
where Song.ArtistId = Artist.ArtistId
group by Song.ArtistId

select count(Song.Title) as Number_of_songs, Genre.Label
from Song, Genre
where Song.GenreId = Genre.GenreId
group by Song.GenreId

select max(AlbumLength) as Album_Length, Album.Title
from Album

select max(SongLength), Song.Title, Album.Title
from Song, Album


