-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- IFNULL Return the specified value IF the expression is NULL, otherwise return the expression:
SELECT band_name, (IFNULL(split, 2021) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE "%Glam rock%"
    ORDER BY lifespan DESC;
