from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
for index, column_header in enumerate(header_row):
    print(index, column_header)
    
# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    
    try:
        high = int(row[3])
        """
        by itself, this will throw an exception because some of the rows are missing data (missing rows)
        "USC00042319","DEATH VALLEY NATIONAL PARK, CA US","2021-05-04",,"72","89"
                                                                      ^^missing
        To handle issues like this, we have error handling (try except)
        """
        low = int(row[4])
    except ValueError:
        print(f"Data missing for the current date: {current_date}")
        # prints the date where data is missing for debugging purposes, but still processes the entire sheet without crashing due to an exception
    
    # an adjustment of the selected rows since highs are in column 4 and lows are in column 5 for death_valley_2021_simple
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    # we put the appending part in an else block
    # this way, only rows that don't throw an exception will be appended to the graph
    # we could alternatively implemented a "continue" instead, skipping this iteration of the loop if an error is thrown
"""Plot the high, low and date temperature data"""

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs,  color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

ax.set_title("Daily High Temps in Death Valley, in 2021", fontsize=21)
ax.set_xlabel('Dates', fontsize=16)
ax.set_ylabel('Temp (F)', fontsize=16)
ax.tick_params(labelsize=16)

fig.autofmt_xdate()
plt.show()