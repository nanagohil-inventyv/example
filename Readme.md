## Basic Queries:

### 1. Write a SQL query to find the name and year of the movies. Return movie title, movie release year.

### SQL Query
```sql
SELECT 
    mov_title,
    mov_year
FROM movie;
```

### Result 

| mov_title                | mov_year |
|--------------------------|----------|
| Vertigo                  | 1958     |
| The Innocents            | 1961     |
| Lawrence of Arabia       | 1962     |
| The Deer Hunter          | 1978     |
| Amadeus                  | 1984     |
| Blade Runner             | 1982     |
| Eyes Wide Shut           | 1999     |
| The Usual Suspects       | 1995     |
| Chinatown                | 1974     |
| Boogie Nights            | 1997     |
| Annie Hall               | 1977     |
| Princess Mononoke        | 1997     |
| The Shawshank Redemption | 1994     |
| American Beauty          | 1999     |
| Titanic                  | 1997     |
| Good Will Hunting        | 1997     |
| Deliverance              | 1972     |
| Trainspotting            | 1996     |
| The Prestige             | 2006     |
| Donnie Darko             | 2001     |
| Slumdog Millionaire      | 2008     |
| Aliens                   | 1986     |
| Beyond the Sea           | 2004     |
| Avatar                   | 2009     |
| Seven Samurai


### 2. Write a SQL query to find when the movie 'American Beauty' released. Return movie release year.

### SQL Query
```sql
SELECT 
    mov_year
FROM movie
WHERE mov_title = 'American Beauty';
```

### Result

| mov_year |
|----------|
| 1999     |


### 3. Write a SQL query to find the movie that was released in 1999. Return movie title.

### SQL Query
```sql
SELECT 
    mov_title
FROM movie
WHERE mov_year = 1999;
```

### Result 

| mov_title       |
|-----------------|
| Eyes Wide Shut  |
| American Beauty |




### 4. Write a SQL query to find those movies, which were released before 1998. Return movie title.

### SQL Query
```sql
SELECT 
    mov_title
FROM movie
WHERE mov_year < 1998;
```

### Result 

| mov_title                |
|--------------------------|
| Vertigo                  |
| The Innocents            |
| Lawrence of Arabia       |
| The Deer Hunter          |
| Amadeus                  |
| Blade Runner             |
| The Usual Suspects       |
| Chinatown                |
| Boogie Nights            |
| Annie Hall               |
| Princess Mononoke        |
| The Shawshank Redemption |
| Titanic                  |
| Good Will Hunting        |
| Deliverance              |
| Trainspotting            |
| Aliens                   |
| Seven Samurai            |
| Back to the Future       |
| Braveheart               |


### 5. Write a SQL query to find the name of all reviewers and movies together in a single list.

### SQL Query
```sql
SELECT rev_name AS name
FROM movie_reviewer
UNION
SELECT mov_title AS name
FROM movie;
```
### Result 

| name                     |
|--------------------------|
| Righty Sock              |
| Jack Malvern             |
| Flagrant Baronessa       |
| Alec Shaw                |
|                          |
| Victor Woeltjen          |
| Simon Wright             |
| Neal Wruck               |
| Paul Monks               |
| Mike Salvati             |
| Wesley S. Walker         |
| Sasha Goldshtein         |
| Josh Cates               |
| Krug Stillo              |
| Scott LeBrun             |
| Hannah Steele            |
| Vincent Cadena           |
| Brandt Sponseller        |
| Richard Adams            |
| Vertigo                  |
| The Innocents            |
| Lawrence of Arabia       |
| The Deer Hunter          |
| Amadeus                  |
| Blade Runner             |
| Eyes Wide Shut           |
| The Usual Suspects       |
| Chinatown                |
| Boogie Nights            |
| Annie Hall               |
| Princess Mononoke        |
| The Shawshank Redemption |
| American Beauty          |
| Titanic                  |
| Good Will Hunting        |
| Deliverance              |
| Trainspotting            |
| The Prestige             |
| Donnie Darko             |
| Slumdog Millionaire      |
| Aliens                   |
| Beyond the Sea           |
| Avatar                   |
| Seven Samurai            |
| Spirited Away            |
| Back to the Future       |
| Braveheart               |



