-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title
FROM tv_shows AS tv_s
JOIN tv_show_genres ON tv_s.id = show_id
JOIN tv_genres AS tv_g ON genre_id = tv_g.id
WHERE tv_g.name = "Comedy"
ORDER BY title;
