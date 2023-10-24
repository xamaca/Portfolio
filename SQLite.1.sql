--get familiar with the data
SELECT*
From garmin_running

--order date to find the start of the training and the end
SELECT Date
FROM garmin_running
ORDER by date DESC

--find the average distance per day
SELECT avg(distance) AS average, day_of_the_week
FROM garmin_running
GROUP BY day_of_the_week

--find max distance per day 
SELECT max(distance) AS max_distance, day_of_the_week
FROM garmin_running
GROUP BY day_of_the_week

--group day of the week to find  average calories and average distance
SELECT avg(calories) as average_calories, day_of_the_week, avg(distance) as average_distance
FROM garmin_running
GROUP by day_of_the_week

--find what day of the week my average distance was <5 miles 
SELECT avg(distance) AS average_distance, day_of_the_week
FROM garmin_running
where distance < 5

--finding average_pace between 7 and 8 minutes
SELECT avg_pace, day_of_the_week
FROM garmin_running
WHERE avg_pace BETWEEN '7:00:00' AND '8:00:00'

--finding max distance in a day
SELECT max(distance) as max_dist, day_of_the_week
FROM garmin_running

--max calories in a day 
SELECT max(calories), day_of_the_week, distance
FROM garmin_running

--days where I ran between 20 and 30 minutes 
SELECt time, distance, day_of_the_week
FROM garmin_running
WHERE time BETWEEN '0:20:00' AND '0:30:00'

--find out what was the distane on my best training days 
SELECT avg_pace, day_of_the_week, distance, calories
From garmin_running
where avg_pace < '6:30:00'
