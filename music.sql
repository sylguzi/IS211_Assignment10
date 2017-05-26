CREATE TABLE artists (ID INTEGER PRIMARY KEY
					  ,Name TEXT)

CREATE TABLE albums (ID INTEGER PRIMARY KEY
					 ,Name TEXT
					 ,ArtistID INTEGER)

CREATE TABLE songs (ID INTEGER PRIMARY KEY
					,Name TEXT
					,ArtistID INTEGER
					,AlbumID INTEGER
					,TrackNumber INTEGER
					,TrackLength INTEGER)