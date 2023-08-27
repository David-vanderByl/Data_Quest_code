## 2. Joining Three Tables ##

SELECT 
    il.track_id,
    t.name AS track_name,
    mt.name AS track_type,
    il.unit_price,
    il.quantity
    
FROM invoice_line AS il

INNER JOIN track AS t ON t.track_id = il.track_id
INNER JOIN media_type AS mt ON mt.media_type_id = t.media_type_id
WHERE il.invoice_id == 4;

## 3. Joining More Than Three Tables ##

SELECT il.track_id,
       t.name AS track_name,
       at.name AS artist_name,
       mt.name AS track_type,
       il.unit_price,
       il.quantity
    
    FROM invoice_line AS il

    INNER JOIN track AS t ON t.track_id = il.track_id
    INNER JOIN media_type AS mt ON mt.media_type_id = t.media_type_id
    INNER JOIN album AS al ON al.album_id = t.album_id
    INNER JOIN artist AS at ON at.artist_id = al.artist_id
    WHERE il.invoice_id == 4;

## 4. Combining Multiple Joins with Subqueries ##

SELECT ta.album_name AS album,
       ta.artist_name AS artist,
       COUNT(*) AS tracks_purchased
       
    FROM invoice_line AS il

    INNER JOIN (
                SELECT 
                   t.track_id,
                   al.title AS album_name,
                   at.name AS artist_name

                FROM track AS t
                INNER JOIN album AS al ON al.album_id = t.album_id
                INNER JOIN artist AS at ON at.artist_id = al.artist_id
                ) AS ta
                ON ta.track_id = il.track_id
    GROUP BY 1, 2
    ORDER BY 3 DESC LIMIT 5;

## 5. Self-joins ##

SELECT 
        e1.first_name || ' ' || e1.last_name AS employee_name,
        e1.title AS employee_title,
        e2.first_name || ' ' || e2.last_name AS supervisor_name,
        e2.title AS supervisor_title
       
    FROM employee e1
    LEFT JOIN employee AS e2 ON e1.reports_to = e2.employee_id
    ORDER BY 1;

## 6. Pattern Matching Using Like ##

SELECT 
    first_name,
    last_name,
    phone

FROM customer
WHERE LOWER(first_name) like '%belle%'

## 7. Revisiting CASE ##

SELECT 
    c.first_name || ' ' || c.last_name AS customer_name,
    COUNT(i.invoice_id) AS number_of_purchases,
    (SUM(i.total)) AS total_spent,
    CASE 
        WHEN sum(i.total) < 40 THEN 'small spender'
        WHEN sum(i.total) > 100 THEN 'big spender'
        ELSE 'regular'
        END AS customer_category
FROM invoice i
INNER JOIN customer AS c ON c.customer_id = i.customer_id 
GROUP BY 1
ORDER BY 1;