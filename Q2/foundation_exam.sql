-- Active: 1698603634176@@127.0.0.1@3306@foundation_exam
CREATE DATABASE foundation_exam;

USE foundation_exam;

-- create a table for move_info

CREATE TABLE movie_info (
    Movie_ID INT PRIMARY KEY,
    Movie_Name VARCHAR(255),
    Movie_Length TIME,
    Age_Rating VARCHAR(5)
);

-- create a table for screens

CREATE TABLE screens (
    Screen_ID INT PRIMARY KEY,
    Four_K BOOLEAN
);

-- create a table for showings

CREATE TABLE showings (
    Showing_ID INT PRIMARY KEY,
    Movie_ID INT,
    Screen_ID INT,
    Start_Time TIME,
    Available_Seats INT,
    FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
    FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID)
);

-- insert all info into tables 

 INSERT INTO movie_info(movie_ID, movie_name, movie_length, age_rating)
 VALUES 
 (1, "The Movie", "2:19:00", "12A"),
 (2, "The Other Movie", "1:30:00", "15"),
 (3, "The 3D Amazing Movie",  "1:42:00", "PG"),
 (4, "La Allure", "1:09:00", "18"),
 (5, "The Cartoon", "1:15:00", "U"),
 (6, "The Scary Cartoon", "1:23:00", "PG"),
 (7, "The Coming Of Age", "1:40:00", "12A"),
 (8, "The War", "2:07:00", "15"),
 (9, "The Murder Mystery", "1:47:00", "15");

 INSERT INTO screens(screen_ID, four_k)
 VALUES 
  (1, True),
  (2, False),
  (3, True),
  (4, True),
  (5, True),
  (6, True),
  (7, True),
  (8, False),
  (9, True),
  (10, True);

 INSERT INTO showings(showing_ID, movie_ID,screen_ID, start_time, available_seats)
 VALUES 
  (1, 1, 2, '12:00:00', 10), 
  (2, 1, 2, '17:00:00', 23), 
  (3, 2, 9, '10:30:00', 30), 
  (4, 3, 1, '07:00:00', 38), 
  (5, 3, 5, '10:00:00', 26), 
  (6, 3, 1, '17:00:00', 5), 
  (7, 3, 1, '19:00:00', 0), 
  (8, 3, 5, '14:00:00', 2), 
  (9, 4, 9, '20:00:00', 14), 
  (10, 4, 9, '23:00:00', 23), 
  (11, 5, 6, '09:30:00', 30), 
  (12, 5, 6, '12:30:00', 7), 
  (13, 5, 6, '14:30:00', 0), 
  (14, 5, 6, '15:20:00', 0), 
  (15, 6, 10, '10:00:00', 32), 
  (16, 6, 10, '13:30:00', 25), 
  (17, 6, 10, '17:00:00', 14), 
  (18, 7, 7, '12:00:00', 36), 
  (19, 8, 4, '15:00:00', 24), 
  (20, 9, 3, '17:00:00', 0);
  
-- show movies that start after 12 o'clock and have at least on seat available 
-- joins movie info and showings ordered from first start time to last

SELECT mi.Movie_Name, s.Start_Time
FROM movie_info mi
JOIN showings s ON mi.Movie_ID = s.Movie_ID
WHERE s.Start_Time > '12:00:00' AND s.Available_Seats > 0
ORDER BY s.Start_Time;

-- Find the movie with the most showings, Join movie_info and showings tables using Movie_ID
-- Sort results in descending order based on the count of showings
-- Limit results to 1 row to get the movie with the most showings

SELECT mi.Movie_Name
FROM movie_info mi
JOIN showings s ON mi.Movie_ID = s.Movie_ID
GROUP BY mi.Movie_ID, mi.Movie_Name
ORDER BY COUNT(s.Showing_ID) DESC
LIMIT 1;