### 6. Write a SQL query to find all reviewers who have rated seven or more stars to their rating. Return reviewer name.

### SQL Query
```sql
SELECT DISTINCT 
    r.rev_name
FROM movie_reviewer r
JOIN movie_rating mr ON r.rev_id = mr.rev_id
WHERE mr.rev_stars >= 7;
```

### Result

| rev_name           |
|--------------------|
| Righty Sock        |
| Jack Malvern       |
| Flagrant Baronessa |
|                    |
| Simon Wright       |
| Mike Salvati       |
| Sasha Goldshtein   |
| Hannah Steele      |
| Vincent Cadena     |
| Brandt Sponseller  |
| Victor Woeltjen    |
| Krug Stillo        |



### 7. Write a SQL query to find the movies without any rating. Return movie title.

### SQL Query
```sql
SELECT 
    m.mov_title
FROM movie m
LEFT JOIN movie_rating mr ON m.mov_id = mr.mov_id
WHERE mr.mov_id IS NULL;
```
### Result

| mov_title                |
|--------------------------|
| The Deer Hunter          |
| Amadeus                  |
| Eyes Wide Shut           |
| The Shawshank Redemption |
| Deliverance              |
| The Prestige             |
| Spirited Away            |
| Back to the Future       |
| Braveheart               |



### 8. Write a SQL query to find the movies with ID 905 or 907 or 917. Return movie title.

### SQL Query

```sql
SELECT mov_title FROM movie WHERE mov_id IN (905 , 907 , 917)
```
### Result
| mov_title |
|-----------|


### 9. Write a SQL query to find the movie titles that contain the word '*Boogie Nights*'. Sort the result-set in ascending order by movie year. Return movie ID, movie title and movie release year.

### SQL Query

```sql
SELECT 
    mov_id , 
    mov_title , 
    YEAR(mov_dt_rel)
FROM movie 
WHERE mov_title LIKE '%Boogie Nights%'
ORDER BY mov_year;
```
### Result

| mov_id | mov_title     | YEAR(mov_dt_rel) |
|--------|---------------|------------------|
|     10 | Boogie Nights |             1998 |


10. Write a SQL query to find those actors with the first name 'Woody' and the last name 'Allen'. Return actor ID.

### SQL Query 

```sql
SELECT 
    act_id 
FROM actor 
WHERE act_fname = 'Woody'
AND act_lname = 'Allen';
```

### Result

| act_id |
|--------|
|     11 |

## Sub-Queries :

### 11. Write a SQL query to find the actors who played a role in the movie 'Annie Hall'. Return all the fields of actor table.

### 12. Write a SQL query to find the director of a film that cast a role in 'Eyes Wide Shut'. Return director first name, last name.

### 13. Write a SQL query to find those movies that have been released in countries other than the United Kingdom. Return movie title, movie year, movie time, and date of release, releasing country.

### 14. Write a SQL query to find for movies whose reviewer is unknown. Return movie title, year, release date, director first name, last name, actor first name, last name.

### 15. Write a SQL query to find those movies directed by the director whose first name is Woddy and last name is Allen. Return movie title.

### 16. Write a SQL query to determine those years in which there was at least one movie that received a rating of at least three stars. Sort the result-set in ascending order by movie year. Return movie year.

### 17. Write a SQL query to search for movies that do not have any ratings. Return movie title.

### 18. Write a SQL query to find those reviewers who have not given a rating to certain films. Return reviewer name.

### 19. Write a SQL query to find movies that have been reviewed by a reviewer and received a rating. Sort the result-set in ascending order by reviewer name, movie title, review Stars. Return reviewer name, movie title, review Stars.

### 20. Write a SQL query to find movies that have been reviewed by a reviewer and received a rating. Group the result set on reviewer’s name, movie title. Return reviewer’s name, movie title.

