-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name
FROM tv_genres AS tv_g
JOIN tv_show_genres ON tv_g.id = genre_id
JOIN tv_shows AS tv_s ON show_id = tv_s.id 
WHERE tv_s.title = "Dexter"
ORDER BY name ASC;
