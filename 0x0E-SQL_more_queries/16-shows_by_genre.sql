-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT title, name
FROM tv_shows AS tv_s
LEFT JOIN tv_show_genres ON tv_s.id = show_id
LEFT JOIN tv_genres AS tv_g ON genre_id = tv_g.id
ORDER BY title, name;