### 21. Write a SQL query to find those movies, which have received highest number of stars. Group the result set on movie title and sorts the result-set in ascending order by movie title. Return movie title and maximum number of review stars.

### 22. Write a SQL query to find all reviewers who rated the movie 'American Beauty'. Return reviewer name.

### 23. Write a SQL query to find the movies that have not been reviewed by any reviewer body other than 'Paul Monks'. Return movie title.

### 24. Write a SQL query to find the movies with the lowest ratings. Return reviewer name, movie title, and number of stars for those movies.

### 25. Write a SQL query to find the movies directed by 'James Cameron'. Return movie title.

### 26. Write a query in SQL to find the movies in which one or more actors appeared in more than one film.


## Joins :

### 27. Write a SQL query to find all reviewers whose ratings contain a NULL value. Return reviewer name.

### 28. Write a SQL query to find out who was cast in the movie 'Annie Hall'. Return actor first name, last name and role.

### SQL Query
```sql
SELECT 
    a.act_fname,
    a.act_lname,
    mc.role
FROM actor a
JOIN movie_cast mc ON a.act_id = mc.act_id
JOIN movie m ON mc.mov_id = m.mov_id
WHERE m.mov_title = 'Annie Hall';
```
### Result
| act_fname | act_lname | role |
|-----------|-----------|------|
| Woody     | Allen     | Alvy Singer |


### 29. Write a SQL query to find the director who directed the movie **"Eyes Wide Shut"**  Return the director’s first name, last name, and the movie title.

### SQL Query
```sql
SELECT 
    d.dir_fname,
    d.dir_lname,
    m.mov_title
FROM director d
JOIN movie_direction md ON d.dir_id = md.dir_id
JOIN movie m ON md.mov_id = m.mov_id
WHERE m.mov_title = 'Eyes Wide Shut';
```

### Result
| dir_fname | dir_lname | mov_title      |
|-----------|-----------|----------------|
| Stanley   | Kubrick   | Eyes Wide Shut |


### 30. Write a SQL query to find the director of a movie that cast a role as Sean Maguire. Return director first name, last name and movie title.


### SQL Query
```sql
SELECT 
    d.dir_fname,
    d.dir_lname,
    m.mov_title
FROM director d
JOIN movie_direction md ON d.dir_id = md.dir_id
JOIN movie m ON md.mov_id = m.mov_id
JOIN movie_cast mc ON m.mov_id = mc.mov_id
WHERE mc.role = 'Sean Maguire';
```

### Result

| dir_fname | dir_lname | mov_title         |
|-----------|-----------|-------------------|
| Gus       | Van Sant  | Good Will Hunting |


### 31. Write a SQL query to find out which actors have not appeared in any movies between 1990 and 2000 (Begin and end values are included.). Return actor first name, last name, movie title and release year.

### SQL Query
```sql
SELECT 
    a.act_fname,
    a.act_lname,
    m.mov_title,
    m.mov_year
FROM actor a
JOIN movie_cast mc ON a.act_id = mc.act_id
JOIN movie m ON mc.mov_id = m.mov_id
WHERE NOT EXISTS (
    SELECT 1
    FROM movie_cast mc2
    JOIN movie m2 ON mc2.mov_id = m2.mov_id
    WHERE mc2.act_id = a.act_id
      AND m2.mov_year BETWEEN 1990 AND 2000
);
```

### Result

| act_fname | act_lname  | mov_title           | mov_year |
|-----------|------------|---------------------|----------|
| James     | Stewart    | Vertigo             | 1958     |
| Deborah   | Kerr       | The Innocents       | 1961     |
| Peter     | OToole     | Lawrence of Arabia  | 1962     |
| Robert    | De Niro    | The Deer Hunter     | 1978     |
| F. Murray | Abraham    | Amadeus             | 1984     |
| Harrison  | Ford       | Blade Runner        | 1982     |
| Jack      | Nicholson  | Chinatown           | 1974     |
| Christian | Bale       | Chinatown           | 1974     |
| Woody     | Allen      | Annie Hall          | 1977     |
| Jon       | Voight     | Deliverance         | 1972     |
| Maggie    | Gyllenhaal | Donnie Darko        | 2001     |
| Dev       | Patel      | Slumdog Millionaire | 2008     |
| Sigourney | Weaver     | Aliens              | 1986     |


