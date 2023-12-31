## 1. Introducing Joins ##

SELECT * FROM facts
    INNER JOIN cities ON cities.facts_id = facts.id
    LIMIT 10;

## 2. Understanding Inner Joins ##

SELECT c.*, f.name AS 'country_name' 
    FROM facts AS 'f'
    INNER JOIN cities AS 'c' ON c.facts_id = f.id
    LIMIT 5;

## 3. Practicing Inner Joins ##

SELECT f.name country, c.name capital_city FROM cities c
INNER JOIN facts f ON f.id = c.facts_id
WHERE c.capital = 1

## 4. Left Joins ##

SELECT f.name AS 'country',
       f.population
       FROM facts AS 'f'
       LEFT JOIN cities AS 'c' ON c.facts_id = f.id
       WHERE c.name IS NULL;

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name AS 'capital_city',
       f.name AS 'country',
       c.population
       
    FROM facts AS f
    INNER JOIN cities AS c ON c.facts_id = f.id
    WHERE c.capital == 1
    ORDER BY 3 DESC
    LIMIT 10;

## 7. Combining Joins with Subqueries ##

SELECT c.name capital_city, f.name country, c.population population
FROM facts f
INNER JOIN (
            SELECT * FROM cities
            WHERE capital = 1
            AND population > 10000000
           ) c ON c.facts_id = f.id
ORDER BY 3 DESC;

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT f.name AS country,
       c.population AS urban_pop,
       f.population AS total_pop,
       (CAST(c.population AS FLOAT) / CAST(f.population AS FLOAT)) AS urban_pct

       
    FROM facts AS f
    
    INNER JOIN (
        SELECT facts_id, 
               SUM(population) AS population
            FROM cities
            GROUP BY 1
                ) AS c ON c.facts_id = f.id
    WHERE urban_pct > 0.5 
    ORDER BY 4 ASC;