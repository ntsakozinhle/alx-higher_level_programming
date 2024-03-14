-- List all shows in data dump hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name AS genre
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, genre ASC;