### 32. Write a SQL query to find the directors who have directed films in a variety of genres. Group the result set on director first name, last name and generic title. Sort the result-set in ascending order by director first name and last name. Return director first name, last name and number of genres movies.

### SQL Query
```sql
SELECT 
    d.dir_fname,
    d.dir_lname,
    COUNT(DISTINCT g.gen_id) AS number_of_genres
FROM director d
JOIN movie_direction md ON d.dir_id = md.dir_id
JOIN movie m ON md.mov_id = m.mov_id
JOIN movie_genres mg ON m.mov_id = mg.mov_id
JOIN genres g ON mg.gen_id = g.gen_id
GROUP BY d.dir_fname, d.dir_lname
HAVING COUNT(DISTINCT g.gen_id) > 1
ORDER BY d.dir_fname ASC, d.dir_lname ASC;
```

### Result 

| dir_fname | dir_lname  | number_of_genres    |
|-----------|------------|---------------------|


### 33. Write a SQL query to find the movies with year and genres. Return movie title, movie year and generic title. give the answer not write  the question again and not give the any  other information only sql

### SQL Query 
```sql
SELECT 
    m.mov_title,
    m.mov_year,
    g.gen_title
FROM movie m
JOIN movie_genres mg ON m.mov_id = mg.mov_id
JOIN genres g ON mg.gen_id = g.gen_id;
```
### Result 

| mov_title                | mov_year | gen_title |
|--------------------------|----------|-----------|
| Aliens                   | 1986     | Action    |
| Lawrence of Arabia       | 1962     | Adventure |
| Deliverance              | 1972     | Adventure |
| Princess Mononoke        | 1997     | Animation |
| Annie Hall               | 1977     | Comedy    |
| The Usual Suspects       | 1995     | Crime     |
| The Shawshank Redemption | 1994     | Crime     |
| Trainspotting            | 1996     | Drama     |
| Slumdog Millionaire      | 2008     | Drama     |
| Spirited Away            | 2001     | Drama     |
| Braveheart               | 1995     | Drama     |
| The Innocents            | 1961     | Horror    |
| Beyond the Sea           | 2004     | Music     |
| Vertigo                  | 1958     | Mystery   |
| Eyes Wide Shut           | 1999     | Mystery   |
| Back to the Future       | 1985     | Mystery   |
| American Beauty          | 1999     | Romance   |
| Blade Runner             | 1982     | Thriller  |
| The Deer Hunter          | 1978     | War       |


### 34. Write a SQL query to find all the movies with year, genres, and name of the director.

### SQL Query 
```sql
SELECT 
    m.mov_title,
    m.mov_year,
    g.gen_title,
    d.dir_fname,
    d.dir_lname
FROM movie m
JOIN movie_genres mg ON m.mov_id = mg.mov_id
JOIN genres g ON mg.gen_id = g.gen_id
JOIN movie_direction md ON m.mov_id = md.mov_id
JOIN director d ON md.dir_id = d.dir_id;
```
### Result 

