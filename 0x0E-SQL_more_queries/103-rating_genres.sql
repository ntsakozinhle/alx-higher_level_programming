-- List all shows in data dump hbtn_0d_tvshows

SELECT tv_genre.name, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN hbtn_0d_tvshows_rate ON tv_show_genre.show.id = hbtn_0d_tvshows_rate.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
