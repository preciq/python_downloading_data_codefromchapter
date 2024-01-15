"""
Process a downloaded CSV file and plot data from it
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt

from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')
# gets the file and saves it to an object "path"
lines = path.read_text().splitlines()
# divides the file into a list based on the lines (each indiv element is a line from the file)

reader = csv.reader(lines)
# a special object that can read and parse CSV files, which we will use below

header_row = next(reader)
# so it would appear that the reader object is an iterable
# since this is the first call to next, we get the very first line in the csv file and save it to "header_row"
# note that header row is a list; each of the individual columns in the csv header line form the individual elements 

for index, column_header in enumerate(header_row):
    # enumerate allows us to loop through a list and get both the indiv elements AND their indices
    print(index, column_header)
    # we print each individual element (individual header, in this case) next to its index (the order that it appears in the CSV file)
    
# reading some of the data within the csv
dates, highs, lows = [], [], []
for row in reader:
    # loop through each row (line) in the csv file, saved in reader
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    # extracts the data from the 3rd (2nd index, under "DATE" column) from each row
    # '%Y-%m-%d' specifies the format we expect the data to be in from the CSV
    # IT DOES NOT CHANGE THE FORMAT BY ITSELF
    dates.append(current_date)
    # appends this extracted data to the dates list
    
    high = int(row[4])
    # gets the 5th (4th index, under "TMAX" column) from each row
    highs.append(high)
    # appends to the highs list
    
    low = int(row[5])
    lows.append(low)
    # same as above but for low temperature

print(highs)

"""Plot the high, low and date temperature data"""

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs,  color='red', alpha=0.5)
# plots the data from highs (y axis) and dates (x axis) to a scatter (connected, line) graph
ax.plot(dates, lows, color='blue', alpha=0.5)
# same thing (a second plot), but for low temperatures. Dates remain the same, and the plot color is blue
# alpha value defines opacity; 0 is completely transparent, 1 is completely opaque
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)
# generates a shaded area (alpha 0.1 to be very transparent but still visible as a shaded area) between the highs line and the lows line


ax.set_title("Daily High Temps in Sitka, AK in 2021", fontsize=21)
ax.set_xlabel('Dates', fontsize=16)
ax.set_ylabel('Temp (F)', fontsize=16)
ax.tick_params(labelsize=16)
# set various graph features, like titles and labels

fig.autofmt_xdate()
# draws date labels diagonally so they do not overlap (as opposed to horizontally, i.e. 10-01-2000)

plt.show()