| mov_title                | mov_year | gen_title | dir_fname | dir_lname |
|--------------------------|----------|-----------|-----------|-----------|
| Aliens                   | 1986     | Action    | James     | Cameron   |
| Lawrence of Arabia       | 1962     | Adventure | David     | Lean      |
| Deliverance              | 1972     | Adventure | John      | Boorman   |
| Princess Mononoke        | 1997     | Animation | Hayao     | Miyazaki  |
| Annie Hall               | 1977     | Comedy    | Woody     | Allen     |
| The Usual Suspects       | 1995     | Crime     | Bryan     | Singer    |
| The Shawshank Redemption | 1994     | Crime     | Frank     | Darabont  |
| Trainspotting            | 1996     | Drama     | Danny     | Boyle     |
| Slumdog Millionaire      | 2008     | Drama     | Danny     | Boyle     |
| The Innocents            | 1961     | Horror    | Jack      | Clayton   |
| Beyond the Sea           | 2004     | Music     | Kevin     | Spacey    |
| Vertigo                  | 1958     | Mystery   | Alfred    | Hitchcock |
| Eyes Wide Shut           | 1999     | Mystery   | Stanley   | Kubrick   |
| American Beauty          | 1999     | Romance   | Sam       | Mendes    |
| Blade Runner             | 1982     | Thriller  | Ridley    | Scott     |
| The Deer Hunter          | 1978     | War       | Michael   | Cimino    |


### 35. Write a SQL query to find the movies released before 1st January 1989. Sort the result-set in descending order by date of release. Return movie title, release year, date of release, duration, and first and last name of the director.

### SQL Query 
```sql
SELECT 
    m.mov_title,
    m.mov_year,
    m.mov_dt_rel,
    m.mov_time,
    d.dir_fname,
    d.dir_lname
FROM movie m
JOIN movie_direction md ON m.mov_id = md.mov_id
JOIN director d ON md.dir_id = d.dir_id
WHERE m.mov_dt_rel < '1989-01-01'
ORDER BY m.mov_dt_rel DESC;
```

### Result 

| mov_title          | mov_year | mov_dt_rel | mov_time | dir_fname | dir_lname |
|--------------------|----------|------------|----------|-----------|-----------|
| Aliens             | 1986     | 1986-08-29 | 137      | James     | Cameron   |
| Amadeus            | 1984     | 1985-01-07 | 160      | Milos     | Forman    |
| Deliverance        | 1972     | 1982-10-05 | 109      | John      | Boorman   |
| Blade Runner       | 1982     | 1982-09-09 | 117      | Ridley    | Scott     |
| The Deer Hunter    | 1978     | 1979-03-08 | 183      | Michael   | Cimino    |
| Annie Hall         | 1977     | 1977-04-20 | 93       | Woody     | Allen     |
| Chinatown          | 1974     | 1974-08-09 | 130      | Roman     | Polanski  |
| Lawrence of Arabia | 1962     | 1962-12-11 | 216      | David     | Lean      |
| The Innocents      | 1961     | 1962-02-19 | 100      | Jack      | Clayton   |
| Vertigo            | 1958     | 1958-08-24 | 128      | Alfred    | Hitchcock |


### 36. Write a SQL query to calculate the average movie length and count the number of movies in each genre. Return genre title, average time and number of movies for each genre.

### SQL Query 
```sql
SELECT 
    g.gen_title,
    AVG(m.mov_time) AS avg_movie_time,
    COUNT(m.mov_id) AS number_of_movies
FROM genres g
JOIN movie_genres mg ON g.gen_id = mg.gen_id
JOIN movie m ON mg.mov_id = m.mov_id
GROUP BY g.gen_title;
```

### Result 

| gen_title | avg_movie_time | number_of_movies |
|-----------|----------------|------------------|
| Action    | 137.0000       | 1                |
| Adventure | 162.5000       | 2                |
| Animation | 134.0000       | 1                |
| Comedy    | 93.0000        | 1                |
| Crime     | 124.0000       | 2                |
| Drama     | 129.2500       | 4                |
| Horror    | 100.0000       | 1                |
| Music     | 118.0000       | 1                |
| Mystery   | 134.3333       | 3                |
| Romance   | 122.0000       | 1                |
| Thriller  | 117.0000       | 1                |
| War       | 183.0000       | 1                |




#### 37. Write a SQL query to find movies with the shortest duration. Return movie title, movie year, director first name, last name, actor first name, last name and role.

