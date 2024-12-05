# Create-Link-Project (Udacity)
Explore-US-Bikeshare-Data

Over the past decade, bicycle-sharing systems have seen significant growth and widespread adoption in cities around the world. These systems allow users to rent bicycles for short-term use at a price, enabling them to pick up a bike at one location and return it at another, or return it to the same spot if they prefer to simply enjoy a ride. Each bike can be used by multiple riders throughout the day.

Thanks to advancements in information technology, accessing a bike-sharing station to unlock or return a bike has become easy. These technologies also generate valuable data that can provide insights into how people use bike-sharing systems.

In this project, I will analyze data from Motivate, a bike share system provider operating in several major U.S. cities, to explore bike-share usage patterns. The analysis will compare the system usage across three large cities: Chicago, New York City, and Washington, DC.

Project Goal

This project aims to examine bike-share system data for three major U.S. cities—Chicago, New York City, and Washington—using Python. I will write code to import the data and compute descriptive statistics to answer key questions. Additionally, I will develop a script that allows users to interact with the data through the terminal to view the computed statistics.

Software Requirements

To complete this project, the following software is needed:

Python 3, NumPy, and pandas, which can be installed using Anaconda
A text editor, such as Sublime or Atom
A terminal application (Terminal on Mac/Linux or Cygwin on Windows)
The Datasets

The dataset consists of randomly selected data from the first six months of 2017 for each city. All three cities’ data files include the following six core columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds, e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
Additionally, the Chicago and New York City datasets include:

Gender
Birth Year
The original, more detailed datasets can be accessed here for those who wish to explore them further (Chicago, New York City, Washington). These original files contained additional columns and varied formats, but have been condensed to the core six columns for analysis.

Statistics Computed

The output of the code will display the following statistics:

Popular Times of Travel

Most common month
Most common day of the week
Most common hour of the day
Popular Stations and Trips

Most common start station
Most common end station
Most common trip (frequent start-to-end station combination)
Trip Duration

Total travel time
Average travel time
User Information

Counts of each user type
Counts of each gender (only available for NYC and Chicago)
Earliest, most recent, and most common birth year (only available for NYC and Chicago)
The Interactive Experience

The bikeshare.py file is designed as a script that prompts the user for input to create an interactive experience in the terminal. The following four questions guide the experience:

Would you like to see data for Chicago, New York, or Washington?
Would you like to filter the data by month, day, or not at all?
If the user selects a month, they choose from January to June.
If the user selects a day, they choose from Monday to Sunday.
These choices determine the dataset and timeframe for analysis. After filtering, the script presents the statistical results, and the user can choose to restart or exit.

Additionally, the script asks if the user would like to see the raw data. If they answer "yes," the script will display 5 rows at a time, asking if they want to see 5 more rows. This process continues until the user selects "no" to stop displaying the data.
