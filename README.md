# sqlalchemy-challenge

In this project I analyse the climate in Honolulu, Hawaii. There are two parts to this project
the first part is `Climate analysis and Exploration` the second part is `Designing a climate app`
which will be a Flask API.


## Part 1 Analysis and Exploration

In this part I use jupyter notebook and hawaii.sqlite files to complete my data exploration and 
climate analysis. I connected to the SQLite database by using SQLAlchemy. I analyse precipitation 
and then I analyse the stations in the area for temperatures within the previous 12 months.

### Analyzing Precipitation

* Found the most recent date in the dataset
* used the date to retrieve the previous 12 months of precipitation data
* selected the `date` and `prcp` values from the data
* loaded the query results into a dataframe, and set the index to the date column
* sorted the dataframe values by date 
* plotted the results by using the dataframe `plot` method
* used pandas to print the summary statistics for the prcp data


### Station Analysis

* Designed a query to calculate the total number of stations in the dataset
* Designed a query to find the most active stations 
   * Listed the stations and observation counts in descending order
   * Listed the stations and observation counts in descending order
   * Using the most active station id, calculated the lowest, highest, and average temperatures
* Designed a query to retrieve the previous 12 months of temperature observation data
    * Filtered by the station with the highest number of observations.
    * Query the previous 12 months of temperature observation data for this station.
    * Plotted the results as a histogram with bins=12

## Part 2 Designing my Climate app

In this part I create a Flask API using the queries that I have developed from Part 1

used the Flask to create my routes in the following manner

* `/`

  * Homepage
  * List all available routes

* `/api/v1.0/precipitation`

  * Converted the query results to a dictionary using date as the key and prcp as the value
  * Returned the JSON representation of your dictionary

* `/api/v1.0/stations`

  * Returned a JSON list of stations from the dataset

* `/api/v1.0/tobs`

  * Query the dates and temperature observations of the most active station for the previous year 
  *   of data
  * Returned a JSON list of temperature observations for the previous year

* `/api/v1.0/<start> and /api/v1.0/<start>/<end>`
  
  * Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature 
      for a given start or start-end range
  * Made it so when given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than or 
      equal to the start date
  * Made it so when given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates from the 
      start date through the end date 