### SQL Query 
```sql
SELECT 
    m.mov_title,
    m.mov_year,
    d.dir_fname,
    d.dir_lname,
    a.act_fname,
    a.act_lname,
    mc.role
FROM movie m
JOIN movie_direction md ON m.mov_id = md.mov_id
JOIN director d ON md.dir_id = d.dir_id
JOIN movie_cast mc ON m.mov_id = mc.mov_id
JOIN actor a ON mc.act_id = a.act_id
WHERE m.mov_time = (
    SELECT MIN(mov_time)
    FROM movie
);
```

### Result 

| mov_title  | mov_year | dir_fname | dir_lname | act_fname | act_lname | role        |
|------------|----------|-----------|-----------|-----------|-----------|-------------|
| Annie Hall | 1977     | Woody     | Allen     | Woody     | Allen     | Alvy Singer |


### 38. Write a SQL query to find the years in which a movie received a rating of 3 or 4. Sort the result in increasing order on movie year.

### SQL Query 
```sql

SELECT DISTINCT
    m.mov_year
FROM movie m
JOIN movie_rating mr ON m.mov_id = mr.mov_id
WHERE mr.rev_stars IN (3, 4)
ORDER BY m.mov_year ASC;
```

### Result 

| mov_year |
|----------|
| 1997     |


### 39. Write a SQL query to get the reviewer name, movie title, and stars in an order that reviewer name will come first, then by movie title, and lastly by number of stars.

### SQL Query 
```sql
SELECT 
    r.rev_name,
    m.mov_title,
    mr.rev_stars
FROM movie_reviewer r
JOIN movie_rating mr ON r.rev_id = mr.rev_id
JOIN movie m ON mr.mov_id = m.mov_id
ORDER BY r.rev_name ASC, m.mov_title ASC, mr.rev_stars ASC;
```
### Result

| rev_name           | mov_title           | rev_stars |
|--------------------|---------------------|-----------|
|                    | Blade Runner        | 8.2       |
|                    | Princess Mononoke   | 8.4       |
| Brandt Sponseller  | Aliens              | 8.4       |
| Flagrant Baronessa | Lawrence of Arabia  | 8.3       |
| Hannah Steele      | Donnie Darko        | 8.1       |
| Jack Malvern       | The Innocents       | 7.9       |
| Josh Cates         | Good Will Hunting   | 4.0       |
| Krug Stillo        | Seven Samurai       | 7.7       |
| Mike Salvati       | Annie Hall          | 8.1       |
| Neal Wruck         | Chinatown           | NULL      |
| Paul Monks         | Boogie Nights       | 3.0       |
| Richard Adams      | Beyond the Sea      | 6.7       |
| Righty Sock        | Titanic             | 7.7       |
| Righty Sock        | Vertigo             | 8.4       |
| Sasha Goldshtein   | American Beauty     | 7.0       |
| Scott LeBrun       | Trainspotting       | NULL      |
| Simon Wright       | The Usual Suspects  | 8.6       |
| Victor Woeltjen    | Avatar              | 7.3       |
| Vincent Cadena     | Slumdog Millionaire | 8.0       |


### 40. Write a SQL query to find those movies that have at least one rating and received the most stars. Sort the result-set on movie title. Return movie title and maximum review stars.

### SQL Query 
```sql
SELECT 
    m.mov_title,
    MAX(mr.rev_stars) AS max_review_stars
FROM movie m
JOIN movie_rating mr ON m.mov_id = mr.mov_id
WHERE mr.rev_stars IS NOT NULL
GROUP BY m.mov_id, m.mov_title
HAVING MAX(mr.rev_stars) = (
    SELECT MAX(rev_stars)
    FROM movie_rating
    WHERE rev_stars IS NOT NULL
)
ORDER BY m.mov_title ASC;
```

### Result 

| mov_title          | max_review_stars |
|--------------------|------------------|
| The Usual Suspects | 8.6              |


### 42. Write a SQL query to find movies in which one or more actors have acted in more than one film. Return movie title, actor first and last name, and the role.

