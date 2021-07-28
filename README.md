# Weather_Analytics_Project

Actual code is in master branch.

The program runs as a module, so do python "-m projects.pj01.weather" to run the program.

The program also requires certain arguments, so this should return "Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]"

[FILE] is a placeholder for the path to the CSV file to process. [COLUMN] is the column of the CSV file of interest. [OPERATION] can be any of list, min, avg, or max.

Examples of usage:
python -m projects.pj01.weather projects/pj01/2020-05-10-to-16.csv DailyAverageWindSpeed list
python -m projects.pj01.weather projects/pj01/2020-05-10-to-16.csv DailyAverageDryBulbTemperature list
python -m projects.pj01.weather projects/pj01/2020-05-10-to-16.csv DailyPrecipitation list 

This program is specifically built to process CSV files from https://www.ncdc.noaa.gov/. To process other data aside from the ones that are predownloaded, navigate to Data Access, find link to Land-based Station data, select Datasets and Products, and then select local climatological data.

It should present a tool for selecting a station. Once a station has been decided on, click “Add to Cart”. The data should be free. Navigate to the cart either by clicking on the orange bar at the bottom of the screen or by scrolling up to the top-right orange Cart link.

Select an output format of LCD CSV.

Give an email address for it to send the data to.
