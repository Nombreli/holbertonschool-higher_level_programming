-- list records where name is not null ordered by score desc
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