### SQL Query 
```sql
SELECT 
    m.mov_title,
    a.act_fname,
    a.act_lname,
    mc.role
FROM movie m
JOIN movie_cast mc ON m.mov_id = mc.mov_id
JOIN actor a ON mc.act_id = a.act_id
WHERE mc.act_id IN (
    SELECT act_id
    FROM movie_cast
    GROUP BY act_id
    HAVING COUNT(DISTINCT mov_id) > 1
)
ORDER BY m.mov_title, a.act_fname, a.act_lname;
```
### Result 

| mov_title       | act_fname | act_lname | role           |
|-----------------|-----------|-----------|----------------|
| American Beauty | Kevin     | Spacey    | Lester Burnham |
| Beyond the Sea  | Kevin     | Spacey    | Bobby Darin    |


### 43. Write a SQL query to find the actor whose first name is 'Claire' and last name is 'Danes'. Return director first name, last name, movie title, actor first name and last name, role.

### SQL Query 
```sql
SELECT 
    d.dir_fname,
    d.dir_lname,
    m.mov_title,
    a.act_fname,
    a.act_lname,
    mc.role
FROM actor a
JOIN movie_cast mc ON a.act_id = mc.act_id
JOIN movie m ON mc.mov_id = m.mov_id
JOIN movie_direction md ON m.mov_id = md.mov_id
JOIN director d ON md.dir_id = d.dir_id
WHERE a.act_fname = 'Claire'
  AND a.act_lname = 'Danes';
```

### Result

| dir_fname | dir_lname | mov_title         | act_fname | act_lname | role |
|-----------|-----------|-------------------|-----------|-----------|------|
| Hayao     | Miyazaki  | Princess Mononoke | Claire    | Danes     | San  |


### 44. Write a SQL query to find for actors whose films have been directed by them. Return actor first name, last name, movie title and role.

### SQL Query 
```sql
SELECT 
    a.act_fname,
    a.act_lname,
    m.mov_title,
    mc.role
FROM actor a
JOIN movie_cast mc ON a.act_id = mc.act_id
JOIN movie m ON mc.mov_id = m.mov_id
JOIN movie_direction md ON m.mov_id = md.mov_id
JOIN director d ON md.dir_id = d.dir_id
WHERE a.act_fname = d.dir_fname
  AND a.act_lname = d.dir_lname;
```
### Result

| act_fname | act_lname | mov_title      | role        |
|-----------|-----------|----------------|-------------|
| Woody     | Allen     | Annie Hall     | Alvy Singer |
| Kevin     | Spacey    | Beyond the Sea | Bobby Darin |


### 45. Write a SQL query to find the cast list of the movie ‘Chinatown’. Return first name, last name.

### SQL Query 
```sql
SELECT 
    a.act_fname,
    a.act_lname
FROM actor a
JOIN movie_cast mc ON a.act_id = mc.act_id
JOIN movie m ON mc.mov_id = m.mov_id
WHERE m.mov_title = 'Chinatown';
```
### Result

| act_fname | act_lname |
|-----------|-----------|
| Jack      | Nicholson |
| Christian | Bale      |


### 46. Write a SQL query to find those movies where actor’s first name is 'Harrison' and last name is 'Ford'. Return movie title.

### SQL Query 
```sql
SELECT 
    m.mov_title
FROM movie m
JOIN movie_cast mc ON m.mov_id = mc.mov_id
JOIN actor a ON mc.act_id = a.act_id
WHERE a.act_fname = 'Harrison'
  AND a.act_lname = 'Ford';
```
### Result

| mov_title    |
|--------------|
| Blade Runner |

### 47. Write a SQL query to find the highest-rated movies. Return movie title, movie year, review stars and releasing country.


### 48. Write a SQL query to find the highest-rated ‘Mystery Movies’. Return the title, year, and rating.

### 49. Write a SQL query to find the years when most of the ‘Mystery Movies’ produced. Count the number of generic title and compute their average rating. Group the result set on movie release year, generic title. Return movie year, generic title, number of generic title and average rating.

### 50. Write a query in SQL to generate a report, which contain the fields movie title, name of the female actor, year of the movie, role, movie genres, the director, date of release, and rating of that movie.

