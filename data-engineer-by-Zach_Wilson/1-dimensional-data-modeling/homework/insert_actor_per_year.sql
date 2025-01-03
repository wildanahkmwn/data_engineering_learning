with last_year AS (
    SELECT * FROM actors
    WHERE current_year = 1970
),
    this_year AS (
    SELECT actor,
		   actorid,
		   year,
		   CASE
            WHEN AVG(rating) > 8 THEN 'star'
            WHEN AVG(rating) > 7 THEN 'good'
            WHEN AVG(rating) > 6 THEN 'average'
	        ELSE 'bad'
	       END :: quality_class,
		   ARRAY_AGG(ARRAY[ROW(
            film,
            votes,
            rating,
            filmid
            )::films]) as films
	FROM actor_films
    where year = 1971
	group by 1,2,3
    )
	
SELECT
    COALESCE(ty.actor, ly.actor) AS actor,
    COALESCE(ty.actorid, ly.actorid) AS actorid,
    COALESCE(ty.year, ly.current_year + 1) as current_year,
    CASE WHEN ly.films is NULL THEN ty.films
         WHEN ty.year IS NOT NULL THEN ly.films || ty.films
         ELSE ly.films
    END AS films,
    CASE WHEN ty.year IS NOT NULL THEN ty.quality_class
    	 ELSE ly.quality_class
    END AS quality_class,
    CASE WHEN ty.year IS NULL THEN FALSE
        ELSE TRUE
        END AS is_active
FROM last_year ly FULL OUTER JOIN this_year ty on ly.actorid = ty.actorid