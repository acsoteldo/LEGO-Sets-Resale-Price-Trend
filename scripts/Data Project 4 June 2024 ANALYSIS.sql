SELECT Set_ID, Name, Year, Theme, Pieces, Minifigures, Price, Resale_Price
FROM sets_CLEANED
WHERE Theme = 'Star Wars'
  AND Year > 2010;

SELECT Theme, AVG(Resale_Price) AS Avg_Resale_Price
FROM sets_CLEANED
GROUP BY Theme;

SELECT Set_ID, Name, Theme, Year, Resale_Price
FROM sets_CLEANED
ORDER BY Resale_Price DESC
LIMIT 10;

-- most expensive set (by resale price) for each theme
SELECT s.Set_ID, s.Name, s.Theme, s.Year, s.Resale_Price
FROM sets_CLEANED s
WHERE s.Resale_Price = (
    SELECT MAX(s_inner.Resale_Price)
    FROM sets_CLEANED s_inner
    WHERE s_inner.Theme = s.Theme
)
ORDER BY s.Theme;
