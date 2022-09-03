# sqlalchemy-challenge
My submission for Assignment 10.

## Overview

To help plan a trip to Hawaii, climate analysis was conducted on the area. The following sections outline the steps that were taken to accomplish this task.

### Part 1: Climate Analysis and Exploration

Python and SQLAlchemy were used to perform basic climate analysis and data exploration of the climate database. The following were used in completing this task: SQLAlchemy ORM queries, Pandas, and Matplotlib.

* SQLAlchemy’s `create_engine` was used to connect to the SQLite database.

* SQLAlchemy’s `automap_base()` to reflect the tables into classes and save a reference to those classes called `Station` and `Measurement`.

* Python was linked to the database by creating a SQLAlchemy session.

#### Precipitation Analysis

An analysis of precipitation in the area was performed, the following steps were taken:

* Found the most recent date in the dataset.

* Using this date, the previous 12 months of precipitation data were retrieved by querying the 12 previous months of data. 

* Only the `date` and `prcp` values were selected.

* Results were loaded and queried into a Pandas DataFrame, and set the index to the date column.

* The DataFrame was sorted by values by `date`.

* Results were plotted by using the DataFrame `plot` method.

* Pandas was used to print the summary statistics for the precipitation data.

#### Station Analysis

An analysis of stations in the area was performed, the following steps were taken:

* A query was designed to calculate the total number of stations in the dataset.

* A query was designed to find the most active stations (the stations with the most rows).

    * The stations and observation counts were listed in descending order.

    * Which station id has the highest number of observations?

    * Using the most active station id, the lowest, highest, and average temperatures were calculated.

* A query was designed to retrieve the previous 12 months of temperature observation data (TOBS).

    * Filtered by the station with the highest number of observations.

    * The previous 12 months of temperature observation data were queried for this station.

    * The results were plotted as a histogram with `bins=12`.

- - -

### Part 2: Design Your Climate App

Flask was used to create the following routes. The function of each route is described below.

* `/`

    * Homepage.

    * List all available routes.

* `/api/v1.0/precipitation`

    * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

    * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

    * Query the dates and temperature observations of the most active station for the previous year of data.

    * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than or equal to the start date.

    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates from the start date through the end date (inclusive).


#### Temperature Analysis 1

Conducted an analysis to answer the following question: Hawaii is reputed to enjoy mild weather all year round. Is there a meaningful difference between the temperatures in, for example, June and December?

* Used Pandas to perform the following steps:

    * Convert the date column format from `string` to `datetime`.

    * Set the date column as the DataFrame index.

    * Drop the date column.

* Identified the average temperature in June and December at all stations across all available years in the dataset. 

* Used the t-test to determine whether the difference in means, if any, is statistically significant. 

#### Temperature Analysis 2

You want to take a trip from August 1 to August 7 of this year, but you are worried that the weather will be less than ideal. Using historical data in the dataset, find out what the temperature has previously been for this timeframe.

The following steps were completed:

* Used the `calc_temps` function to calculate the minimum, average, and maximum temperatures for your trip using the matching dates from a previous year (for example, use "2017-08-01").

* Plotted the minimum, average, and maximum temperature from your previous query as a bar chart, as captured in the following steps and image:

    * Use "Trip Avg Temp" as the title.

    * Use the average temperature as the bar height (_y_ value).

    * Use the peak-to-peak (TMAX-TMIN) value as the _y_ error bar (YERR).


#### Daily Rainfall Average

Now that you have an idea of the temperature, let’s find out what the rainfall has been. You don't want to visit if it rains the whole time! Complete the following steps:

* Calculated the rainfall per weather station using the previous year's matching dates.

    * Sorted this in descending order by precipitation amount, and list the station, name, latitude, longitude, and elevation.

### Daily Temperature Normals

Calculated the daily normals for the duration of the trip. Normals are the averages for the minimum, average, and maximum temperatures.

Completed the following steps:

* Set the start and end date of the trip.

* Use the date to create a range of dates.

* Strip off the year, and save a list of strings in the format `%m-%d`.

* Used the `daily_normals` function to calculate the normals for each date string, and append the results to a list called `normals`.

* Loaded the list of daily normals into a Pandas DataFrame, and set the index equal to the date.

* Used Pandas to plot an area plot (`stacked=False`) for the daily normals.

## Analysis

* Regarding temperatures in June vs. December, it's better to use a paired t-test since we're dealing with similar samples taken by the same stations at different times. The p-value is very low which indicates that the temperature difference between June and December is, in fact, statistically significant. However, that difference is only around 4 degrees.
* Precipitation was very low at all stations during the trip dates in 2017 so it's likely that the first week of August will be relatively dry.
* Normal temperatures were consistent for the entire duration of the trip in 2017 so good weather can be expected during that time frame in Hawaii.

## Resources
* Homework 10 Instructions
* https://www.w3schools.com/